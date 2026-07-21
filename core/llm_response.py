class ToolCall:
    def __init__(
            self,
            name: str,
            arguments: dict,
            call_id: str,
        ):
            self.name = name
            self.arguments = arguments
            self.call_id = call_id

class LLMResponse:
    def __init__(
        self,
        text: str = "",
        tool_calls: list[ToolCall] | None = None,
        response_id: str | None = None,
    ):
        self.text = text
        self.tool_calls = tool_calls or []
        self.response_id = response_id

