from core.base_llm import BaseLLM
from core.llm_response import LLMResponse, ToolCall

class FakeOpenAIService(BaseLLM):

    def __init__(self):
        self.tool_result = None

    def generate(self, prompt):
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