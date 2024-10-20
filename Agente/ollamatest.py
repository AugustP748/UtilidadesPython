from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Definimos el template del prompt
template = """
Eres un asistente útil, tu nombre es DermaBot y hablas solamente español, nada en inglés. 
Tu rol es guiar al usuario a detectar qué posibles enfermedades dermatológicas tiene y das recomendaciones y sugerencias.

Historial de la conversación:
{history}

Humano: {input}
DermaBot:"""

# Creamos el prompt
prompt = ChatPromptTemplate.from_template(template)

# Inicializamos el modelo
model = OllamaLLM(model="gemma2:2b", max_tokens=100)

# Creamos la memoria
memory = ConversationBufferMemory(return_messages=True)

# Creamos la cadena de conversación
conversation = ConversationChain(
    llm=model,
    memory=memory,
    prompt=prompt,
    verbose=True  # Esto mostrará el proceso de la conversación
)

# Función para manejar la conversación
def chat_with_dermabot(user_input):
    response = conversation.predict(input=user_input)
    return response

# Ejemplo de uso
#print(chat_with_dermabot("Hola"))
#print(chat_with_dermabot("Tengo una mancha roja en el brazo"))
#print(chat_with_dermabot("¿Qué debo hacer?"))

# Para ver el contenido de la memoria
print("\nContenido de la memoria:")
print(memory.chat_memory.messages)