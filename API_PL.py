import boto3 
from sagemaker import get_execution_role, LinearLearner


# Definir los datos de entrada del problema
train_data = [[1,2],[2,1],[3,1]]
train_labels = [5,9,0]
num_features = len(train_data[0])

# Configurar SageMaker
sagemaker_session = boto3.Session().client('sagemaker')
role = get_execution_role()
container = LinearLearner(role=role,train_instance_count=1,
	train_instance_type='ml.c4.xlarge', predictor_type='binary_ classifier')


