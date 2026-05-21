# variables/zeotropic_mix.py

def calculate_exergy_gain(fluid_type, t_source_in, t_source_out, mass_flow):
    """
    Rough calculation to compare pure fluids vs zeotropic mixtures
    t_source_in: Server coolant entry temp (C)
    t_source_out: Server coolant exit temp (C)
    """
    # Specific heat capacity approximation (kJ/kg*K)
    cp_coolant = 4.18 
    
    # Heat load from the servers (kW)
    q_fluid = mass_flow * cp_coolant * (t_source_in - t_source_out)
    
    if fluid_type == "pure":
        # Pure fluids lose energy due to the thermal mismatch (fixed boiling point)
        heat_exchanger_efficiency = 0.70
    elif fluid_type == "zeotropic_blend":
        # Zeotropic mixtures glide with the temperature profile, capturing more exergy
        heat_exchanger_efficiency = 0.84
    else:
        heat_exchanger_efficiency = 0.50

    net_thermal_harvest = q_fluid * heat_exchanger_efficiency
    return net_thermal_harvest

# --- Test Variables ---
server_temp_in = 55.0   # 55°C straight off the chips
server_temp_out = 45.0  # 45°C returning to the rack
flow_rate = 2.5         # kg/s

pure_yield = calculate_exergy_gain("pure", server_temp_in, server_temp_out, flow_rate)
zeo_yield = calculate_exergy_gain("zeotropic_blend", server_temp_in, server_temp_out, flow_rate)

print(f"--- Thermal Harvesting Sandbox Variables ---")
print(f"Baseline Pure Fluid Thermal Harvest: {pure_yield:.2f} kW")
print(f"Experimental Zeotropic Blend Harvest: {zeo_yield:.2f} kW")
print(f"Net Gain from Temperature Glide Optimization: {((zeo_yield - pure_yield) / pure_yield) * 100:.1f}% increase")
