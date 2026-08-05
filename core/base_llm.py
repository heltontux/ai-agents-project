from abc import ABC, abstractmethod
from core.message import Message

class BaseLLM(ABC):

    @abstractmethod
    def generate(self, messages: list[Message]):
        pass

    @abstractmethod
    def submit_tool_result(
        self,
        previous_response_id,
        tool_call_id,
        tool_output,
    ):
        pass
