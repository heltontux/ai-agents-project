from core.base_memory import BaseMemory
from core.message import Message

class InMemory(BaseMemory):
    def __init__(self):
        self._messages = []

    def add(self, message: Message):
        self._messages.append(message)

    def get(self):
        return self._messages

    def clear(self):
        self._messages.clear()