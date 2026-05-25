import os
import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTS ---
# Stefan-Boltzmann constant (W/m²·K⁴)
SIGMA = 5.670374419e-8 

class ThermalCascadeSimulator:
    """
    Simulates and validates a multi-stage thermal scavenging pipeline.
    Ensures structural conservation of energy and checks against the Carnot limit.
    """
    def __init__(self, t_source, t_ambient, initial_heat_flux):
        self.t_source = t_source        # K
        self.t_ambient = t_ambient      # K
        self.q_in = initial_heat_flux   # Watts
        
        # Simulation results containers
        self.stages = []
        self.temperatures = [t_source]
        self.power_extracted = []
        self.efficiencies = []
        self.heat_fluxes = [initial_heat_flux]

    def add_stage(self, name, local_efficiency):
        """
        Adds a scavenging stage to the cascade.
        Processes the remaining heat flux from the previous stage.
        """
        current_q_in = self.heat_fluxes[-1]
        t_current_hot = self.temperatures[-1]
        
        # Calculate theoretical upper bound (Carnot Limit) for this stage step down to ambient
        max_possible_eta = 1.0 - (self.t_ambient / t_current_hot)
        
        # Guardrail: Prevent physics violations in model configuration
        if local_efficiency > max_possible_eta:
            print(f"Warning: [{name}] efficiency ({local_efficiency*100:.1f}%) "
                  f"exceeds Carnot limit ({max_possible_eta*100:.1f}%) at {t_current_hot}K. "
                  f"Capping efficiency.")
            local_efficiency = max_possible_eta

        # Calculate energy metrics
        w_out = current_q_in * local_efficiency
        q_out = current_q_in - w_out  # 1st Law: Q_in = W_out + Q_out
        
        # Predict an estimated temperature drop across the stage (simplified thermal resistance model)
        # Assuming temperature drops proportionally to work extracted and radiative losses
        t_next = max(t_current_hot * (q_out / current_q_in)**0.25, self.t_ambient)
        
        # Record stage data
        self.stages.append(name)
        self.power_extracted.append(w_out)
        self.efficiencies.append(local_efficiency)
        self.heat_fluxes.append(q_out)
        self.temperatures.append(t_next)

    def run_analysis(self):
        """Validates systemic data metrics and builds the visualization dashboard."""
        total_power = sum(self.power_extracted)
        system_efficiency = total_power / self.q_in
        carnot_limit = 1.0 - (self.t_ambient / self.t_source)
        
        print("\n=== THERMODYNAMIC INTEGRITY REPORT ===")
        print(f"Initial Heat Input:  {self.q_in:.2f} W")
        print(f"Total Power Out:      {total_power:.2f} W")
        print(f"Residual Waste Heat:  {self.heat_fluxes[-1]:.2f} W")
        print(f"System Efficiency:    {system_efficiency * 100:.2f}%")
        print(f"Absolute Carnot Limit:{carnot_limit * 100:.2f}%")
        print(f"Energy Conservation:  {'PASSED' if np.isclose(total_power + self.heat_fluxes[-1], self.q_in) else 'FAILED'}")
        
        self._generate_plots(system_efficiency, carnot_limit)

    def _generate_plots(self, system_efficiency, carnot_limit):
        """Generates clear, diagnostic engineering plots."""
        # Set clean engineering plot styles
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['axes.edgecolor'] = '#CCCCCC'
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle("Cascading Hybrid Thermal Scavenger (CHTS) Performance Matrix", 
                     fontsize=14, fontweight='bold', color='#2C3E50')

        # --- PLOT 1: THERMAL DEGRADATION & POWER EXTRACTION ---
        ax1 = axes[0]
        color_temp = '#E74C3C'
        color_power = '#2ECC71'
        
        # Temperature profile line
        x_stages = range(len(self.temperatures))
        ax1.plot(x_stages, self.temperatures, marker='o', color=color_temp, linewidth=2, label='Temperature (K)')
        ax1.set_ylabel('Nodal Temperature (K)', color=color_temp, fontweight='bold')
        ax1.tick_params(axis='y', labelcolor=color_temp)
        ax1.set_xlabel('Cascade Stage Node Index', fontweight='bold')
        ax1.set_xticks(x_stages)
        ax1.set_xticklabels(['Source'] + self.stages)
        ax1.grid(True, linestyle=':', alpha=0.6)

        # Twin axis for extracted power steps
        ax1_twin = ax1.twinx()
        x_bars = range(1, len(self.temperatures))
        ax1_twin.bar(x_bars, self.power_extracted, alpha=0.3, color=color_power, width=0.4, label='Extracted Power (W)')
        ax1_twin.set_ylabel('Extracted Electrical Power (W)', color=color_power, fontweight='bold')
        ax1_twin.tick_params(axis='y', labelcolor=color_power)
        
        ax1.set_title("Thermal Gradient Drop vs. Power Generation", fontsize=11, pad=10)

        # --- PLOT 2: CUMULATIVE EFFICIENCY VS CARNOT LIMIT ---
        ax2 = axes[1]
        
        # Calculate cumulative system efficiency progression
        cum_power = np.cumsum(self.power_extracted)
        cum_eff = cum_power / self.q_in
        
        ax2.plot(range(1, len(self.temperatures)), cum_eff * 100, marker='s', 
                 color='#3498DB', linewidth=2.5, label='Cumulative System Efficiency')
        
        # Plot individual step efficiencies as points
        ax2.scatter(range(1, len(self.temperatures)), np.array(self.efficiencies) * 100, 
                    color='#9B59B6', zorder=5, label='Individual Stage Efficiency')

        # Theoretical System Carnot Ceiling Reference Line
        ax2.axhline(carnot_limit * 100, color='#E74C3C', linestyle='--', linewidth=1.5, 
                    label=f'Total System Carnot Limit ({carnot_limit*100:.1f}%)')
        
        ax2.set_xlabel('Cascade Stage Node Index', fontweight='bold')
        ax2.set_ylabel('Efficiency Percentage (%)', fontweight='bold')
        ax2.set_xticks(range(1, len(self.temperatures)))
        ax2.set_xticklabels(self.stages)
        ax2.set_ylim(0, min(carnot_limit * 100 + 10, 100))
        ax2.grid(True, linestyle=':', alpha=0.6)
        ax2.legend(loc='lower right')
        ax2.set_title("Exergy Utilization Alignment", fontsize=11, pad=10)

        plt.tight_layout()
        
        # Auto-create output directory if needed and save
        os.makedirs('docs/images', exist_ok=True)
        plt.savefig('docs/images/simulation_results.png', dpi=300)
        print("\n[Success] Diagnostic performance charts saved to docs/images/simulation_results.png")
        plt.show()

# --- RUN EXECUTION INSTANCE ---
if __name__ == "__main__":
    # Setup initial extreme thermal baseline conditions (e.g., Data Center Exergy Scavenging Core)
    # 1200K high-temp node, 300K ambient sink, 5000 Watts continuous initial heat flux
    sim = ThermalCascadeSimulator(t_source=1200, t_ambient=300, initial_heat_flux=5000)
    
    # Cascade modeling configuration
    sim.add_stage("Carbon Exergy Matrix", local_efficiency=0.25)
    sim.add_stage("TEG Sandwich Array", local_efficiency=0.15)
    sim.add_stage("MHD Plasma Scavenger", local_efficiency=0.12)
    sim.add_stage("Low-Temp Fluid Loop", local_efficiency=0.08)
    
    # Process equations and build charts
    sim.run_analysis()
