# import numpy as np
import matplotlib.pyplot as plt
import numpy as np
# programa de Control Estadístico de Procesos (CEP) 

# Datos de ejemplo (puedes reemplazarlos con tus propios datos)
datos = [15, 17, 18, 16, 20, 19, 22, 16, 21, 18]

# Cálculo de estadísticas básicas
media = np.mean(datos)
desviacion_estandar = np.std(datos)

# Gráfico de control: gráfico de línea central y límites de control
linea_central = [media] * len(datos)
limite_superior = [media + 3 * desviacion_estandar] * len(datos)
limite_inferior = [media - 3 * desviacion_estandar] * len(datos)

# Gráfico de datos y límites de control
plt.plot(datos, marker='o', linestyle='-', color='b')
plt.plot(linea_central, linestyle='--', color='r', label='Línea Central')
plt.plot(limite_superior, linestyle='--', color='g', label='Límite Superior')
plt.plot(limite_inferior, linestyle='--', color='g', label='Límite Inferior')

plt.title('Gráfico de Control')
plt.xlabel('Muestras')
plt.ylabel('Valor')
plt.legend()
plt.show()
