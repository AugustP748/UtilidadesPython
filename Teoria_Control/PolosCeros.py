import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Definir el sistema, por ejemplo, un sistema de segundo orden
numerator = [1]
denominator = [1, 1, 1]  # Por ejemplo, un sistema de segundo orden: s^2 + s + 1

# Obtener polos y ceros del sistema
zeros, poles, _ = signal.tf2zpk(numerator, denominator)

# Graficar polos y ceros
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Ceros')
plt.scatter(np.real(poles), np.imag(poles), marker='^', color='r', label='Polos', s=100)  # Triángulos para polos

# Resaltar ejes de coordenadas
plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=0, color='black', linewidth=1)

plt.title('Diagrama de Polos y Ceros')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginaria')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
