from services.openai_service import OpenAIService
#from tests.fakes.fake_openai_service import FakeOpenAIService
from tools.registry import ToolRegistry
from tools.datetime_tool import DateTimeTool
from agents.simple_agent import SimpleAgent
#from memory.in_memory import InMemory
from memory.sliding_window import SlidingWindow

llm = OpenAIService()
#llm = FakeOpenAIService()

registry = ToolRegistry()
registry.register(DateTimeTool())

#memory = InMemory()
memory = SlidingWindow(max_messages=4)

agent = SimpleAgent(llm, registry, memory)

while True:
    prompt = input("Eu: ")
    if prompt.lower() == "sair":
        break
    response = agent.run(prompt)

    print()
    print("TuxBot: ",response.text)
    print("=" * 20)
    print("Histórico de mensagens:")
    print(memory.get())