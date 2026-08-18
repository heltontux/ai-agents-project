from mcp.server.mcpserver import MCPServer
from datetime import datetime

mcp = MCPServer("TuxBot Server v1.0")

@mcp.tool()
def get_current_datetime() -> str:
    from datetime import datetime
    """Returns the current date and time as a string."""
    return datetime.now().isoformat()

if __name__ == "__main__":
    mcp.run()