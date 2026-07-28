from abc import ABC, abstractmethod

class BaseLLM(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass

    @abstractmethod
    def submit_tool_result(
        previous_response_id,
        tool_call_id,
        tool_output,
    ):
        pass
