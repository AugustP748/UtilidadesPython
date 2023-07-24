import numpy as np
import matplotlib.pyplot as plt

# Distancias entre ciudades (matriz de adyacencia)
distancias = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

def calcular_distancia_ruta(ruta):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += distancias[ruta[i]][ruta[i+1]]
    distancia_total += distancias[ruta[-1]][ruta[0]]  # Volver al punto de partida
    return distancia_total

def busqueda_tabu(num_iteraciones, tam_tabu, ruta_inicial):
    mejor_ruta = ruta_inicial
    mejor_distancia = calcular_distancia_ruta(mejor_ruta)

    tam_ciudades = len(ruta_inicial)
    tabu_list = []
    
    for _ in range(num_iteraciones):
        mejor_vecino = None
        mejor_distancia_vecino = float('inf')

        for i in range(tam_ciudades - 1):
            for j in range(i + 1, tam_ciudades):
                vecino = mejor_ruta.copy()
                vecino[i], vecino[j] = vecino[j], vecino[i]

                distancia_vecino = calcular_distancia_ruta(vecino)

                if distancia_vecino < mejor_distancia_vecino and vecino not in tabu_list:
                    mejor_vecino = vecino
                    mejor_distancia_vecino = distancia_vecino

        tabu_list.append(mejor_ruta)
        if len(tabu_list) > tam_tabu:
            tabu_list.pop(0)

        if mejor_distancia_vecino < mejor_distancia:
            mejor_ruta = mejor_vecino
            mejor_distancia = mejor_distancia_vecino

    return mejor_ruta, mejor_distancia

# Puntos de partida y ruta inicial
ciudades = [0, 1, 2, 3]  # Índices de las ciudades
ruta_inicial = [0, 1, 2, 3]  # Ruta inicial (empezando y terminando en la ciudad 0)

# Parámetros del algoritmo
num_iteraciones = 100
tam_tabu = 10

# Ejecutar búsqueda tabú
mejor_ruta, mejor_distancia = busqueda_tabu(num_iteraciones, tam_tabu, ruta_inicial)

# Imprimir resultado
print("Mejor ruta encontrada:", mejor_ruta)
print("Distancia total de la mejor ruta:", mejor_distancia)

# Gráfico de la ruta
x = [ciudades[i] for i in mejor_ruta]
y = [ciudades[i] for i in mejor_ruta]
x.append(x[0])
y.append(y[0])
plt.plot(x, y, 'ro-')
plt.xlabel('Ciudades')
plt.ylabel('Ciudades')
plt.title('Mejor ruta encontrada')
plt.show()
