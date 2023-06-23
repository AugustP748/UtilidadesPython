from pulp import *

# Crear el problema de maximización
prob = LpProblem("Maximización de ingresos", LpMaximize)

# Definir las variables de decisión
x1 = LpVariable("x1", 0, None, LpInteger)
x2 = LpVariable("x2", 0, None, LpInteger)

# Definir la función objetivo
prob += 100*x1 + 30*x2

# Definir las restricciones
prob += x1 + x2 <= 7
prob += 10*x1 + 4*x2 <= 40
prob += 25*x1 >= 30

# Resolver el modelo
prob.solve()

# Imprimir la solución
print("Número de hectáreas de limón a plantar:", value(x1))
print("Número de hectáreas de naranja a plantar:", value(x2))
print("Ingreso total máximo:", value(prob.objective), "dólares")
