from services.openai_service import OpenAIService
from tools.registry import ToolRegistry
from tools.datetime_tool import DateTimeTool
from agents.simple_agent import SimpleAgent
from memory.summary_memory import SummaryMemory
from services.llm_summarizer import LLMSummarizer

llm = OpenAIService()
registry = ToolRegistry()
registry.register(DateTimeTool())
memory = SummaryMemory(max_messages=10)
summarizer = LLMSummarizer(llm)

agent = SimpleAgent(llm, registry, memory, summarizer)

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