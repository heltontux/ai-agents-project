import json
import time

from core.logger import Logger

class SimpleAgent:

    def __init__(self, llm, registry):
        self.llm = llm
        self.registry = registry

    def run(self, prompt: str):
        agent_start = time.perf_counter()
        response = self.llm.generate(prompt)
        for tool_call in response.tool_calls:
            tool = self.registry.get(tool_call.name)
            Logger.info(
                f"Tooll selecionada: {tool_call.name}"
            )
            tool_start = time.perf_counter()
            result = tool.execute(**tool_call.arguments)
            tool_end = time.perf_counter()
            Logger.info(
                f"A Tool executou em {tool_end - tool_start:.3f}s"
            )
            response = self.llm.submit_tool_result(
                response.response_id,
                tool_call.call_id,
                result,
            )
        agent_end = time.perf_counter()
        Logger.info(
            f"Tempo total: {agent_end - agent_start:.3f}s"
        )
        return response
