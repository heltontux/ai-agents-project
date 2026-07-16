import json

from services.openai_service import OpenAIService

from tools.registry import ToolRegistry
from tools.datetime_tool import DateTimeTool

class SimpleAgent:

    def __init__(self):
        self.llm = OpenAIService()
        self.registry = ToolRegistry()
        self.registry.register(DateTimeTool())

    def run(self, prompt: str):
        response = self.llm.generate(prompt)

        for item in response.output:

            if item.type == "function_call":

                tool = self.registry.get(item.name)

                arguments = json.loads(item.arguments)

                result = tool.execute(**arguments)

                final_response = self.llm.submit_tool_result(
                    previous_response_id=response.id,
                    call_id=item.call_id,
                    output=result,
                )

                return final_response.output_text
        
        return response.output_text



