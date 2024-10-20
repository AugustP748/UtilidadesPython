import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir variables de entrada
humedad_suelo = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad_suelo')
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
horario_dia = ctrl.Antecedent(np.arange(0, 25, 1), 'horario_dia')

# Definir variable de salida
cantidad_agua = ctrl.Consequent(np.arange(0, 11, 1), 'cantidad_agua')

# Definir funciones de membresía para las variables de entrada y salida
# (aquí deberías definir tus propias funciones de membresía según tu conocimiento del sistema)

# Definir reglas difusas
regla1 = ctrl.Rule(humedad_suelo['alta'] & temperatura['baja'] & horario_dia['tarde'], cantidad_agua['alta'])
regla2 = ctrl.Rule(humedad_suelo['media'] & temperatura['media'] & horario_dia['tarde'], cantidad_agua['media'])
# Agregar más reglas según sea necesario

# Crear sistema de control difuso
sistema_riego = ctrl.ControlSystem([regla1, regla2])
riego = ctrl.ControlSystemSimulation(sistema_riego)

# Establecer valores de entrada
riego.input['humedad_suelo'] = 50
riego.input['temperatura'] = 70
riego.input['horario_dia'] = 15

# Calcular la salida
riego.compute()

# Obtener el valor de salida
print(riego.output['cantidad_agua'])

# Visualizar la distribución de membresía de la salida
cantidad_agua.view(sim=riego)
