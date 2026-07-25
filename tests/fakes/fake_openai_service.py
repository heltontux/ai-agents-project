import time

from core.base_llm import BaseLLM
from core.llm_response import LLMResponse, ToolCall
from core.logger import Logger

class FakeOpenAIService(BaseLLM):

    def __init__(self):
        self.tool_result = None

    def generate(self, prompt):
        llm_start = time.perf_counter()
        llm_end = time.perf_counter()
        Logger.info(
            f"LLM respondeu em {llm_end - llm_start:.3f}s"
        )
        return LLMResponse(
            tool_calls = [
                ToolCall(
                    name = "get_current_datetime",
                    arguments = {},
                    call_id = "fake-call-001"
                )
            ]
        )

    def submit_tool_result(
            self,
            previous_responde_id, 
            tool_call_id, 
            tool_output):
        self.tool_result = tool_output
        return LLMResponse(
            text = tool_output
        )