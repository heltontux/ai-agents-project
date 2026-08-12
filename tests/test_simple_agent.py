from agents.simple_agent import SimpleAgent
from tests.fakes.fake_openai_service import FakeOpenAIService
from tools.registry import ToolRegistry
from tools.datetime_tool import DateTimeTool
from memory.in_memory import InMemory
from services.llm_summarizer import LLMSummarizer
from memory.summary_memory import SummaryMemory
from tests.fakes.fake_summarizer import FakeSummarizer
from core.message import Message
from core.role import Role

def test_simple_agent_executes_tool():
    registry = ToolRegistry()
    registry.register(DateTimeTool())
    memory = InMemory()
    llm = FakeOpenAIService()
    llm.simulate_tool_call = True
    summarizer = LLMSummarizer(llm=llm)
    
    agent = SimpleAgent(llm=llm, registry=registry, memory=memory, summarizer=summarizer)

    response = agent.run(Message(role="user", content="Que horas são?"))
    assert response.text == llm.tool_result

def test_simple_agent_summarizes_memory():
    llm = FakeOpenAIService()
    memory = SummaryMemory(max_messages=3)
    summarizer = FakeSummarizer()
    registry = ToolRegistry()

    agent = SimpleAgent(
        llm=llm,
        memory=memory,
        registry=registry,
        summarizer=summarizer,
    )

    memory.add(Message(role="user", content="Mensagem 1"))
    memory.add(Message(role="user", content="Mensagem 2"))
    memory.add(Message(role="user", content="Mensagem 3"))

    agent.run(Message(role="user", content="Mensagem nova"))

    assert summarizer.called
    assert memory.get_summary() == "This is a fake summary."

def test_simple_agent_does_not_duplicate_assistant_response():
    llm = FakeOpenAIService()
    registry = ToolRegistry()
    memory = SummaryMemory(max_messages=3)
    summarizer = FakeSummarizer()

    agent = SimpleAgent(llm=llm,
                        registry=registry,
                        memory=memory,
                        summarizer=summarizer)

    agent.run("pergunta que dispara tool")
    messages = memory.get()

    assistant_messages = [
        message
        for message in messages
        if message.role == Role.ASSISTANT
    ]

    assert len(assistant_messages) == 1