from services.openai_service import OpenAIService



class SimpleAgent:

    def __init__(self):
        self.llm = OpenAIService()

    def run(self, prompt: str):
        
        return self.llm.generate(
            prompt=prompt
        )
