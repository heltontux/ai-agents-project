from services.openai_service import OpenAIService

from tools.registry import ToolRegistry
from tools.datetime_tool import DateTimeTool

class SimpleAgent:

    def __init__(self):
        self.llm = OpenAIService()
        self.registry = ToolRegistry()
        self.registry.register(DateTimeTool)

    def run(self, prompt: str):
        response = self.llm.generate(prompt)
        return response
