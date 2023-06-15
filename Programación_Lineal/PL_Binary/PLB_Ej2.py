from pulp import *

"""
Problema 2
    Se desea ampliar ampliar una compañía compañía con la instalación instalación de una nueva factoría factoría en Zaragoza Zaragoza o Sevilla Sevilla o en ambas ciudades ciudades. También También se piensa
construir a lo sumo un almacén en una ciudad donde se instale alguna factoría. En la siguiente tabla aparecen los beneficios estimados
de instalar una factoría y construir un almacén en Zaragoza y Sevilla, y el capital requerido para ello. Se dispone de un capital total para
la inversión de 39 M euros. El objetivo es tomar las decisiones que optimicen el beneficio de la inversión.

Decisiones                          Beneficio       estimado Capital requerido
Instalar una factoría en Zaragoza   19 M euros      16 M euros
Instalar una factoría en Sevilla    15 M euros      13 M euros
Construir un almacén en Zaragoza    16 M euros      15 M euros
Construir un almacén en Sevilla     14 M euros      12 M euros
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
prob += 19*x1+15*x2+16*x3+14*x4

# Definir las restricciones
prob += 16*x1 + 13*x2 + 15*x3 + 12*x4 <= 39
prob += 1*x3 + 1*x4 <= 1
prob += 1*x3 <= 1*x1
prob += 1*x4 <= 1*x2

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
