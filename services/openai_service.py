import json
import time

from openai import OpenAI
from tools.registry import ToolRegistry
from tools.datetime_tool import DateTimeTool
from core.base_llm import BaseLLM
from core.llm_response import LLMResponse
from core.llm_response import ToolCall
from core.observability import Observability

from config.settings import (
        OPENAI_API_KEY,
        OPENAI_MODEL,
    )

registry = ToolRegistry()
registry.register(DateTimeTool())

class OpenAIService(BaseLLM):
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate(self, prompt: str):
        try:
            tools=registry.schemas()
            llm_start = time.perf_counter()
            response = self.client.responses.create(
                model=OPENAI_MODEL,
                input=prompt,
                tools=tools,
            )
            llm_end = time.perf_counter()

            Observability.log_duration("LLM respondeu em", llm_end - llm_start)
          
            tool_calls = []
            for item in response.output:
                if item.type == "function_call":
                    tool_calls.append(
                    ToolCall(
                        name = item.name,
                        arguments = json.loads(item.arguments),
                        call_id = item.call_id,
                )
            )
            return LLMResponse(
                text = response.output_text,
                tool_calls = tool_calls,
                response_id = response.id,
                input_tokens=response.usage.input_tokens,
                output_tokens=response.usage.output_tokens,
                total_tokens=response.usage.total_tokens,
            )

        except Exception as e:
            raise RuntimeError(
                f"Erro ao consultar OpenAI:{e}"
            ) from e
        
    def submit_tool_result(
            self,
            previous_response_id: str,
            tool_call_id: str,
            tool_output: str,
        ):
        response = self.client.responses.create(
            model=OPENAI_MODEL,
            previous_response_id=previous_response_id,
            input=[
                {
                    "type": "function_call_output",
                    "call_id": tool_call_id,
                    "output": tool_output,
                }
            ],
        )
        return LLMResponse(
            text = response.output_text,
            response_id = response.id,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            total_tokens=response.usage.total_tokens,
        )