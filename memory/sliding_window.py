from core.base_memory import BaseMemory
from collections import deque
from core.message import Message

class SlidingWindow(BaseMemory):
    def __init__(self, max_messages: int):
        self._messages = deque(maxlen=max_messages)

    def add(self, message: Message):
        self._messages.append(message)

    def get(self):
        return list(self._messages)

    def clear(self):
        self._messages.clear()