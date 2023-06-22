import networkx as nx
import matplotlib.pyplot as plt

# Crear un nuevo grafo dirigido
G = nx.DiGraph()

# Agregar nodos al grafo
G.add_node("Actividad 1")
G.add_node("Actividad 2")
G.add_node("Actividad 3")
G.add_node("Actividad 4")
G.add_node("Actividad 5")

# Agregar arcos (actividades y sus dependencias)
G.add_edge("Actividad 1", "Actividad 2")
G.add_edge("Actividad 1", "Actividad 3")
G.add_edge("Actividad 2", "Actividad 4")
G.add_edge("Actividad 3", "Actividad 4")
G.add_edge("Actividad 4", "Actividad 5")

# Establecer duración estimada para cada actividad
duracion = {
    "Actividad 1": 10,
    "Actividad 2": 25,
    "Actividad 3": 15,
    "Actividad 4": 10,
    "Actividad 5": 5
}

# Agregar atributos de duración a los nodos del grafo
nx.set_node_attributes(G, duracion, "duracion")

# Calcular la ruta crítica utilizando el algoritmo PERT
ruta_critica = nx.algorithms.dag.dag_longest_path(G, weight="duracion")

# Imprimir la ruta crítica
print("Ruta crítica:")
print(ruta_critica)

# Graficar el grafo
nx.draw(G, with_labels=True, node_size=500, node_color="lightblue", font_weight="bold")

# Mostrar el gráfico
plt.show()  