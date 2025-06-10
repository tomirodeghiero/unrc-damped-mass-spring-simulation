import numpy as np

# Load simulation parameters from a text file
def load_parameters(filename='parameters.txt'):
    parameters = {}
    with open(filename) as file:
        for line in file:
            if '=' in line and not line.strip().startswith('#'):
                key, value = line.split('=')
                parameters[key.strip()] = float(value.split('#')[0].strip())
    return parameters

# Compute the acceleration of the system at a given position and velocity
def acceleration(position, velocity, params):
    if position > 0:
        # Regular spring and damping force
        return (-params['b'] * velocity - params['k'] * position) / params['m'] - params['g']
    else:
        # Elastic stopper and alternative damping force
        return (-params['ba'] * velocity - params['ke'] * position) / params['m'] - params['g']

# Euler integration method
def euler_method(params):
    t, x, v = [0.0], [params['x0']], [params['v0']]

    while t[-1] < params['t_max'] and (abs(v[-1]) >= 0.001 or abs(x[-1]) >= 0.001):
        a = acceleration(x[-1], v[-1], params)
        v_new = v[-1] + params['h'] * a
        x_new = x[-1] + params['h'] * v[-1]

        t.append(t[-1] + params['h'])
        x.append(x_new)
        v.append(v_new)

    return np.array(t), np.array(x), np.array(v)

# Heun's method (improved Euler)
def heun_method(params):
    t, x, v = [0.0], [params['x0']], [params['v0']]

    while t[-1] < params['t_max'] and (abs(v[-1]) >= 0.001 or abs(x[-1]) >= 0.001):
        a1 = acceleration(x[-1], v[-1], params)

        # Predictor step
        x_predict = x[-1] + params['h'] * v[-1]
        v_predict = v[-1] + params['h'] * a1

        # Corrector step
        a2 = acceleration(x_predict, v_predict, params)
        x_new = x[-1] + params['h'] * 0.5 * (v[-1] + v_predict)
        v_new = v[-1] + params['h'] * 0.5 * (a1 + a2)

        t.append(t[-1] + params['h'])
        x.append(x_new)
        v.append(v_new)

    return np.array(t), np.array(x), np.array(v)

# Runge-Kutta 4th order method
def rk4_method(params):
    t, x, v = [0.0], [params['x0']], [params['v0']]
    h = params['h']

    while t[-1] < params['t_max'] and (abs(v[-1]) >= 0.001 or abs(x[-1]) >= 0.001):
        x_n, v_n = x[-1], v[-1]

        # Derivatives
        dxdt = lambda v: v
        dvdt = lambda x, v: acceleration(x, v, params)

        # RK4 intermediate steps
        k1x = h * dxdt(v_n)
        k1v = h * dvdt(x_n, v_n)

        k2x = h * dxdt(v_n + 0.5 * k1v)
        k2v = h * dvdt(x_n + 0.5 * k1x, v_n + 0.5 * k1v)

        k3x = h * dxdt(v_n + 0.5 * k2v)
        k3v = h * dvdt(x_n + 0.5 * k2x, v_n + 0.5 * k2v)

        k4x = h * dxdt(v_n + k3v)
        k4v = h * dvdt(x_n + k3x, v_n + k3v)

        # Update position and velocity
        x_new = x_n + (1/6) * (k1x + 2 * k2x + 2 * k3x + k4x)
        v_new = v_n + (1/6) * (k1v + 2 * k2v + 2 * k3v + k4v)

        t.append(t[-1] + h)
        x.append(x_new)
        v.append(v_new)

    return np.array(t), np.array(x), np.array(v)

# Check for final rest condition (RK4 preferred for precision)
def is_at_rest(x, v):
    return abs(x[-1]) < 0.001 and abs(v[-1]) < 0.001