#from services.openai_service import OpenAIService
from agents.simple_agent import SimpleAgent

agent = SimpleAgent()

while True:
    prompt = input("Eu: ")
    if prompt.lower() == "sair":
        break
    resposta = agent.run(prompt)

    print()
    print("TuxBot: ", resposta)
    print()
