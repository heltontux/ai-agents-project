from abc import ABC, abstractmethod
from core.message import Message

class Summarizable(ABC):
    @abstractmethod
    def should_summarize(self) -> bool:
        pass

    @abstractmethod
    def get_messages_to_summarize(self) -> list[Message]:
        pass
    @abstractmethod
    def update_summary(self, summary: str):
        pass