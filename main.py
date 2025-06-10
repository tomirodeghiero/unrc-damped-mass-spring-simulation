import numpy as np
import subprocess
from simulation_methods import euler_method, heun_method, rk4_method, is_at_rest, load_parameters

# Load simulation parameters
params = load_parameters()
params['h'] = 0.0001           # Integration step size
params['t_max'] = 100.0        # Maximum simulation time (s)

# Run simulations using Euler, Heun, and RK4 methods
t_euler, x_euler, v_euler = euler_method(params)
t_heun, x_heun, v_heun = heun_method(params)
t_rk4, x_rk4, v_rk4 = rk4_method(params)

# Save simulation results to .dat files
np.savetxt("euler.dat", np.column_stack((t_euler, x_euler, v_euler)), header="t x v")
np.savetxt("heun.dat", np.column_stack((t_heun, x_heun, v_heun)), header="t x v")
np.savetxt("rk4.dat", np.column_stack((t_rk4, x_rk4, v_rk4)), header="t x v")

# Generate Gnuplot script for position vs time plot
with open("plot.gnuplot", "w") as f:
    f.write("""
set terminal png size 1000,600
set output 'comparison_methods.png'
set title 'Comparación de Métodos Numéricos'
set xlabel 'Tiempo (s)'
set ylabel 'Posición (m)'
set grid
plot 'euler.dat' using 1:2 with lines title 'Euler', \
     'heun.dat' using 1:2 with lines title 'Heun', \
     'rk4.dat' using 1:2 with lines title 'RK4'
""")

# Generate Gnuplot script for phase diagram (velocity vs position)
with open("fase.gnuplot", "w") as f:
    f.write("""
set terminal png size 1000,600
set output 'phase_diagram.png'
set title 'Diagrama de Fase: Velocidad vs Posición'
set xlabel 'Posición (m)'
set ylabel 'Velocidad (m/s)'
set grid
plot 'euler.dat' using 2:3 with lines title 'Euler', \
     'heun.dat' using 2:3 with lines title 'Heun', \
     'rk4.dat' using 2:3 with lines title 'RK4'
""")

# Run Gnuplot to generate the PNG images
subprocess.run(["gnuplot", "plot.gnuplot"])
subprocess.run(["gnuplot", "fase.gnuplot"])

# Exploration: Vary the damping parameter b
b_values = [10, 5, 1]
for b in b_values:
    params_varied = params.copy()
    params_varied['b'] = b
    
    t_euler_varied, x_euler_varied, v_euler_varied = euler_method(params_varied)
    
    filename = f"euler_b{b}.dat"
    np.savetxt(filename, np.column_stack((t_euler_varied, x_euler_varied, v_euler_varied)), header="t x v")

# Generate Gnuplot script for comparison of different b values
with open("plot_varied_b.gnuplot", "w") as f:
    f.write("""
set terminal png size 1000,600
set output 'comparison_b_values.png'
set title 'Comparación con diferentes valores de b'
set xlabel 'Tiempo (s)'
set ylabel 'Posición (m)'
set grid
""")
    # Dynamically add plot commands for each b value
    plot_commands = "plot "
    for b in b_values:
        plot_commands += f"'euler_b{b}.dat' using 1:2 with lines title 'b = {b}', "
    plot_commands = plot_commands[:-2]
    f.write(plot_commands)

# Run Gnuplot to generate the varied b comparison
subprocess.run(["gnuplot", "plot_varied_b.gnuplot"])

# Generate Gnuplot script for velocity vs time
with open("velocity_plot.gnuplot", "w") as f:
    f.write("""
set terminal png size 1000,600
set output 'velocity_over_time.png'
set title 'Velocidad vs Tiempo'
set xlabel 'Tiempo (s)'
set ylabel 'Velocidad (m/s)'
set grid
plot 'euler.dat' using 1:3 with lines title 'Euler', \
     'heun.dat' using 1:3 with lines title 'Heun', \
     'rk4.dat' using 1:3 with lines title 'RK4'
""")
subprocess.run(["gnuplot", "velocity_plot.gnuplot"])

if is_at_rest(x_rk4, v_rk4):
    print("El sistema alcanzó el reposo estable.")
else:
    print("El sistema no alcanzó el reposo estable en el tiempo simulado.")
