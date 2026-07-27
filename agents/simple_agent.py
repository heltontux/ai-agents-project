import json
import time

from core.logger import Logger
from core.observability import Observability

class SimpleAgent:

    def __init__(self, llm, registry):
        self.llm = llm
        self.registry = registry

    def run(self, prompt: str):
        agent_start = time.perf_counter()
        response = self.llm.generate(prompt)

        Observability.log_token_usage(response)

        for tool_call in response.tool_calls:
            tool = self.registry.get(tool_call.name)

            Observability.log_tool(tool_call.name)

            tool_start = time.perf_counter()
            result = tool.execute(**tool_call.arguments)
            tool_end = time.perf_counter()

            Observability.log_duration("A Tool executou em", tool_end - tool_start)

            response = self.llm.submit_tool_result(
                response.response_id,
                tool_call.call_id,
                result,
            )
        agent_end = time.perf_counter()

        Observability.log_duration("Tempo total", agent_end - agent_start)

        return response
