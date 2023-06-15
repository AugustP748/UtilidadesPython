from pulp import *

# Crear el problema de maximización
prob = LpProblem("Maximización de ingresos", LpMaximize)

# Definir las variables de decisión
A = LpVariable("A", 0, None, LpInteger)
B = LpVariable("B", 0, None, LpInteger)

# Definir la función objetivo
prob += 5*A + 6*B

# Definir las restricciones
prob += A + 2*B <= 80
prob += 2*A + B <= 100
prob += 3*A + B <= 120
prob += A >= 0
prob += B >= 0

# Resolver el modelo
prob.solve()

# Imprimir la solución
print("Cantidad de Productos A: ", value(A))
print("Cantidad de Productos B: ", value(B))
print("Ingreso total máximo:", value(prob.objective), "dólares")