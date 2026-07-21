from services.openai_service import OpenAIService
from tools.registry import ToolRegistry
from tools.datetime_tool import DateTimeTool
from agents.simple_agent import SimpleAgent

llm = OpenAIService()
registry = ToolRegistry()
registry.register(DateTimeTool())

agent = SimpleAgent(llm, registry)

while True:
    prompt = input("Eu: ")
    if prompt.lower() == "sair":
        break
    response = agent.run(prompt)

    print()
    print("TuxBot: ",response)
    print()
