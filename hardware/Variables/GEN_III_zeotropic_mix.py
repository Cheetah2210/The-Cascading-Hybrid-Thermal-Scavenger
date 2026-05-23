# variables/GEN_III_zeotropic_mix.py

import math
import logging

# Set up logging for thermodynamic calculations
logging.basicConfig(level=logging.INFO, format='%(message)s')

class ZeotropicFluidBlend:
    """
    Models a binary zeotropic fluid mixture to calculate temperature glide,
    vapor-liquid equilibrium (VLE), and thermodynamic exergy extraction.
    """
    def __init__(self, fluid_a_name, fluid_b_name, molar_fraction_a):
        self.name_A = fluid_a_name
        self.name_B = fluid_b_name
        self.x_A = molar_fraction_a  # Molar fraction of Fluid A in liquid phase
        self.x_B = 1.0 - molar_fraction_a
        
        # Antoine constants for vapor pressure calculation: log10(P) = A - (B / (T + C))
        # (Default values mapped to low-boiling point fluorocarbon/refrigerant profiles)
        self.antoine_A = {"A": 4.0, "B": 1100.0, "C": 230.0}
        self.antoine_B = {"A": 4.2, "B": 1250.0, "C": 220.0}

    def calculate_vapor_pressure(self, temperature_C, constants):
        """Calculates vapor pressure (bar) using Antoine equation."""
        p_sat = 10 ** (constants["A"] - (constants["B"] / (temperature_C + constants["C"])))
        return p_sat

    def calculate_bubble_point(self, target_pressure_bar):
        """Iteratively solves for the Bubble Point temperature (onset of boiling)."""
        low_t, high_t = -20.0, 150.0
        tolerance = 1e-4
        
        for _ in range(100):
            mid_t = (low_t + high_t) / 2.0
            p_sat_A = self.calculate_vapor_pressure(mid_t, self.antoine_A)
            p_sat_B = self.calculate_vapor_pressure(mid_t, self.antoine_B)
            
            # Raoult's Law for bubble point pressure
            p_bubble = (self.x_A * p_sat_A) + (self.x_B * p_sat_B)
            
            if abs(p_bubble - target_pressure_bar) < tolerance:
                return mid_t
            elif p_bubble < target_pressure_bar:
                low_t = mid_t
            else:
                high_t = mid_t
        return low_t

    def calculate_dew_point(self, target_pressure_bar):
        """Iteratively solves for the Dew Point temperature (complete vaporization)."""
        low_t, high_t = -20.0, 150.0
        tolerance = 1e-4
        
        for _ in range(100):
            mid_t = (low_t + high_t) / 2.0
            p_sat_A = self.calculate_vapor_pressure(mid_t, self.antoine_A)
            p_sat_B = self.calculate_vapor_pressure(mid_t, self.antoine_B)
            
            # Raoult's Law for dew point pressure
            if p_sat_A == 0 or p_sat_B == 0:
                low_t = mid_t
                continue
            p_dew = 1.0 / ((self.x_A / p_sat_A) + (self.x_B / p_sat_B))
            
            if abs(p_dew - target_pressure_bar) < tolerance:
                return mid_t
            elif p_dew < target_pressure_bar:
                low_t = mid_t
            else:
                high_t = mid_t
        return low_t

    def analyze_glide_performance(self, operating_pressure_bar, t_ambient_K=298.15):
        """
        Calculates the temperature glide profile and performs second-law
        exergy analysis for energy harvesting evaluation.
        """
        # 1. Determine phase change temperatures (Celsius and Kelvin)
        t_bubble_C = self.calculate_bubble_point(operating_pressure_bar)
        t_dew_C = self.calculate_dew_point(operating_pressure_bar)
        
        t_bubble_K = t_bubble_C + 273.15
        t_dew_K = t_dew_C + 273.15
        
        # Temperature Glide ΔT (Crucial for non-isothermal matches)
        temperature_glide = t_dew_C - t_bubble_C
        
        # 2. Entropic and Exergetic Math
        # Idealized specific heat capacities (kJ/kg·K)
        cp_mix = 1.35 
        h_evap_mix = 165.0  # Latent heat of vaporization (kJ/kg)
        
        # Enthalpy change (Δh) and Entropy change (Δs) during phase glide
        delta_h = (cp_mix * temperature_glide) + h_evap_mix
        delta_s = (cp_mix * math.log(t_dew_K / t_bubble_K)) + (h_evap_mix / t_bubble_K)
        
        # Total Available Exergy (Maximum theoretical work potential)
        available_exergy = delta_h - (t_ambient_K * delta_s)
        
        # Expected extraction efficiency scaling factor based on the glide profile
        glide_efficiency_multiplier = min(0.85, 0.40 + (temperature_glide * 0.025))
        target_exergy_extracted = available_exergy * glide_efficiency_multiplier

        # Log results to console
        logging.info("=========================================================")
        logging.info(f" ZEOTROPIC BLEND ANALYSIS: {self.name_A} ({self.x_A*100}%) + {self.name_B} ({self.x_B*100}%)")
        logging.info("=========================================================")
        logging.info(f"Operating Pressure      : {operating_pressure_bar:.2f} bar")
        logging.info(f"Bubble Point (Liquid)   : {t_bubble_C:.2f} °C ({t_bubble_K:.2f} K)")
        logging.info(f"Dew Point (Vapor)       : {t_dew_C:.2f} °C ({t_dew_K:.2f} K)")
        logging.info(f"Phase Temperature Glide : {temperature_glide:.2f} K")
        logging.info(f"Total Phase Enthalpy Δh : {delta_h:.2f} kJ/kg")
        logging.info(f"Total Phase Entropy Δs  : {delta_s:.4f} kJ/kg·K")
        logging.info(f"Available Exergy Pool   : {available_exergy:.2f} kJ/kg")
        logging.info(f"Predicted Exergy Yield  : {target_exergy_extracted:.2f} kJ/kg")
        logging.info("=========================================================\n")
        
        return {
            "glide_K": temperature_glide,
            "exergy_pool_kj_kg": available_exergy,
            "exergy_yield_kj_kg": target_exergy_extracted
        }

# ---------------------------------------------------------------------------
# Test Verification Run
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Initialize fluid matrix (60% High-Conductivity Phase A, 40% Low-Boiling Phase B)
    blend = ZeotropicFluidBlend("Fluorochemical-Core", "Volatile-Carrier", molar_fraction_a=0.60)
    
    # Analyze blend performance at standard system operating pressure (2.5 bar)
    blend.analyze_glide_performance(operating_pressure_bar=2.5)
