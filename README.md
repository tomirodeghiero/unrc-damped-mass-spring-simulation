# Damped Mass–Spring System Simulation

&#x20;

## Description

This program simulates the vertical motion of a mass attached to a spring with linear damping and a stiff elastic stop. You can view between the **Euler**, **Heun**, and **Runge-Kutta 4** methods. The simulation results are saved as `.dat` files and plotted using **Gnuplot**.

Four plots are generated using Gnuplot:

- `comparison_methods.png`: Position x(t) vs Time plot comparing the Euler, Heun, and RK4 methods.
- `phase_diagram.png`: Phase diagram showing velocity v(t) vs position x(t).
- `velocity_over_time.png`: Velocity v(t) vs Time plot for the three numerical methods.
- `comparison_b_values.png`: Comparison of position evolution for different values of the damping coefficient b.

---

## Dependencies

- **Python 3** (version 3.7 or higher)
- **Gnuplot** (version 5.0 or higher)

> Make sure both are installed and available in your system PATH.

---

## Project Structure

```
.
├── main.py                # Entry point of the simulation
├── simulation_methods.py  # Numerical methods and acceleration model
├── parameters.txt         # Editable physical and simulation parameters
```

---

## Simulation Parameters

All parameters live in `parameters.txt`. Available settings:

| Parameter | Description                       | Default Value |     |     |     |       |
| --------- | --------------------------------- | ------------- | --- | --- | --- | ----- |
| `m`       | Mass of the body (kg)             | 1.0           |     |     |     |       |
| `b`       | Damping coefficient (N·s/m)       | 10.0          |     |     |     |       |
| `b_a`     | Damping when compressed (N·s/m)   | 0.1           |     |     |     |       |
| `k`       | Linear spring constant (N/m)      | 20.0          |     |     |     |       |
| `k_e`     | Elastic‐stop stiffness (N/m)      | 50000.0       |     |     |     |       |
| `g`       | Gravitational acceleration (m/s²) | 9.81          |     |     |     |       |
| `x0`      | Initial displacement (m)          | 2.0           |     |     |     |       |
| `v0`      | Initial velocity (m/s)            | 0.0           |     |     |     |       |
| `h`       | Time step (s)                     | 0.0001        |     |     |     |       |
| `t_max`   | Maximum simulation time (s)       | 100.0         |     |     |     |       |
| `tol`     | Convergence tolerance for         | v             | and | x   |     | 0.001 |

---

## Usage

From the project root, follow these steps:

1. First, make sure to install the required Python libraries:

```bash
pip install -r requirements.txt
```

2. Then, run the main script:

```bash
python3 main.py
```

After the simulation finishes, the following output files will be generated:

- `euler.dat`, `heun.dat`, `rk4.dat` – simulation results for each method
- `comparison_methods.png` – position vs time plot
- `phase_diagram.png` – phase diagram (velocity vs position)

---

## Authors

Developed by **Lingua Matías** and **Tomás Rodeghiero**, students of the B.Sc. in Computer Science program at the National University of Río Cuarto (UNRC), for the **Simulation** course.
