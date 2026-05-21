# CHTS Maintenance & Troubleshooting Guide

This manual outlines standard preventative care 
and diagnostics for the Cascading Hybrid 
Thermal Scavenger system.

---

## 1. Preventative Maintenance Schedule

To guarantee peak thermal recovery and zero 
fluid leakage, follow this vertical checklist:

### Monthly Inspections
* Check Viton gaskets along the MHD core channel 
  walls for any signs of physical wear.
* Verify electrode mounting bolts are tight 
  and flush with the channel housing.
* Check the 50.0 mL expansion reservoir fluid 
  level to ensure no active driver fluid has 
  vaporized out of the loop.

### Bi-Annual Inspections
* Inspect the flush copper electrode faces 
  for surface oxidation or micro-pitting.
* Clean the Stage 2 micro-channel heat exchanger 
  fins using low-pressure compressed air to 
  remove any settled data center dust.
* Test N52 neodymium magnet placement slots 
  for structural housing warping caused by 
  continuous server exhaust heat exposure.

---

## 2. Dynamic Troubleshooting Matrix

Use this guide to diagnose system drops or 
unexpected readings.

### Issue A: Low or Zero Voltage Output
* **Potential Cause 1:** Fluid velocity has 
  dropped below the sonic threshold at the 
  1.5 mm nozzle throat.
  * *Fix:* Check server rack exhaust fans; 
    ensure inlet temperature is reaching the 
    target 40°C to 60°C range to force fluid 
    phase-change expansion.
* **Potential Cause 2:** Internal electrode 
  fouling or oxidation layer buildup.
  * *Fix:* Isolate the channel, drain the 
    25.0 mL fluid charge, and lightly buff the 
    copper plates back to a bright shine.

### Issue B: Fluid Loop Over-Pressurization
* **Potential Cause 1:** The 50.0 mL expansion 
  reservoir is overfilled, leaving no volume 
  for vapor expansion.
  * *Fix:* Bleed the primary fluid loop back down 
    to the baseline static charge of 25.0 mL.
* **Potential Cause 2:** High static back-pressure 
  from the external exhaust hood frame.
  * *Fix:* Inspect the exhaust plenum frame for 
    airflow blockages or restrictions.

### Issue C: Home Assistant Sensor Drops
* **Potential Cause 1:** Microcontroller has 
  disconnected from the local MQTT highway.
  * *Fix:* Power-cycle the local sensor board 
    and verify the network configuration matches 
    your `home_assistant_sensors.yaml` file.
