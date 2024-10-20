from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain.prompts import StringPromptTemplate
from langchain import OpenAI, SerpAPIWrapper, LLMChain
from langchain.schema import AgentAction, AgentFinish
from typing import List, Union
import re

# Definir las herramientas del agente
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="útil para cuando necesitas responder preguntas sobre eventos actuales"
    )
]

# Definir el template del prompt
template = """Responde la siguiente pregunta lo mejor que puedas. Tienes acceso a la siguiente herramienta:

{tools}

Usa el siguiente formato:

Question: la pregunta de entrada que debes responder
Thought: siempre debes pensar sobre qué hacer
Action: la acción a tomar, debe ser una de [{tool_names}]
Action Input: la entrada a la acción
Observation: el resultado de la acción
... (este Thought/Action/Action Input/Observation puede repetirse N veces)
Thought: Ahora sé la respuesta final
Final Answer: la respuesta final a la pregunta original

Question: {input}
{agent_scratchpad}"""

# Definir el prompt
class CustomPromptTemplate(StringPromptTemplate):
    template: str
    tools: List[Tool]
    
    def format(self, **kwargs) -> str:
        intermediate_steps = kwargs.pop("intermediate_steps")
        thoughts = ""
        for action, observation in intermediate_steps:
            thoughts += action.log
            thoughts += f"\nObservation: {observation}\nThought: "
        kwargs["agent_scratchpad"] = thoughts
        kwargs["tools"] = "\n".join([f"{tool.name}: {tool.description}" for tool in self.tools])
        kwargs["tool_names"] = ", ".join([tool.name for tool in self.tools])
        return self.template.format(**kwargs)

prompt = CustomPromptTemplate(
    template=template,
    tools=tools,
    input_variables=["input", "intermediate_steps"]
)

# Definir el output parser
class CustomOutputParser(AgentOutputParser):
    
    def parse(self, llm_output: str) -> Union[AgentAction, AgentFinish]:
        if "Final Answer:" in llm_output:
            return AgentFinish(
                return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
                log=llm_output,
            )
        
        regex = r"Action\s*\d*\s*:(.*?)\nAction\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"
        match = re.search(regex, llm_output, re.DOTALL)
        if not match:
            raise ValueError(f"Could not parse LLM output: `{llm_output}`")
        action = match.group(1).strip()
        action_input = match.group(2)
        return AgentAction(tool=action, tool_input=action_input.strip(" ").strip('"'), log=llm_output)

output_parser = CustomOutputParser()

# Definir el modelo de lenguaje
llm = OpenAI(temperature=0)

# Definir la cadena LLM
llm_chain = LLMChain(llm=llm, prompt=prompt)

# Definir el agente
agent = LLMSingleActionAgent(
    llm_chain=llm_chain, 
    output_parser=output_parser,
    stop=["\nObservation:"], 
    allowed_tools=[tool.name for tool in tools]
)

# Definir el ejecutor del agente
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)

# Usar el agente
agent_executor.run("¿Cuál es el clima actual en Madrid?")