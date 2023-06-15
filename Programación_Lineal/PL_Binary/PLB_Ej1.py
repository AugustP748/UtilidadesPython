from pulp import *

"""
Problema 1
    Se están considerando cuatro posibles inversiones. La primera de ellas se prevé que proporcione unos beneficios netos de
    16.000 euros, la segunda, 22.000 euros, la tercera 12.000 euros, y la cuarta 8.000 euros. Cada una de las inversiones
    requiere una cantidad de dinero en efectivo: 5.000, 7.000, 4.000 y 3.000 euros, respectivamente. Si solo se dispone de
    14.000 euros para invertir. ¿Qué modelo de programación lineal entera permite obtener la combinación de inversiones que
    prevea los máximos beneficios?
"""


# Crear el problema de maximización
prob = LpProblem("Ejemplo de Programación Lineal Entera", LpMaximize)

# Definir las variables de decisión (VARIABLES ENTERAS)
#x1 = LpVariable("x1", lowBound=0, cat='Integer')
#x2 = LpVariable("x2", lowBound=0, cat='Integer')
#x3 = LpVariable("x3", lowBound=0, cat='Integer')
#x4 = LpVariable("x4", lowBound=0, cat='Integer')

# Definir las variables de decisión (VARIABLES BINARIAS)
x1 = LpVariable("x1", cat='Binary')
x2 = LpVariable("x2", cat='Binary')
x3 = LpVariable("x3", cat='Binary')
x4 = LpVariable("x4", cat='Binary')

# Definir la función objetivo
prob += 16*x1+22*x2+12*x3+8*x4

# Definir las restricciones
prob += 5*x1 + 7*x2 + 4*x3 + 3*x4 <= 14

# Resolver el problema
prob.solve()

# Imprimir el estado de resolución
print("Estado:", LpStatus[prob.status])

# Imprimir los valores óptimos de las variables
print("Valor óptimo de x1:", value(x1))
print("Valor óptimo de x2:", value(x2))
print("Valor óptimo de x3:", value(x3))
print("Valor óptimo de x4:", value(x4))

# Imprimir el valor óptimo de la función objetivo
print("Valor óptimo de la función objetivo:", value(prob.objective))
