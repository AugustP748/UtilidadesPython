import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import ipywidgets as widgets
from ipywidgets import interactive

# Función para graficar la respuesta transitoria con una ganancia dada
def plot_transient_response(gain):
    # Sistema de ejemplo (puedes ajustar los coeficientes según tu sistema)
    numerator = [gain]
    denominator = [1, 1, 1]

    system = signal.TransferFunction(numerator, denominator)

    # Generar la respuesta al escalón unitario
    time, response = signal.step(system)

    # Graficar la respuesta transitoria
    plt.plot(time, response)
    plt.title('Respuesta Transitoria del Sistema')
    plt.xlabel('Tiempo')
    plt.ylabel('Respuesta')
    plt.grid(True)
    plt.show()

# Crear un slider interactivo para la ganancia
gain_slider = widgets.FloatSlider(value=1.0, min=0.1, max=10.0, step=0.1, description='Ganancia')

# Crear la interfaz interactiva
interactive_plot = interactive(plot_transient_response, gain=gain_slider)

# Mostrar la interfaz
output = interactive_plot.children[-1]
output.layout.height = '350px'
interactive_plot
