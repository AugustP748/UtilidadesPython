import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Datos de ejemplo
#punto 3
#X = np.array([[100], [150], [200], [250], [300], [350]])
#y = np.array([10,20,25,40,45,55])

X = np.array([[2], [4], [6], [8], [10], [12], [14], [16]])
y = np.array([5,9,12,15,16,18,20,22])

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X, y)

# Hacer predicciones
predicciones = modelo.predict(X)

# Graficar los datos y la línea de regresión
plt.scatter(X, y, color='blue', label='Datos reales')
#plt.scatter(350, 55, color='green', label='Prodicción ventas')
#plt.scatter(12000, 13684, color='green', label='Prodicción ventas')
plt.plot(X, predicciones, color='red', label='Regresión lineal')
#plt.xlabel('Clics')
plt.xlabel('Gastos en publicidad')
plt.ylabel('Ventas')
plt.title('Regresión Lineal')
plt.legend()
#plt.text(350, 55, 'Predicción (350, 55)', fontsize=10, ha='right', color='green')
#plt.text(12000, 13684, 'Predicción (12000, 13684)', fontsize=10, ha='right', color='green')
plt.grid(True)
plt.show()
