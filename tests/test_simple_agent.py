from agents.simple_agent import SimpleAgent
from tests.fakes.fake_openai_service import FakeOpenAIService
from tools.registry import ToolRegistry
from tools.datetime_tool import DateTimeTool
from memory.in_memory import InMemory

def test_simple_agent_executes_tool():
    registry = ToolRegistry()
    registry.register(DateTimeTool())
    memory = InMemory()

    llm = FakeOpenAIService()
    agent = SimpleAgent(llm=llm, registry=registry, memory=memory)

    response = agent.run("Que horas são?")
    assert response.text == llm.tool_result