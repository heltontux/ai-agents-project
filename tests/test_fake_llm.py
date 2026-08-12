from memory.in_memory import InMemory
from services.llm_summarizer import LLMSummarizer
from tests.fakes.fake_openai_service import FakeOpenAIService
from agents.simple_agent import SimpleAgent
from tools.registry import ToolRegistry
from core.role import Role

def test_fake_llm_integration():
    memory = InMemory()
    fake_llm = FakeOpenAIService()
    registry = ToolRegistry()
    summarizer = LLMSummarizer(llm=fake_llm)

    agent = SimpleAgent(llm=fake_llm, registry=registry, memory=memory, summarizer=summarizer)

    agent.run("Olá")

    assert len(fake_llm.received_messages) == 1
    assert fake_llm.received_messages[0].content == "Olá"
    assert fake_llm.received_messages[0].role == Role.USER