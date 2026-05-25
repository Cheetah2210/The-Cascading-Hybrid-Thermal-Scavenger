import numpy as np
from variables.variable_theory_testing import simulate_real_mhd_node

class CascadedExergyOrchestrator:
    """
    Orchestrates a multi-stage thermal cascade. Evaluates sequential energy 
    extraction across non-ideal fluidic, solid-state, and radiative boundaries.
    """
    def __init__(self, t_source, t_ambient, initial_heat_flux):
        self.t_source = t_source        # K (Primary High-Temp Node)
        self.t_ambient = t_ambient      # K (Ultimate Environmental Sink)
        self.q_in = initial_heat_flux   # Watts (Input thermal capacity)
        
        self.nodes = []
        self.extracted_power = []
        self.rejected_heat = [initial_heat_flux]
        self.node_temperatures = [t_source]

    def process_mhd_stage(self, name, velocity, flux_density, conductivity, fluid_props, geometry):
        """
        Processes the Gen III MHD fluid layer. Captures realistic electrical power 
        and extracts the hydraulic pumping work penalty from the net energy yield.
        """
        current_q_in = self.rejected_heat[-1]
        t_current = self.node_temperatures[-1]
        
        # Calculate local Carnot limit for validation reporting
        local_carnot = 1.0 - (self.t_ambient / t_current)
        
        # Invoke the non-ideal MHD simulation engine
        mhd_metrics = simulate_real_mhd_node(
            fluid_velocity=velocity,
            flux_density=flux_density,
            conductivity=conductivity,
            properties=fluid_props,
            geometry=geometry,
            load_factor=0.5  # Matched load optimization
        )
        
        # Factor in mechanical pumping work overhead to find NET electrical power.
        # W_pump = Volume_flow_rate * Delta_P = (w * h * velocity) * Total_Pressure_Drop
        v_flow_rate = geometry['w'] * geometry['h'] * velocity
        pumping_power_penalty = v_flow_rate * (mhd_metrics['total_pressure_drop_kPa'] * 1000)
        
        net_stage_power = mhd_metrics['net_power_W'] - pumping_power_penalty
        
        # Guardrail: If drag penalties completely overwhelm generation, clip output to zero
        net_stage_power = max(0.0, net_stage_power)
        
        # Energy Balance (1st Law): Q_out = Q_in - W_net
        current_q_out = current_q_in - net_stage_power
        
        # Predict temperature drop based on extracted energy and bulk properties
        # Approximated via a standard non-linear thermal degradation curve
        t_next = max(t_current * (current_q_out / current_q_in)**0.25, self.t_ambient)
        
        # Append data to the cascade registry
        self.nodes.append(name)
        self.extracted_power.append(net_stage_power)
        self.rejected_heat.append(current_q_out)
        self.node_temperatures.append(t_next)

    def process_solid_state_stage(self, name, analytical_efficiency):
        """
        Processes downstream solid-state elements (TEG layers/Radiative blocks).
        Bounded by localized temperature-dependent ceilings.
        """
        current_q_in = self.rejected_heat[-1]
        t_current = self.node_temperatures[-1]
        
        local_carnot = 1.0 - (self.t_ambient / t_current)
        
        # Enforce the Second Law constraint dynamically
        if analytical_efficiency >= local_carnot:
            analytical_efficiency = local_carnot * 0.85  # Bound to real-world operational degradation
            
        net_stage_power = current_q_in * analytical_efficiency
        current_q_out = current_q_in - net_stage_power
        t_next = max(t_current * (current_q_out / current_q_in)**0.25, self.t_ambient)
        
        self.nodes.append(name)
        self.extracted_power.append(net_stage_power)
        self.rejected_heat.append(current_q_out)
        self.node_temperatures.append(t_next)

    def generate_system_report(self):
        """Validates global metrics and outputs the system energy balance log."""
        total_net_power = sum(self.extracted_power)
        global_efficiency = total_net_power / self.q_in
        global_carnot = 1.0 - (self.t_ambient / self.t_source)
        
        print("\n=======================================================")
        print("   CHTS GENERATION III SYSTEM DEEP EXERGY ANALYSIS")
        print("=======================================================")
        print(f"Primary Thermal Source:   {self.t_source:.1f} K")
        print(f"Ambient Environment Sink: {self.t_ambient:.1f} K")
        print(f"Initial Heat Input:       {self.q_in / 1000:.2f} kW")
        print("-------------------------------------------------------")
        
        for i, stage in enumerate(self.nodes):
            print(f"Node [{i+1}] {stage.ljust(22)}: Net Power = {self.extracted_power[i]:.2f} W | Boundary Temp = {self.node_temperatures[i+1]:.1f} K")
            
        print("-------------------------------------------------------")
        print(f"Total System Net Power:   {total_net_power / 1000:.3f} kW")
        print(f"Residual System Waste:    {self.rejected_heat[-1] / 1000:.3f} kW")
        print(f"Realized Net Efficiency:  {global_efficiency * 100:.2f}%")
        print(f"Absolute Carnot Ceiling:  {global_carnot * 100:.2f}%")
        print(f"Thermodynamic Integrity:  {'PASSED' if global_efficiency < global_carnot else 'FAILED'}")
        print("=======================================================\n")

# --- CASCADE EVALUATION RUN ---
if __name__ == "__main__":
    # Define primary thermal cluster baseline (1200K source, 300K ambient, 10kW initial flux)
    cascade = CascadedExergyOrchestrator(t_source=1200.0, t_ambient=300.0, initial_heat_flux=10000.0)
    
    # Establish fluidic parameters matching our non-ideal variable_theory_3 module
    galinstan_boundary_props = {
        'rho': 6440.0,
        'nu': 3.73e-7,
        'mu_e': 1.2e-4,
        'r_contact': 1.5e-4  # 0.15 mOhm contact fouling resistance
    }
    mhd_geometry = {'w': 0.025, 'h': 0.010, 'L': 0.120}
    
    # Stage 1: The Bounded High-Temperature MHD Loop
    cascade.process_mhd_stage(
        name="Gen III EHD/MHD Loop",
        velocity=3.5,            # m/s fluid speed
        flux_density=1.2,        # 1.2 Tesla N52 array field
        conductivity=3.46e6,     # S/m
        fluid_props=galinstan_boundary_props,
        geometry=mhd_geometry
    )
    
    # Stage 2: Thermoelectric Core (Fed by the residual heat of Stage 1)
    cascade.process_solid_state_stage("TEG Sandwich Array", analytical_efficiency=0.14)
    
    # Stage 3: Low-Temperature Downstream Scavenger Loop
    cascade.process_solid_state_stage("Fluidic Phase Glide Loop", analytical_efficiency=0.07)
    
    # Execute structural report
    cascade.generate_system_report()
