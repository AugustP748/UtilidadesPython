import networkx as nx

def calcular_pert_cpm(actividades, precedencias):
    # Crear el gráfico dirigido
    G = nx.DiGraph()

    # Agregar las actividades como nodos
    for actividad in actividades:
        G.add_node(actividad)

    # Agregar las precedencias como arcos
    for precedencia in precedencias:
        actividad_antecesora, actividad_sucesora, duracion = precedencia
        G.add_edge(actividad_antecesora, actividad_sucesora, weight=duracion)

    # Calcular las fechas tempranas (TE) sin considerar las dependencias
    te = {}
    for actividad in actividades:
        te[actividad] = 0

    # Calcular las fechas tempranas (TE) considerando las dependencias
    for actividad in nx.topological_sort(G):
        if len(G[actividad]) > 0:
            te[actividad] = max(te[antecesora] + G[antecesora][actividad]['weight'] for antecesora in G[actividad])

    # Calcular las fechas tardías (TT) utilizando CPM
    tt = {}
    for actividad in nx.topological_sort(G)[::-1]:
        if len(G[actividad]) == 0:
            tt[actividad] = te[actividad]
        else:
            tt[actividad] = min(tt[sucesora] - G[actividad][sucesora]['weight'] for sucesora in G[actividad])

    # Calcular el camino crítico
    camino_critico = [actividad for actividad in G if te[actividad] == tt[actividad]]

    return te, tt, camino_critico

# Ejemplo de uso
actividades = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
precedencias = [('A', 'B', 5),
                ('A', 'C', 3),
                ('B', 'D', 2),
                ('C', 'D', 2),
                ('C', 'E', 4),
                ('D', 'F', 7),
                ('E', 'F', 4),
                ('D', 'G', 4),
                ('F', 'H', 2),
                ('G', 'H', 1)]

te, tt, camino_critico = calcular_pert_cpm(actividades, precedencias)

print("Fechas tempranas (TE):", te)
print("Fechas tardías (TT):", tt)
print("Camino crítico:", camino_critico)
