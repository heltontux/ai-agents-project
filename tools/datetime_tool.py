from datetime import datetime
from tools.base_tool import BaseTool

class DateTimeTool(BaseTool):

    @property
    def name(self):
        return "get_current_datetime"
    
    @property
    def description(self):
        return "Retorna a data e hora atual."

    @property
    def schema(self):
        pass

    def execute(self, **kwargs):
        return datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    