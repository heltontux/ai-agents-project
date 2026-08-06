import time

from core.base_llm import BaseLLM
from core.llm_response import LLMResponse, ToolCall
from core.logger import Logger
from pyexpat.errors import messages

class FakeOpenAIService(BaseLLM):

    def __init__(self):
        self.received_messages = []
        self.simulate_tool_call = False

    def generate(self, messages):
        llm_start = time.perf_counter()
        llm_end = time.perf_counter()
        Logger.info(
            f"LLM respondeu em {llm_end - llm_start:.3f}s"
        )
        self.received_messages = messages.copy()
        if self.simulate_tool_call:
            return LLMResponse(
                tool_calls = [
                    ToolCall(
                        name = "get_current_datetime",
                        arguments = {},
                        call_id = "fake-call-001"
                    )
                ]
            )
        return LLMResponse(
            text = "Resposta do LLM fake"
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