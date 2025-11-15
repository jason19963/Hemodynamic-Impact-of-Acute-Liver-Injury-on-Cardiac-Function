# Hemodynamic-Impact-of-Acute-Liver-Injury-on-Cardiac-Function


## Overview
This repository contains simulation files generated using the open-source hemodynamics software **CRIMSON** in 0D mode.(https://crimson.software/). These files represent the baseline simulations used in the study. By adjusting the parameters within these files, users can create personalized or customized simulation scenarios.

---

## Files and Description

| File | Description |
|------|-------------|
| `elastanceControl.py` | Time-varying elastance control file for the **left ventricle**. Internal parameters can be adjusted. |
| `elastanceControlRight.py` | Time-varying elastance control file for the **right ventricle**. Internal parameters can be adjusted. |
| `netlist_surfaces.xml` | Contains the **circuit structure** information. Parameters can be modified. |
| `netlist_closed_loop_downstream.xml` | Circuit connection for **closed-loop simulation**. |
| `solver.inp` | Contains solver settings such as **time step and simulation duration**. |
| `faceInfo.dat` | Configuration file. |
| `geombc.dat.1` | Configuration file. |
| `multidomain.dat` | Configuration file. |
| `numstart.dat` | Configuration file. |
| `restart.0.1` | Configuration file. |

> **Note:** All files can be directly loaded and run in CRIMSON 0D mode.

---

## Requirements
- **CRIMSON software**  
  [Download and installation instructions](https://crimson.software/)  

---

## Set up the simulation in CRIMSON

1. **Open CRIMSON.**

2. **Load the files `0D_closed_loop`**  

---

## Modify parameters if needed

- For cardiac elastance control:  
  - `elastanceControl.py` → left heart  
  - `elastanceControlRight.py` → right heart
  - `netlist_surfaces.xml` → whole body parameters 

- Adjust relevant parameters according to your simulation needs.

---

## Run the simulation

Use CRIMSON’s 0D solver interface to execute the simulation. Output data will be generated.For more details, please refer to the CRIMSON website.

---

## Post-processing

- Visualization and analysis can be done using MATLAB, etc.

---

## Notes

- All files are intended for research purposes only.  
- Ensure CRIMSON is properly installed and environment paths are correctly set.  
- Modifying parameters without understanding their physiological meaning may lead to non-physiological results.

---

## References

- **CRIMSON software:** [https://crimson.software/](https://crimson.software/)
