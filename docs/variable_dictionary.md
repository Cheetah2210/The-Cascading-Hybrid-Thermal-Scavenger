# CHTS Comprehensive Variable Dictionary & Physics Matrix
## Master Mathematical Index for Sandbox Simulation Verification

This document compiles, defines, and maps every mathematical variable, physical constant, and tracking coefficient used across the Cascading Hybrid Thermal Scavenger (CHTS) architecture tracks.

---

## 1. Primary Magnetohydrodynamic (MHD) & Fluid Dynamics Variables

These variables govern the primary, solid-state capillary loop where thermal phase-expansion drives fluid across an orthogonal magnetic flux field.

| Variable | Definition | SI Units | Core Mathematical Function / Context | Code Domain |
| :--- | :--- | :--- | :--- | :--- |
| **$v_y$** | Transverse Fluid Velocity | $\text{m/s}$ | Measures the physical flow rate of the working fluid core driven by thermal phase expansion through the micro-channels. | `variables/php_oscillations.py` |
| **$v_{\text{avg}}$** | Mean Volumetric Velocity | $\text{m/s}$ | The integrated average velocity across the conduit cross-section used to calculate net induced Faraday voltage. | `variables/node_amplifiers.py` |
| **$v_{\text{slip}}$** | Boundary Wall Slip Velocity | $\text{m/s}$ | The non-zero velocity profile achieved directly at the solid-fluid interface when the no-slip condition is broken. | `variables/node_amplifiers.py` |
| **$\rho$** | Fluid Density | $\text{kg/m}^3$ | Evaluates mass-inertial resistance to acceleration within the modified Navier-Stokes momentum equations. | `variables/php_oscillations.py` |
| **$\mu$** | Dynamic Viscosity | $\text{Pa}\cdot\text{s}$ | Quantifies the internal fluid friction and resistance to shear deformation during high-speed plug flow states. | `variables/node_amplifiers.py` |
| **$p$** | Localized Fluid Pressure | $\text{Pa}$ | Transverse pressure gradient developed along the capillary loop via localized volumetric expansion. | `variables/php_oscillations.py` |
| **$w$** | Channel Internal Width | $\text{m}$ | The physical distance between the parallel electrode plates capturing the induced EMF field. | `variables/teg_sandwich.py` |

---

## 2. Electromagnetics & Lorentz Force Vector Variables

These variables model the solid-state conversion of kinetic fluid motion into electrical current via localized magnetic fields.

| Variable | Definition | SI Units | Core Mathematical Function / Context | Code Domain |
| :--- | :--- | :--- | :--- | :--- |
| **$B_z$** | Orthogonal Magnetic Flux Density | $\text{Tesla (T)}$ | The intensity of the permanent magnetic field applied perpendicular to both the fluid channel axis and the extraction electrodes. | `variables/node_amplifiers.py` |
| **$\mathbf{J}$** | Induced Current Density Field | $\text{A/m}^2$ | Vector field tracking the spatial distribution of electric current generated within the moving conductive fluid. | `variables/node_amplifiers.py` |
| **$\sigma$** | Bulk Electrical Conductivity | $\text{S/m}$ | Defines the intrinsic ability of the multi-component working fluid blend to conduct electrical charge carriers. | `variables/node_amplifiers.py` |
| **$E_x$** | Induced Electric Field Vector | $\text{V/m}$ | The resulting electrostatic field established across the channel width due to the Faraday ($\mathbf{v} \times \mathbf{B}$) separation of charges. | `variables/node_amplifiers.py` |
| **$V_{\text{emf}}$** | Open-Circuit Electromotive Force | $\text{Volts (V)}$ | Total voltage differential generated between extraction electrodes under steady-state fluid velocity profiles. | `variables/teg_sandwich.py` |
| **$P$** | Net Electrical Power Generation | $\text{Watts (W)}$ | Total rate of electrical energy extraction, scaling quadratically ($P = \frac{V^2}{R}$) with localized Halbach array flux peaks. | `variables/node_amplifiers.py` |

---

## 3. Second-Law Thermodynamics & Zeotropic Phase-Change Variables

These variables govern the secondary bottoming cycle designed to eliminate thermal degradation and maximize exergy recovery.

| Variable | Definition | SI Units | Core Mathematical Function / Context | Code Domain |
| :--- | :--- | :--- | :--- | :--- |
| **$T_{\text{bubble}}$** | Mixture Bubble Point Temperature | $\text{Kelvin (K)}$ | The temperature threshold where the first micro-bubble of vapor begins to form within the liquid phase blend at a given pressure. | `variables/zeotropic_mix.py` |
| **$T_{\text{dew}}$** | Mixture Dew Point Temperature | $\text{Kelvin (K)}$ | The temperature threshold where the first droplet of liquid begins to condense out of the vapor phase blend. | `variables/zeotropic_mix.py` |
| **$T_{\text{glide}}$** | Temperature Glide | $\text{Kelvin (K)}$ | The temperature delta ($T_{\text{dew}} - T_{\text{bubble}}$) engineered to parallel the temperature profile of the data center exhaust stream. | `variables/zeotropic_mix.py` |
| **$T_h$** | Hot Stream Source Temperature | $\text{Kelvin (K)}$ | The local temperature profile of the incoming data center exhaust air stream along the scavenger hood path. | `variables/variable_theory.py` |
| **$T_c$** | Cold Stream Sink Temperature | $\text{Kelvin (K)}$ | The local boiling temperature profile of the non-azeotropic refrigerant blend moving parallel to the exhaust. | `variables/variable_theory.py` |
| **$X_{\text{destruction}}$** | Exergy Destruction Rate | $\text{Watts (W)}$ | The rate of lost work potential caused by irreversible thermal gaps ($\Delta T$) across the heat exchange boundary layer. | `variables/variable_theory.py` |
| **$\eta_{\text{ex}}$** | Second-Law Exergy Efficiency | $\%$ | Measures how close the system approaches an ideal, reversible Carnot harvesting cycle across narrow differentials. | `variables/variable_theory.py` |

---

## 4. Gen III Ultra Boundary-Layer Nanotechnology Variables

These parameters model the microscopic surface modifications responsible for elevating the framework to its 80.4% maximum efficiency peak.

| Variable | Definition | SI Units | Core Mathematical Function / Context | Code Domain |
| :--- | :--- | :--- | :--- | :--- |
| **$b$** | Microscopic Hydrophobic Slip Length | $\text{Nanometers (nm)}$ | Extrapolation distance past the solid wall where the fluid velocity vector would theoretically hit zero under slip conditions. | `variables/node_amplifiers.py` |
| **$\tau_w$** | Boundary Viscous Shear Stress | $\text{Pascal (Pa)}$ | The drag force per unit area exerted by the fluid on the interior channel walls, minimized via Graphene Oxide nano-coatings. | `variables/node_amplifiers.py` |
| **$\left(\frac{\partial v}{\partial z}\right)_{\text{wall}}$** | Perpendicular Velocity Gradient | $\text{s}^{-1}$ | The spatial rate of change of fluid velocity moving outward from the conduit boundary toward the core center. | `variables/node_amplifiers.py` |

---
