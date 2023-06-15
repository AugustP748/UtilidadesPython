import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

atencion = ctrl.Antecedent(np.arange(1, 11, 1), 'atencion')
comida = ctrl.Antecedent(np.arange(1, 11, 1), 'comida')
demora_comida = ctrl.Antecedent(np.arange(1, 11, 1), 'demora_comida')
calificacion = ctrl.Consequent(np.arange(1, 11, 1), 'calificacion')

atencion['baja'] = fuzz.trimf(atencion.universe, [1, 1, 5])
atencion['regular'] = fuzz.trimf(atencion.universe, [1, 5, 9])
atencion['alta'] = fuzz.trimf(atencion.universe, [5, 9, 10])

comida['mala'] = fuzz.trimf(comida.universe, [1, 1, 5])
comida['promedio'] = fuzz.trimf(comida.universe, [1, 5, 9])
comida['excelente'] = fuzz.trimf(comida.universe, [5, 9, 10])

demora_comida['lenta'] = fuzz.trimf(demora_comida.universe, [1, 1, 5])
demora_comida['aceptable'] = fuzz.trimf(demora_comida.universe, [1, 5, 9])
demora_comida['rapida'] = fuzz.trimf(demora_comida.universe, [5, 9, 10])

calificacion['baja'] = fuzz.trimf(calificacion.universe, [1, 1, 5])
calificacion['regular'] = fuzz.trimf(calificacion.universe, [1, 5, 9])
calificacion['alta'] = fuzz.trimf(calificacion.universe, [5, 9, 10])

regla1 = ctrl.Rule(atencion['alta'] & comida['excelente'] & demora_comida['aceptable'], calificacion['alta'])
regla2 = ctrl.Rule(atencion['regular'] & comida['promedio'] & demora_comida['aceptable'], calificacion['regular'])
regla3 = ctrl.Rule(atencion['baja'] & comida['mala'] & demora_comida['lenta'], calificacion['baja'])

sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
sistema_calificacion = ctrl.ControlSystemSimulation(sistema_control)

sistema_calificacion.input['atencion'] = 9
sistema_calificacion.input['comida'] = 7
sistema_calificacion.input['demora_comida'] = 5

sistema_calificacion.compute()

calificacion_difusa = sistema_calificacion.output['calificacion']
calificacion_defuzz = fuzz.defuzz(calificacion.universe, calificacion_difusa, 'centroid')

print("Calificación difusa: {:.2f}".format(calificacion_difusa))
print("Calificación desdifusificada: {:.2f}".format(calificacion_defuzz))