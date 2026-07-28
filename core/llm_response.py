from dataclasses import dataclass, field

@dataclass
class ToolCall:
        name: str
        arguments: dict
        call_id: str

@dataclass
class LLMResponse:
        text: str = ""
        tool_calls: list[ToolCall] = field(default_factory=list)
        response_id: str | None = None
        input_tokens: int = 0
        output_tokens: int = 0
        total_tokens: int = 0