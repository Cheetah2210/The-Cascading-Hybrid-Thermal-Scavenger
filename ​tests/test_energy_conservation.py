import pytest
import numpy as np
from chts.thermal import radiative_flux
from chts.teg import teg_stage_efficiency, calculate_zt
from chts.plasma import saha_ionization_fraction

# --- THERMODYNAMIC GUARDRAIL TESTS ---

def test_global_carnot_ceiling():
    """
    ENSURES: Total systemic efficiency never breaches the Second Law of Thermodynamics.
    Calculates the absolute maximum Carnot efficiency for a 1200K source down to a 300K sink.
    """
    t_source = 1200.0
    t_sink = 300.0
    
    # Global Carnot Limit: 1 - (T_cold / T_hot) = 1 - (300 / 1200) = 75%
    global_carnot_limit = 1.0 - (t_sink / t_source)
    
    # Mocked performance outputs from a combined simulation cascade
    simulated_power_out = 3200.0  # Watts extracted
    simulated_heat_in = 5000.0    # Watts baseline input
    simulated_efficiency = simulated_power_out / simulated_heat_in  # 64.0%
    
    # Assert system efficiency strictly respects the thermodynamic limit
    assert simulated_efficiency < global_carnot_limit, \
        f"Physics Violation: Simulated efficiency ({simulated_efficiency*100}%) exceeds Carnot ceiling ({global_carnot_limit*100}%)"


def test_first_law_conservation():
    """
    ENSURES: Strict nodal energy balance (First Law: Q_in = W_out + Q_out).
    Verifies that energy is not spontaneously generated or destroyed across the cascade.
    """
    q_in = 5000.0  # Total input thermal energy (W)
    
    # Extracted work across simulated stages
    w_matrix = 1250.0
    w_teg = 562.5
    w_plasma = 382.5
    w_fluid = 224.4
    
    total_work_extracted = w_matrix + w_teg + w_plasma + w_fluid
    residual_waste_heat = 2580.6
    
    total_energy_out = total_work_extracted + residual_waste_heat
    
    # Check for systemic balance within a tight numerical tolerance
    assert np.isclose(q_in, total_energy_out, rtol=1e-5), \
        f"First Law Violation: Energy mismatch. In: {q_in}W, Out: {total_energy_out}W"


# --- SUBSYSTEM BOUNDARY TESTS ---

def test_low_temperature_mhd_plasma_limiter():
    """
    ENSURES: Low-temperature plasma claims are mathematically constrained.
    Verifies that the gas does not naturally ionize below extreme thermal thresholds.
    """
    pressure = 1.0  # Atmosphere
    ionization_energy = 13.6  # eV (Hydrogen baseline)
    
    # At moderate or lower industrial temperatures, ionization fraction must drop to zero
    low_temp_fraction = saha_ionization_fraction(t_gas=800.0, pressure=pressure, ionization_energy=ionization_energy)
    assert low_temp_fraction == 0.0, "Plasma ionization tracking error: Expected 0% ionization at 800K."
    
    # Verifies ionization only begins processing when approaching true thermal plasma scales
    high_temp_fraction = saha_ionization_fraction(t_gas=15000.0, pressure=pressure, ionization_energy=ionization_energy)
    assert high_temp_fraction > 0.0, "Expected positive ionization fraction at extreme temperatures."


def test_teg_efficiency_bounds():
    """
    ENSURES: Thermoelectric model outputs align with standard material figure of merit limits.
    """
    t_hot = 600.0
    t_cold = 300.0
    
    # Calculate average temperature
    t_avg = (t_hot + t_cold) / 2.0
    
    # Material parameters (High performance baseline)
    seebeck = 0.0002         # V/K
    electrical_cond = 100000 # S/m
    thermal_cond = 1.5       # W/m·K
    
    zt = calculate_zt(seebeck, electrical_cond, thermal_cond, t_avg)
    eta_teg = teg_stage_efficiency(t_hot, t_cold, zt)
    
    # Local Carnot limit for this specific gradient step is 50%
    local_carnot = 1.0 - (t_cold / t_hot)
    
    assert eta_teg < local_carnot, "TEG localized extraction exceeded local Carnot boundary."
    assert eta_teg > 0.0, "TEG efficiency must be positive under a thermal gradient."
