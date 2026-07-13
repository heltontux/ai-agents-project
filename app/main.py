from services.openai_service import OpenAIService

service = OpenAIService()

resposta = service.generate_text(

    "Responda apenas: Olá, Projeto AI Agents!"
)

print(resposta)
