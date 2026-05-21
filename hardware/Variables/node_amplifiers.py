# variables/node_amplifiers.py

def simulate_amplified_cascade(initial_tick_w, num_nodes, amplification_gain):
    print(f"--- Cascading Node Amplifier Sandbox ---")
    print(f"Initial Input Signal: {initial_tick_w:.4f} Watts\n")
    
    current_signal = initial_tick_w
    total_harvested_power = 0
    
    for node in range(1, num_nodes + 1):
        # The node takes the small incoming tick and amplifies the physical output
        amplified_output = current_signal * amplification_gain
        
        # We harvest a portion of this amplified force as electricity
        harvested_electricity = amplified_output * 0.15  # 15% harvesting efficiency per node
        total_harvested_power += harvested_electricity
        
        print(f"Node {node}:")
        print(f" -> Incoming Trigger Trigger: {current_signal:.4f} W")
        print(f" -> Amplified Stage Force:   {amplified_output:.2f} W")
        print(f" -> Electrical Yield:         {harvested_electricity:.2f} W")
        
        # The remaining kinetic/thermal force passes down to become the trigger for the next stage
        current_signal = amplified_output * 0.05  # A small residual fraction acts as the next tick
        print(f" -> Residual Passed Down:     {current_signal:.4f} W\n")
        
    print(f"====================================================")
    print(f"Total Cumulative Power Harvested: {total_harvested_power:.2f} Watts")
    print(f"====================================================")

# --- Test Variables ---
trigger_force = 0.05       # A tiny 50-milliwatt "tick" to start the cascade
stages = 4                 # 4 progressive step-down nodes
gain_factor = 25.0         # Each node uses ambient pressure/heat to amplify the force 25x

simulate_amplified_cascade(trigger_force, stages, gain_factor)
