from contextlib import AsyncExitStack

from mcp import ClientSession
from mcp.client.stdio import stdio_client

class MCPClient:
    def __init__(self, server):
        self.server = server
        self.client = None
        self.exit_stack = AsyncExitStack()

    async def connect(self):
        read, write = await self.exit_stack.enter_async_context(
            stdio_client(self.server)
            )
        self.client = await self.exit_stack.enter_async_context(
            ClientSession(read, write)
            )
        await self.client.initialize()

    async def list_tools(self):
        if self.client is None:
            raise RuntimeError("MCP Client not connected")
        return await self.client.list_tools()

    async def call_tool(self, name, arguments):
        if self.client is None:
            raise RuntimeError("MCP Client not connected")
        return await self.client.call_tool(
            name,
            arguments
        )
    async def close(self):
        await self.exit_stack.aclose()

#======================================
import asyncio

from mcp import StdioServerParameters


server = StdioServerParameters(
    command="uv",
    args=["run", "python", "mcp/server.py"],
)


async def main():

    client = MCPClient(server)

    try:

        await client.connect()

        result = await client.list_tools()

        print("=== TOOLS ===")

        for tool in result.tools:
            print(tool.name)

        print()
        print("=== CALL ===")

        result = await client.call_tool(
            "get_current_datetime",
            {}
        )

        print(result.structured_content)

    finally:

        await client.close()


if __name__ == "__main__":
    asyncio.run(main())