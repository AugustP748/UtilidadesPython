from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
# Inicializar el modelo Gemma2 de Ollama
#llm = OllamaLLM(model="gemma2:2b")

template = """
Eres un asistente útil, tu nombre es DermaBot y hablas solamente español, nada en inglés. 
Tu rol es guiar al usuario a detectar qué posibles enfermedades dermatológicas tiene y das recomendaciones y sugerencias"
Mensaje del usuario: {mensaje}
Respuesta del chatbot:

"""
# Hacer una prueba con un input básico

prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="gemma2:2b",max_tokens=100)

chain = prompt | model

response = chain.invoke({"mensaje": "Hola"})

print(response)