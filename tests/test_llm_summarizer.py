from core import role
from tests.fakes.fake_openai_service import FakeOpenAIService
from services.llm_summarizer import LLMSummarizer
from core.message import Message
from core.role import Role

def test_llm_summarizer():
    llm = FakeOpenAIService()
    summarizer = LLMSummarizer(llm)
    messages = [
        Message(
            role=Role.USER,
            content="How are you?"),
        Message(
            role=Role.ASSISTANT,
            content="I am doing well, thank you."),
        Message(
            role=Role.USER,
            content="Please summarize them."),
        Message(
            role=Role.ASSISTANT,
            content="The messages can be summarized.")
    ]
    summary = summarizer.summarize(messages)
    assert isinstance(summary, str)
    assert summary == "Resposta do LLM fake"