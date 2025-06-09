import numpy as np
import subprocess
from simulation_methods import load_parameters, euler_method, heun_method, rk4_method

# Load simulation parameters
params = load_parameters()
params['h'] = 0.0001           # Integration step size
params['t_max'] = 100.0        # Maximum simulation time (s)

# Run simulations using Euler, Heun, and RK4 methods
t_euler, x_euler, v_euler = euler_method(params)
t_heun,  x_heun,  v_heun  = heun_method(params)
t_rk4,   x_rk4,   v_rk4   = rk4_method(params)

# Save simulation results to .dat files
np.savetxt("euler.dat", np.column_stack((t_euler, x_euler, v_euler)), header="t x v")
np.savetxt("heun.dat",  np.column_stack((t_heun,  x_heun,  v_heun)),  header="t x v")
np.savetxt("rk4.dat",   np.column_stack((t_rk4,   x_rk4,   v_rk4)),   header="t x v")

# Generate Gnuplot script for position vs time plot
with open("plot.gnuplot", "w") as f:
    f.write("""
set terminal png size 1000,600
set output 'comparacion_metodos.png'
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
set output 'diagrama_fase.png'
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
