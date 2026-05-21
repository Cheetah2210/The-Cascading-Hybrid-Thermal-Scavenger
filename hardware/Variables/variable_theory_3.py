# variables/variable_theory_3.py
import math

def run_generation_3_ehd_theory():
    print(f"====================================================")
    print(f"   EHD-ENHANCED HIGH-YIELD SCAVENGER GRID GEN III   ")
    print(f"====================================================\n")
    
    # --- Enterprise Scaling Constraints ---
    t_coolant_in = 65.0   # Facility-side hot coolant arrival loop (°C)
    t_ambient = 15.0      # External cooling tower sink (°C)
    total_nodes = 4       
    base_thermal_w = 4000.0 * total_nodes # 16kW raw facility heat load
    
    print(f"[Enterprise Profile: Plug-and-Play Facility Loop]")
    print(f"Incoming Facility Coolant: {t_coolant_in}°C | Sink: {t_ambient}°C")
    print(f"Total Thermal Energy Handled: {base_thermal_w:.2f} W\n")

    # --------------------------------------------------------
    # STEP 1: Electro-Hydrodynamic (EHD) Boiling Maximizer
    # --------------------------------------------------------
    # Using low-current electric fields to artificially remove fluid boundary layer resistance
    ehd_overhead_w = 12.0 * total_nodes   # Negligible power required for voltage fields
    ehd_heat_transfer_multiplier = 3.5    # 350% increase in phase change velocity
    
    # EHD drastically lowers the thermal drop needed to drive the cycle
    t_cascade_in = t_coolant_in - 1.5     # Only 1.5°C drop across interface due to EHD velocity
    
    print(f"[Layer 1: External EHD Phase-Change Maximizer]")
    print(f" -> Electrical Overhead:       {ehd_overhead_w:.2f} W (Micro-Amps at High Voltage)")
    print(f" -> Active Phase Acceleration: {ehd_heat_transfer_multiplier * 100:.0f}% Velocity Multiplier")
    print(f" -> Cascade Operational Input: {t_cascade_in:.1f}°C\n")

    # --------------------------------------------------------
    # STEP 2: Active Solid-State Thermal Uplift
    # --------------------------------------------------------
    pumping_power_input_w = 280.0 * total_nodes # Reduced pump restriction due to EHD fluidity
    coefficient_of_performance = 3.8            # Enhanced COP due to maximized heat transfer
    
    elevated_thermal_load_w = base_thermal_w + (pumping_power_input_w * coefficient_of_performance)
    t_fluid_elevated = 130.0                    # Elevated temperature threshold (°C)

    print(f"[Layer 2: External Heat Uplift Stage]")
    print(f" -> Active Pumping Power:      {pumping_power_input_w:.2f} W")
    print(f" -> Superheated Fluid Output:  {t_fluid_elevated:.1f}°C\n")

    # --------------------------------------------------------
    # STEP 3: EHD-Driven Multi-Stage Cascading Expansion Nodes
    # --------------------------------------------------------
    print(f"[Layer 3: EHD-Enhanced Fluidic Node Cascade]")
    
    # EHD allows our exergy extraction efficiencies to climb into unprecedented bounds
    node_stages = [
        {"name": "Stage 1 (Hyper-Dense Loop)", "t_in": 130.0, "t_out": 85.0,  "exergy_eff": 0.94},
        {"name": "Stage 2 (Mid-Range Cascade)", "t_in": 85.0,  "t_out": 45.0,  "exergy_eff": 0.95},
        {"name": "Stage 3 (Low-Grade Tail)",    "t_in": 45.0,  "t_out": 20.0,  "exergy_eff": 0.96}
    ]
    
    total_fluid_cascade_harvest_w = 0
    remaining_fluid_thermal_w = elevated_thermal_load_w
    
    for stage in node_stages:
        th_k = stage["t_in"] + 273.15
        tc_k = stage["t_out"] + 273.15
        stage_carnot = 1.0 - (tc_k / th_k)
        
        # Power harvested via high-velocity EHD phase expansion
        stage_harvest_w = remaining_fluid_thermal_w * stage_carnot * stage["exergy_eff"]
        total_fluid_cascade_harvest_w += stage_harvest_w
        
        print(f" -> {stage['name']}: Node Harvest = {stage_harvest_w:.2f} W")
        remaining_fluid_thermal_w -= stage_harvest_w

    # --------------------------------------------------------
    # TOTAL SYSTEM CONSOLIDATION
    # --------------------------------------------------------
    total_system_overhead_w = pumping_power_input_w + ehd_overhead_w
    net_recovered_electrical_w = total_fluid_cascade_harvest_w - total_system_overhead_w
    net_data_center_return_pct = (net_recovered_electrical_w / base_thermal_w) * 100

    print(f"\n====================================================")
    print(f"             GEN III FACILITY VERDICT               ")
    print(f"====================================================")
    print(f"Gross Fluidic Cascade Harvest:   {total_fluid_cascade_harvest_w:.2f} W")
    print(f"Total Facility System Overhead: -{total_system_overhead_w:.2f} W")
    print(f"----------------------------------------------------")
    print(f"Net Recovered Facility Power:    {net_recovered_electrical_w:.2f} W")
    print(f"Total Net Energy Return Metric:  {net_data_center_return_pct:.1f}%")
    print(f"====================================================")

if __name__ == "__main__":
    run_generation_3_ehd_theory()
