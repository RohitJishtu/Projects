from pydantic import field_validator
from langchain_community.llms import Ollama

class Model:

    def __init__(name=None,description=None):
        name=name
        description=description

    def Calling_Local_LAMA(self,prompt=None):
        llm = Ollama(model="llama3")
        if prompt==None:
            prompt = "Tell me a joke about llama"
        result = llm.invoke(prompt)
        return result