
from tools.registry import ToolRegistry
from tools.datetime_tool import DateTimeTool

registry = ToolRegistry()

registry.register(DateTimeTool())

tool = registry.get("get_current_datetime")

print(tool.execute())