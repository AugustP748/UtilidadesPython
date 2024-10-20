import pulp

# Datos de ejemplo
n = 3  # Número de cursos
m = 2  # Número de laboratorios
t = 4  # Número de franjas horarias

Num = [30, 25, 40]  # Número de estudiantes en cada curso
Cap = [35, 50]      # Capacidad de cada laboratorio
P = [[1, 1, 0, 0],  # Disponibilidad del profesor para cada curso en cada franja horaria
     [1, 1, 1, 0],
     [1, 0, 0, 1]]
Equip_C = [[1, 1, 1, 1],  # Equipamiento requerido por cada curso en cada franja horaria
           [1, 1, 1, 0],
           [1, 0, 0, 1]]
Equip_L = [[1, 1, 1, 1],  # Equipamiento disponible en cada laboratorio
           [1, 1, 1, 1]]

# Crear el problema de optimización
model = pulp.LpProblem("AsignacionLaboratorios", pulp.LpMaximize)

# Variables de decisión
x = pulp.LpVariable.dicts("x", (range(n), range(m), range(t)), cat='Binary')

# Función objetivo
model += pulp.lpSum(x[i][j][h] for i in range(n) for j in range(m) for h in range(t))

# Restricciones
# 1. Cada curso debe asignarse a un laboratorio en una franja horaria
for i in range(n):
    model += pulp.lpSum(x[i][j][h] for j in range(m) for h in range(t)) == 1

# 2. La capacidad del laboratorio debe ser suficiente para el número de estudiantes del curso
for i in range(n):
    for j in range(m):
        for h in range(t):
            model += x[i][j][h] * Num[i] <= Cap[j]

# 3. Un laboratorio puede ser utilizado por un solo curso en una franja horaria dada
for j in range(m):
    for h in range(t):
        model += pulp.lpSum(x[i][j][h] for i in range(n)) <= 1

# 4. Disponibilidad del profesor para cada curso
for i in range(n):
    for j in range(m):
        for h in range(t):
            model += x[i][j][h] <= P[i][h]

# 5. Requisitos de equipamiento del curso y del laboratorio
for i in range(n):
    for j in range(m):
        for h in range(t):
            model += x[i][j][h] * Equip_C[i][h] <= Equip_L[j][h]

# Resolver el modelo
model.solve()

# Imprimir resultados
for i in range(n):
    for j in range(m):
        for h in range(t):
            if pulp.value(x[i][j][h]) == 1:
                print(f"Curso {i} asignado al laboratorio {j} en la franja horaria {h}")
