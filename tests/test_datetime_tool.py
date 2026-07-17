
from datetime import datetime
from tools.datetime_tool import DateTimeTool

def test_datetime_tool_returns_string():
    tool = DateTimeTool()
    result = tool.execute()

    assert isinstance(result, str)
    assert result != ''

    datetime.strptime(
        result, "%d/%m/%Y %H:%M:%S"
    )