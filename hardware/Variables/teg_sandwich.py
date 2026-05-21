# variables/teg_sandwich.py

def calculate_teg_co_generation(t_chips, t_fluid_target, num_modules):
    """
    Calculates direct electrical harvest from Seebeck-effect TEG modules
    layered between server chips and the primary fluid recovery loop.
    
    t_chips: Temperature of the running silicon (C)
    t_fluid_target: Target temperature of the fluid loop entering the scavenger (C)
    num_modules: Total number of TEG units in the server rack array
    """
    # Convert inputs to Kelvin for standard thermodynamics
    th = t_chips + 273.15
    tc = t_fluid_target + 273.15
    dt = th - tc
    
    if dt <= 0:
        return {
            "error": "Temperature difference must be positive. Chips must be hotter than the fluid loop."
        }
    
    # Typical standard parameters for a single bismuth telluride (Bi2Te3) commercial TEG module:
    # Seebeck Coefficient (V/K) per module approximation
    seebeck_alpha = 0.035  
    # Internal electrical resistance (Ohms)
    internal_r = 1.5       
    # Thermal conductivity (W/K) per module
    thermal_k = 0.25       
    
    # 1. Open Circuit Voltage (V = alpha * dT)
    v_open = seebeck_alpha * dt
    
    # 2. Maximum Power Output assuming matched load resistance (P_max = V_open^2 / (4 * R_internal))
    p_electrical_per_module = (v_open ** 2) / (4 * internal_r)
    total_teg_electrical_output = p_electrical_per_module * num_modules
    
    # 3. Total Thermal Energy conducted through the TEGs to the fluid loop (Q = k * dT * modules)
    # This represents the residual heat passed down to the fluid loop (in Watts)
    q_passed_to_fluid = (thermal_k * dt * num_modules)
    
    return {
        "temperature_delta_c": dt,
        "teg_electrical_w": total_teg_electrical_output,
        "fluid_thermal_w": q_passed_to_fluid,
        "total_energy_handled_w": total_teg_electrical_output + q_passed_to_fluid
    }

# --- Test Variables ---
chip_temperature = 65.0      # Keeping the silicon at a safe, steady 65°C under load
fluid_loop_temperature = 45.0 # Fluid cooling loop running at 45°C
total_modules = 32           # Modeling an array scaled across a high-density node space

results = calculate_teg_co_generation(chip_temperature, fluid_loop_temperature, total_modules)

print(f"--- TEG Co-Generation Sandwich Variables ---")
if "error" in results:
    print(f"Error: {results['error']}")
else:
    print(f"Temperature Gradient across TEG: {results['temperature_delta_c']:.1f}°C")
    print(f"Direct Solid-State Electricity Generated: {results['teg_electrical_w']:.2f} W")
    print(f"Residual Thermal Energy Passed to Fluid Loop: {results['fluid_thermal_w']:.2f} W")
    print(f"Total Scavenged Power Entering Hybrid Loop: {results['total_energy_handled_w']:.2f} W")
    print(f"\nNet Gain: {results['teg_electrical_w']:.2f} Watts of pure DC power unlocked instantly.")
