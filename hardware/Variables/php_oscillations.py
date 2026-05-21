# variables/php_oscillations.py
import math

def simulate_php_performance(inner_diameter_mm, fluid_filling_ratio, t_evap, t_cond, num_turns):
    """
    Models the passive oscillation frequency and effective thermal conductivity 
    of a Pulsating Heat Pipe micro-channel array.
    
    inner_diameter_mm: ID of the micro-channels (Must be small enough for capillary action, usually < 2mm)
    fluid_filling_ratio: Volumetric ratio of fluid inside (Optimal is usually 0.4 to 0.6)
    t_evap: Evaporator / Server chip temperature (C)
    t_cond: Condenser / Cooling loop inlet temperature (C)
    num_turns: Number of serpentine turns across the hot zone
    """
    dt = t_evap - t_cond
    d_meters = inner_diameter_mm / 1000.0
    
    if dt <= 0:
        return {"error": "Temperature delta must be positive to drive fluid oscillation."}
        
    # Check if diameter is small enough to maintain the capillary "slug-bubble" regime
    # Calculated via the Bond number limit (Bo < 4) using water/refrigerant averages
    # Critical diameter threshold formula: D_crit = 2 * sqrt(surface_tension / (g * (rho_l - rho_v)))
    if inner_diameter_mm > 2.5:
         regime_status = "Failed: Channel too wide. Fluid will stratify instead of oscillating."
    else:
        regime_status = "Active: Capillary forces will successfully form alternating liquid/vapor slugs."

    if "Failed" in regime_status:
        return {"regime": regime_status, "frequency_hz": 0, "effective_k_w_mk": 400} # Default to copper baseline

    # --- Approximation of Oscillation Dynamics ---
    # Frequency scales with heat input (dT) and filling ratio optimization
    # Optimal filling ratio (around 50%) yields the maximum kinetic oscillation
    filling_factor = 1.0 - abs(fluid_filling_ratio - 0.5) * 2.0 
    
    # Arbitrary empirical frequency scaling for sandbox variable testing
    frequency_hz = 1.5 * math.sqrt(dt) * filling_factor * (num_turns / 10.0)
    
    # Effective Thermal Conductivity calculation
    # Solid copper is ~400 W/m*K. An oscillating PHP can scale into the thousands.
    baseline_copper_k = 400
    kinetic_multiplier = 3.5 * frequency_hz * (1.0 / d_meters) * 0.001
    effective_k = baseline_copper_k + (kinetic_multiplier * num_turns)
    
    # Thermal resistance (R = L / (k * A)) assuming a 150mm transport length
    length = 0.15 
    area = (math.pi * (d_meters / 2)**2) * num_turns * 2
    thermal_resistance = length / (effective_k * area)

    return {
        "regime": regime_status,
        "frequency_hz": frequency_hz,
        "effective_k_w_mk": effective_k,
        "thermal_resistance_c_w": thermal_resistance,
        "copper_performance_ratio": effective_k / baseline_copper_k
    }

# --- Test Variables ---
channel_id = 1.2             # 1.2mm micro-channels to ensure capillary action
filling_ratio = 0.5          # 50% liquid, 50% vapor space (ideal baseline)
evaporator_temp = 60.0       # 60°C on the server silicon
condenser_temp = 45.0        # 45°C at the heat exchanger
serpentine_turns = 14        # Number of parallel micro-loops crossing the chip

results = simulate_php_performance(channel_id, filling_ratio, evaporator_temp, condenser_temp, serpentine_turns)

print(f"--- Pulsating Heat Pipe (PHP) Oscillation Sandbox ---")
print(f"Capillary Regime: {results['regime']}")
if "error" not in results and results['frequency_hz'] > 0:
    print(f"Estimated Internal Fluid Oscillation: {results['frequency_hz']:.2f} Hz")
    print(f"Effective Thermal Conductivity: {results['effective_k_w_mk']:.2f} W/m*K")
    print(f"Performance Relative to Pure Copper: {results['copper_performance_ratio']:.1f}x More Conductive")
    print(f"Total Array Thermal Resistance: {results['thermal_resistance_c_w']:.4f} °C/W")
