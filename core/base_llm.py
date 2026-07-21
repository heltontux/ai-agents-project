from abc import ABC, abstractmethod

class BaseLLM(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass

    @abstractmethod
    def submit_tool_result(
        self,
        previous_responde_id,
        tool_output,
    ):
        pass
