import boto3 # permite acceder y utilizar los servicios de Amazon Web Services (AWS) (conf y admin)
#es una librería de AWS que proporciona una forma de construir, entrenar y desplegar modelos de 
#aprendizaje automático de forma escalable y eficiente en la nube de AWS.
from sagemaker import get_excecute_role #  intenta obtener automáticamente el rol de ejecución
# actualmente en uso en el entorno de ejecución en el que se está ejecutando el código
from sagemaker import LinearLearner # crear, entrenar y desplegar modelos de aprendizaje automático lineales en SageMaker 

# ROL :  es una entidad que se utiliza para conceder permisos a Amazon SageMaker y a otros servicios de AWS

# Definir los datos de entrada del problema
train_data = [[1,2],[2,1],[3,1]]
train_labels = [10,15,0]
num_features = len(train_data[0])

# Configurar SageMaker
sagemaker_session = boto3.Session().client('sagemaker')
role = get_excecute_role()
container = LinearLearner(role=role,train_instance_count=1,
	train_instance_type='ml.c4.xlarge', predictor_type='binary_ classifier')