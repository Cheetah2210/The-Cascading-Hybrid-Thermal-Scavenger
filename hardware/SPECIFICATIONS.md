# FILE: hardware/SPECIFICATIONS.md
# EHD Phase-Boundary Conduit Module Specifications

This document outlines the physical, mechanical, and electrical specifications for the external, facility-side Electro-Hydrodynamic (EHD) containment shield modules used in Generation III of the Cascading Hybrid Thermal Scavenger ecosystem. This file works in direct tandem with the core simulation parameters defined in `variables/variable_theory_3.py`.

---

## 🔩 1. Core Structural Dimensions & Substrate Selection

The physical enclosure is designed to maintain structural integrity under high system pressures while completely isolating high-voltage ionization fields from the facility piping.

| Specification Parameter | Target Value | Engineering Justification |
| :--- | :--- | :--- |
| **Inner Conduit Diameter** | 2.0 inches (50.8 mm) | Matches standard enterprise secondary liquid loop sizing to eliminate flow restriction. |
| **Wall Thickness** | 0.25 inches (6.35 mm) | Provides a safety buffer for operating pressures up to 300 PSI. |
| **Primary Core Material** | **Borosilicate Glass 3.3** or **PTFE** | High dielectric strength (>20 kV/mm) to prevent electrical arcing to the chassis. |
| **Outer RF/EMC Shielding** | 6061-T6 Aluminum Mesh Jacket | Grounded Faraday cage to block electromagnetic interference (EMI) from leaking. |
|
|  ​Internal Surface Treatment: Atomically Smooth Graphene Oxide (GO) Nano-Coating applied to the inner diameter of the Borosilicate core to establish a hydrophobic slip boundary condition, minimizing viscous shear stress and maximizing fluid kinetic retention. |
---

## ⚡ 2. Electrode Geometry & Grid Configuration

The EHD effect relies on a non-uniform electric field to polarize and violently accelerate dielectric zeotropic fluid molecules away from the pipe walls, stripping away insulating vapor bubbles.

### Emitter Ring (High-Voltage Electrode)
* **Material:** Ultra-pure **Platinum-Plated Titanium** (prevents galvanic corrosion over decades of continuous operation).
* **Geometry:** Sharp, hyper-thin internal ring edge (0.1 mm radius) protruding slightly into the inner diameter of the conduit to concentrate field lines and maximize local charge injection.
* **Placement:** Positioned exactly at the liquid inlet boundary of the evaporation stage.

### Collector Ring (Grounded Reference)
* **Material:** 316L Stainless Steel.
* **Geometry:** Smooth, flush-mounted cylindrical sleeve embedded into the inner wall of the pipe.
* **Axial Spacing:** Spaced exactly **15.0 mm downstream** from the sharp emitter ring to create an optimized asymmetric field gradient without inducing total dielectric breakdown.

---

## 🔌 3. Electrical Insulation & Power Supply Parameters

To maintain high-velocity phase enhancement without creating a high-power parasitic draw, the system operates on high voltage but incredibly low current (micro-amperes).

* **Peak Operational Voltage:** $12.5\text{ kV DC}$ (Adjustable from $8\text{ kV}$ to $15\text{ kV}$ based on real-time fluid velocity).
* **Current Draw:** Capped at a maximum of **350 micro-amps ($\mu\text{A}$)** per node module.
* **Total Module Power Consumption:** $P = V \times I = 12,500\text{ V} \times 0.000350\text{ A} = 4.375\text{ Watts}$.

---

## 🔒 4. Safety & Fluid Containment Safeguards

Because our optimized fluid cascade utilizes highly efficient working fluids, absolute containment isolation is engineered directly into the hardware spec:

1. **Dual-Wall Vacuum Hermetic Seals:** The inner dielectric fluid tube is housed within a secondary outer vacuum chamber sleeve ($10^{-4}\text{ Torr}$), acting as both a perfect thermal insulator and an absolute secondary containment barrier.
2. **Dielectric Isolation Flanges:** The ends of the EHD module interface with standard facility stainless steel piping using heavy-duty, non-conductive PEEK (Polyetheretherketone) isolation flanges to prevent high-voltage potentials from traveling down the building's metal framework.
3. **Automated Interlock Shutdown:** Integrated optical bubble sensors monitor the flow. If fluid pressure drops below 40 PSI or a sudden spike in current is detected (indicating micro-arcing), an automated physical relay cuts the high-voltage power supply within **8 milliseconds**.

---

## 🔄 5. Enterprise Topology, Redundancy & Hot-Swapping

To ensure 99.999% facility uptime, the EHD containment modules must never act as a single point of failure for the primary cooling loop. The physical deployment requires a parallel-path manifold topology.

### N+1 Parallel Manifold Configuration
* **System Layout:** Instead of a single inline pipe, the fluid stream is split across an $N+1$ manifold array of smaller, parallel EHD conduit modules (where $N$ satisfies the maximum thermal load volumetric flow rate, and $+1$ acts as an active standby unit).
* **Isolation Valve Assemblies:** Each individual EHD module is bookended by automated, high-pressure motorized ball valves. 

### Zero-Downtime Hot-Swapping Maintenance
1. **Pneumatic Isolation:** If an internal optical bubble sensor or micro-amp current monitor flags a cleaning interval or electrode degradation inside an individual module, the central PLC controller triggers the isolation valves for that specific runner.
2. **Diverted Flow:** The volumetric flow is instantly distributed across the remaining active modules and the $+1$ standby runner.
3. **Physical Serviceability:** The isolated module can be safely unbolted from its PEEK flanges, cleaned or swapped out, and re-installed without a single drop in compute cluster performance or server room temperature fluctuations.

---
*An open-hardware sustainability initiative by Cheetahs Creations.*
*Governed under file reference: hardware/SPECIFICATIONS.md*
