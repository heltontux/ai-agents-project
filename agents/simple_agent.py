import time

from core.observability import Observability
from tools.registry import ToolRegistry
from core.base_llm import BaseLLM
from core.base_memory import BaseMemory
from core.base_summarizer import BaseSummarizer
from core.summarizable import Summarizable

class SimpleAgent:

    def __init__(
        self, 
        llm: BaseLLM, 
        registry: ToolRegistry, 
        memory: BaseMemory,
        summarizer: BaseSummarizer
    ):
        self.llm = llm
        self.registry = registry
        self.memory = memory
        self.summarizer = summarizer

    def _summarize_if_needed(self):
        if not isinstance(self.memory, Summarizable):
            return
        
        if not self.memory.should_summarize():
            return

        messages = self.memory.get_messages_to_summarize()
        summary = self.summarizer.summarize(messages)
        self.memory.clear_messages()
        self.memory.update_summary(summary)
    
    def run(self, prompt: str):
        self.memory.add_user(prompt)
        self._summarize_if_needed()
        messages = self.memory.get()

        agent_start = time.perf_counter()

        response = self.llm.generate(messages)

        Observability.log_token_usage(response)

        for tool_call in response.tool_calls:
            tool = self.registry.get(tool_call.name)

            Observability.log_tool(tool_call.name)

            tool_start = time.perf_counter()
            result = tool.execute(**tool_call.arguments)
            tool_end = time.perf_counter()

            Observability.log_duration("A Tool executou em", tool_end - tool_start)

            response = self.llm.submit_tool_result(
                response.response_id,
                tool_call.call_id,
                result,
            )

        agent_end = time.perf_counter()

        Observability.log_duration("Tempo total", agent_end - agent_start)

        self.memory.add_assistant(response.text)

        return response
