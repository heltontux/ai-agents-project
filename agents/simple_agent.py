import json

class SimpleAgent:

    def __init__(self, llm, registry):
        self.llm = llm
        self.registry = registry

    def run(self, prompt: str):
        response = self.llm.generate(prompt)

        for tool_call in response.tool_calls:

            tool = self.registry.get(tool_call.name)

            result = tool.execute(**tool_call.arguments)

            return self.llm.submit_tool_result(
                response.response_id,
                tool_call.call_id,
                result,
            )
        return response