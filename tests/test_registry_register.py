import pytest

from tools.registry import ToolRegistry
from tools.datetime_tool import DateTimeTool

# Verifica duplicidade
def test_duplicate_tool_registration():
    registry = ToolRegistry()
    registry.register(DateTimeTool())

    with pytest.raises(ValueError):
        registry.register(DateTimeTool())

# Verifica a sáida do get()
# O Registry retorna a Tool registrada?                 
def test_registry_returns_registered_tool():
    registry = ToolRegistry()
    tool = DateTimeTool()
    registry.register(tool)
    assert registry.get(tool.name) == tool

# Verifica se o registro aconteceu.
def test_registry_register():
    registry = ToolRegistry()
    tool = DateTimeTool()
    registry.register(tool)
    assert len(registry.all()) == 1

# Validar to conteúdo do schema.
def test_registry_returns_schema():
    registry = ToolRegistry()
    registry.register(DateTimeTool())
    schemas = registry.schemas()
    assert isinstance(schemas, list)
    assert len(schemas) == 1