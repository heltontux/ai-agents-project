from core.base_summarizer import BaseSummarizer
from core.base_llm import BaseLLM
from core.message import Message
from core.role import Role

class LLMSummarizer(BaseSummarizer):
    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def summarize(self, messages: list[Message]) -> str:
        instruction = Message(
            role=Role.USER,
            content=(
                "Resuma a conversa abaixo para ser usada como memória "
                "em interações futuras. Preserve informações importantes "
                "sobre o usuário, como nome, idade, preferências, objetivos "
                "e fatos relevantes. Não responda às perguntas da conversa. "
                "Apenas produza o resumo."
            )
        )
        messages_to_summarize = [instruction, *messages]
        response = self.llm.generate(messages_to_summarize)
        return response.text