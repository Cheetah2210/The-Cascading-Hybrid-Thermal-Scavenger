# CHTS Fail-Safe & Airflow Security Framework

This document outlines the passive safety 
mechanisms engineered into the CHTS to guarantee 
zero operational risk to host server hardware.

---

## 1. Passive Airflow Isolation

The primary rule of data center thermal management 
is preventing static back-pressure. If air cannot 
escape the back of a server rack, the internal 
components will rapidly overheat.

* **The Expanding Plenum Design:** The external 
  scavenger exhaust hood features a geometric 
  expansion zone. This guarantees that even if 
  the solid-state core is completely blocked, 
  exhaust air can passively divert.
  
* **Natural Convection Bypass:** In a total 
  system shutdown scenario, the physical chassis 
  utilizes weighted gravity-flap dampers. If 
  internal pressure rises by even 2 Pascals, the 
  flaps drop open passively, venting 100% of the 
  exhaust air directly into the room exactly like a 
  standard un-retrofitted server rack.

---

## 2. Zero-Uptime Leak Containment

Traditional liquid cooling loops introduce fluid 
directly inside the server chassis, running risk 
inches away from live motherboards.

* **100% External Architecture:** The CHTS mounts 
  entirely to the exterior exhaust frame of the 
  42U/48U cabinet. No fluid lines ever cross 
  the threshold of the server chassis.
  
* **Isolated Drip Core:** The 25.0 mL primary 
  MHD channel is housed inside a sealed, non-conductive 
  polycarbonate catch tray. In the highly unlikely 
  event of a Viton gasket failure, gravity pulls 
  the immiscible fluid down into the tray and away 
  from the rack intake, triggering a local Home 
  Assistant sensor alert without disrupting server 
  operations.

---

## 3. Maintenance Without Downtime

Data centers operate on a 99.999% uptime rule. 
They cannot shut down active servers to perform 
maintenance on an auxiliary thermal scavenger.

Because the system is fully decoupled:
* The N52 magnet blocks can be slid out of their 
  exterior housing channels seamlessly.
* The flush copper electrodes can be electrically 
  isolated via the power management board.
* The secondary Stage 2 refrigerant loop can be 
  drained or serviced while the servers continue 
  to process active computing workloads at full 
  capacity.
