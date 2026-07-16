from openai import OpenAI
from tools.registry import ToolRegistry
from tools.datetime_tool import DateTimeTool

from config.settings import (
        OPENAI_API_KEY,
        OPENAI_MODEL,
    )

registry = ToolRegistry()
registry.register(DateTimeTool())

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate(self, prompt: str):
        try:
            tools=registry.schemas()
            response = self.client.responses.create(
                model=OPENAI_MODEL,
                input=prompt,
                tools=tools,
        )
            return response
        except Exception as e:
            raise RuntimeError(
                f"Erro ao consultar OpenAI:{e}"
            )
        
    def submit_tool_result(
            self,
            previous_response_id: str,
            call_id: str,
            output: str,
        ):
        return self.client.responses.create(
            model=OPENAI_MODEL,
            previous_response_id=previous_response_id,
            input=[
                {
                    "type": "function_call_output",
                    "call_id": call_id,
                    "output": output,
                }
            ],
        )