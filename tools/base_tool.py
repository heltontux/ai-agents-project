
from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
    Base class for all tools used by agents.
    Every Tool must provide a name, a description, and an execute() method.
    """
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def schema(self):
        pass

    @abstractmethod
    def execute(self, **kwargs):
        pass
