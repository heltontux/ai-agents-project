from abc import ABC, abstractmethod
from core.message import Message

class BaseSummarizer(ABC):

    @abstractmethod
    def summarize(self, messages: list[Message]) -> str:
        pass