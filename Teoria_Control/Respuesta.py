import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Definir el sistema, por ejemplo, un sistema de segundo orden
numerator = [1]
denominator = [1, 4, 1]  # Por ejemplo, un sistema de segundo orden: s^2 + s + 1

system = signal.TransferFunction(numerator, denominator)

# Generar la respuesta al escalón unitario
time, response = signal.step(system)

# Graficar la respuesta transitoria
plt.plot(time, response, label='Respuesta Transitoria')
plt.axhline(y=1, color='r', linestyle='--', label='Entrada = 1')  # Línea horizontal en y=1

plt.title('Respuesta Transitoria del Sistema')
plt.xlabel('Tiempo')
plt.ylabel('Respuesta')
plt.legend()
plt.grid(True)
plt.show()
