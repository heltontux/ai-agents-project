from abc import ABC, abstractmethod

class BaseMemory(ABC):
    @abstractmethod
    def add(self, message):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def clear(self):
        pass