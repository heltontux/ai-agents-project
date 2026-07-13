from openai import OpenAI

from config.settings import (
        OPENAI_API_KEY,
        OPENAI_MODEL,
    )

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate_text(self, prompt: str):
        try:
            response = self.client.responses.create(
            model=OPENAI_MODEL,
            input=prompt,
        )

            return response.output_text

        except Exception as e:

            raise RuntimeError(
                f"Erro ao consultar OpenAI:{e}"
            )
