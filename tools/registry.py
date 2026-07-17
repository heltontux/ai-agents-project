
from tools.base_tool import BaseTool

class ToolRegistry:

    def __init__(self):
        self._tools= {}

    def register(self, tool:BaseTool):
        if tool.name in self._tools:
            raise ValueError(
                f"Tool '{tool.name}' already registered."
            )
        self._tools[tool.name] = tool
    
    def get(self, name):
        return self._tools.get(name)
    
    def all(self):
        return self._tools.values()
    
    def schemas(self):
        return [
            tool.schema()
            for tool in self._tools.values()
        ]