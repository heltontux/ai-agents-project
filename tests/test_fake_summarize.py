from tests.fakes.fake_summarizer import FakeSummarizer
from memory.summary_memory import SummaryMemory
from core.message import Message

def test_fake_summarizer():
    summarizer = FakeSummarizer()
    memory = SummaryMemory(max_messages=3)
    assert summarizer.called == False

    summary = summarizer.summarize(memory.get())
    assert summarizer.called == True
    assert summary == "This is a fake summary."

def test_memory_not_clear_summary():
    memory = SummaryMemory(max_messages=3)

    memory.update_summary("Resumo da conversa")

    memory.add(Message(role="user", content="Mensagem 1"))
    memory.add(Message(role="user", content="Mensagem 2"))

    memory.clear_messages()

    assert memory.get_summary() == "Resumo da conversa"
    assert len(memory.get()) == 1