
from tools.base_tool import BaseTool

class ToolRegistry:

    def __init__(self):
        self._tools= {}

    def register(self, tool:BaseTool):
        self._tools[tool.name] = tool
    
    def get(self, name):
        return self._tools.get(name)
    
    def all(self):
        return self._tools.values()