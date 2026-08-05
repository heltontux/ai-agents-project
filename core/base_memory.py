from abc import ABC, abstractmethod
from core.message import Message
from core.role import Role

class BaseMemory(ABC):
    @abstractmethod
    def add(self, message: Message):
        pass

    def add_user(self, content: str):
        self.add(
            Message(
                Role.USER, 
                content,
            )
        )

    def add_assistant(self, content: str):
        self.add(
            Message(
                Role.ASSISTANT, 
                content,
            )
        )

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def clear(self):
        pass