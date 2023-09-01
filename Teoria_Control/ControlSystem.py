import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Función que representa la dinámica del sistema de nivel de agua en el tanque
def tank_system(y, t, u):
    Kp = 2.0  # Ganancia proporcional
    Ki = 1.0  # Ganancia integral
    Kd = 0.1  # Ganancia derivativa

    e = u - y[0]  # Error
    if not hasattr(tank_system, 'last_error'):
        tank_system.last_error = 0.0
    integral = tank_system.last_error + e  # Integral acumulada
    derivative = e - tank_system.last_error  # Derivada

    u = Kp * e + Ki * integral + Kd * derivative

    dydt = -y[0] + u  # Modelo del sistema

    tank_system.last_error = e  # Almacenar el error para la siguiente iteración

    return dydt

# Tiempo de simulación
t = np.linspace(0, 20, 1000)

# Entrada (setpoint) del sistema
u = np.zeros(len(t))
u[100:] = 10.0  # Cambio en el setpoint a t=10

# Condición inicial
y0 = [0.0]

# Simulación del sistema
y = odeint(tank_system, y0, t, args=(u,))

# Visualización de los resultados
plt.figure()
plt.plot(t, u, 'r--', linewidth=2, label='Setpoint (u)')
plt.plot(t, y[:, 0], 'b', linewidth=2, label='Nivel de Agua (y)')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()
plt.grid()
plt.show()
