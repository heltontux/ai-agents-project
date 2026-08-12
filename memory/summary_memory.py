
from collections import deque
from core.base_memory import BaseMemory
from core.message import Message
from core.summarizable import Summarizable
from core.role import Role

class SummaryMemory(BaseMemory, Summarizable):
    def __init__(self, max_messages: int):
        self._summary = ""
        self._messages = deque(maxlen=max_messages)

    def is_full(self) -> bool:
        return len(self._messages) == self._messages.maxlen

    def add(self, message: Message):
        self._messages.append(message)

    def get(self) -> list[Message]:
        messages = list(self._messages)
        if self._summary:
            messages.insert(
                0, 
                Message(
                    role=Role.ASSISTANT,
                    content=f"Resumo da conversa: {self._summary}"
                )
            )
        return messages

    def clear(self):
        self._messages.clear()
        self._summary = ""

    def clear_messages(self):
        self._messages.clear()

    def update_summary(self, summary: str):
        self._summary = summary

    def get_summary(self) -> str:
        return self._summary

    def get_messages_to_summarize(self) -> list[Message]:
        return list(self._messages)

    def should_summarize(self) -> bool:
        return self.is_full()