from services.openai_service import OpenAIService

service = OpenAIService()

resposta = service.generate(

    "Responda apenas: Olá, Projeto AI Agents!"
)

print(resposta)
