import numpy as np

def calculate_mhd_power(T_exhaust, T_ambient, magnetic_flux_density, fluid_conductivity, channel_width, channel_height):
    """
    Simulates the fluid expansion and MHD power output for the CHTS Stage 1 Core.
    
    Parameters:
    T_exhaust (float): Server exhaust temperature in Celsius (e.g., 55 C)
    T_ambient (float): Ambient cooling air temperature in Celsius (e.g., 22 C)
    magnetic_flux_density (float): Strength of the permanent magnets in Tesla (B)
    fluid_conductivity (float): Electrical conductivity of the fluid mix in Siemens/meter (sigma)
    channel_width (float): Width of the MHD channel in meters (w)
    channel_height (float): Height of the MHD channel in meters (h)
    """
    # Convert temperatures to Kelvin
    Th = T_exhaust + 273.15
    Tc = T_ambient + 273.15
    
    # Ideal Carnot efficiency limit for this specific delta T
    carnot_efficiency = 1.0 - (Tc / Th)
    
    # Estimate fluid expansion velocity (v) based on low-boiling phase change pressure drop
    # Assumes optimized nozzle geometry converting thermal expansion into kinetic velocity
    R_fluid = 240.0  # Specific fluid gas constant proxy (J/kg*K)
    velocity = np.sqrt(2 * R_fluid * (Th - Tc) * 0.4) # 40% kinetic conversion efficiency profile
    
    # Cross-sectional area of the channel
    area = channel_width * channel_height
    
    # Open-circuit Faraday voltage induced across the channel width: V = B * w * v
    induced_voltage = magnetic_flux_density * channel_width * velocity
    
    # Internal electrical resistance of the moving fluid volume: R = w / (sigma * length * h)
    # Assumes a 10cm active magnetic channel length
    channel_length = 0.1 
    internal_resistance = channel_width / (fluid_conductivity * channel_length * channel_height)
    
    # Peak power extraction occurs at matched load impedance (R_load = R_internal)
    # P_max = V^2 / (4 * R_internal)
    max_power_output = (induced_voltage ** 2) / (4 * internal_resistance)
    
    print("--- CHTS Stage 1 Core Simulation Results ---")
    print(f"Thermodynamic Carnot Limit:    {carnot_efficiency * 100:.2f}%")
    print(f"Calculated Fluid Velocity:     {velocity:.2f} m/s")
    print(f"Induced Peak Voltage:          {induced_voltage * 1000:.2f} mV")
    print(f"Fluid Channel Resistance:     {internal_resistance:.4f} Ohms")
    print(f"Estimated Max Power Output:    {max_power_output * 1000:.2f} mW per channel")
    print(f"--------------------------------------------")
    
    return max_power_output

if __name__ == "__main__":
    # Test execution parameters
    calculate_mhd_power(
        T_exhaust=55.0,            # High-density rack exhaust temp
        T_ambient=22.0,            # Intake/ambient data center floor temp
        magnetic_flux_density=1.2, # Strong Neodymium (N52) permanent magnet profile (Tesla)
        fluid_conductivity=250.0,  # Ionized / liquid metal suspension proxy (S/m)
        channel_width=0.02,        # 2 cm wide micro-channel microfluidic block
        channel_height=0.005       # 5 mm channel height
    )
