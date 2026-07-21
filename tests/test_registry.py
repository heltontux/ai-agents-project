import pytest

from tools.registry import ToolRegistry
from tools.datetime_tool import DateTimeTool

def test_registry_register():
    registry = ToolRegistry()
    tool = DateTimeTool()
    registry.register(tool)
    assert len(list(registry.all())) == 1

def test_registry_returns_registered_tool():
    registry = ToolRegistry()
    tool = DateTimeTool()
    registry.register(tool)
    assert registry.get(tool.name) == tool

def test_registry_returns_schema():
    registry = ToolRegistry()
    registry.register(DateTimeTool())
    schemas = registry.schemas()
    assert isinstance(schemas, list)
    assert len(schemas) == 1

def test_duplicate_tool_registration():
    registry = ToolRegistry()
    registry.register(DateTimeTool())
    with pytest.raises(ValueError):
        registry.register(DateTimeTool())