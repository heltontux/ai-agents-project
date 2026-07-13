from openai import OpenAI

from config.settings import OPENAI_API_KEY

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
    def ask(self, prompt: str):
        response = self.client.responses.create(
            model="gpt-5",
            input=prompt,
        )

        return response.output_text
