from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpStatus

# Supongamos que tenemos los siguientes datos:
# Clases
clases = ['Clase1', 'Clase2', 'Clase3']
# Aulas
aulas = ['Aula1', 'Aula2']
# Periodos (por ejemplo, 4 periodos en un día)
periodos = ['P1', 'P2', 'P3', 'P4']
# Capacidad de aulas
capacidades = {'Aula1': 30, 'Aula2': 25}
# Número de estudiantes por clase
num_estudiantes = {'Clase1': 20, 'Clase2': 25, 'Clase3': 30}
# Disponibilidad de aulas (para simplificación, asumimos que todas están disponibles en todos los periodos)
disponibilidad_aulas = {('Aula1', 'P1'): 1, ('Aula1', 'P2'): 1, ('Aula1', 'P3'): 1, ('Aula1', 'P4'): 1,
                        ('Aula2', 'P1'): 1, ('Aula2', 'P2'): 1, ('Aula2', 'P3'): 1, ('Aula2', 'P4'): 1}

# Definición del problema
problema = LpProblem("Asignacion_de_Aulas", LpMinimize)

# Definición de las variables
x = LpVariable.dicts("x", [(c, a, t) for c in clases for a in aulas for t in periodos], cat='Binary')

# Función objetivo (minimizar el total de variables binarias activas, es decir, asignaciones)
problema += lpSum(x[c, a, t] for c in clases for a in aulas for t in periodos)

# Restricciones
# Cada clase debe ser asignada a exactamente un aula en un único periodo
for c in clases:
    problema += lpSum(x[c, a, t] for a in aulas for t in periodos) == 1

# Cada aula solo puede tener una clase asignada en cada periodo
for a in aulas:
    for t in periodos:
        problema += lpSum(x[c, a, t] for c in clases) <= 1

# Las clases deben asignarse a aulas que puedan acomodar a todos los estudiantes
for c in clases:
    for a in aulas:
        for t in periodos:
            problema += x[c, a, t] * num_estudiantes[c] <= capacidades[a]

# Considerar la disponibilidad de las aulas (si aplica)
for (a, t), disponible in disponibilidad_aulas.items():
    if not disponible:
        for c in clases:
            problema += x[c, a, t] == 0

# Resolución del problema
problema.solve()

# Imprimir el estado del problema
print("Estado del problema:", LpStatus[problema.status])

# Imprimir resultados
for c in clases:
    for a in aulas:
        for t in periodos:
            if x[c, a, t].varValue == 1:
                print(f"{c} asignada al {a} en el periodo {t}")
