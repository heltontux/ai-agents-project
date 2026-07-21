from core.base_llm import BaseLLM
from core.llm_response import LLMResponse

class FakeOpenAIService(BaseLLM):
    def generate(self, prompt):
        return LLMResponse(
            text = "Resposta Fake"
        )