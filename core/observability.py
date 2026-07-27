from core.logger import Logger

class Observability:

    @staticmethod
    def log_token_usage(response):
        Logger.info(
            f"Input Tokens:{response.input_tokens}"
        )
        Logger.info(
            f"Output Tokens: {response.output_tokens}"
        )
        Logger.info(
            f"Total Tokens: {response.total_tokens}"
        )

    @staticmethod
    def log_duration(name: str, duration: float):
        Logger.info(
            f"{name}: {duration}s"
        )

    @staticmethod
    def log_tool(tool_name: str):
         Logger.info(
            f"Tool selecionada: {tool_name}"
        )