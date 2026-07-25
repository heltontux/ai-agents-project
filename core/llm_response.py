from dataclasses import dataclass

@dataclass
class ToolCall:
        name: str
        arguments: dict
        call_id: str

@dataclass
class LLMResponse:
        text: str = ""
        tool_calls: list[ToolCall] | None = None
        response_id: str | None = None