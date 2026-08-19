import asyncio

from mcp import Client, StdioServerParameters
from mcp.client.stdio import stdio_client

server = StdioServerParameters(
    command="uv",
    args=["run", "python", "mcp/server.py"],
)

async def main():
    async with Client(stdio_client(server)) as (client):
        print('==== TOOLS DISPONIVEIS ====')
        result = await client.list_tools()

        for tool in result.tools:
            print(tool.name)

        print()
        print("=== EXECUTANDO TOOL ===")

        result = await client.call_tool(
            "get_current_datetime",
            {}
        )

        print("CONTENT:")
        print(result.content)

        print("STRUCTURED:")
        print(result.structured_content)

        print("ERROR:")
        print(result.is_error)

        content = result.content[0]
        print(type(content))
        print(content.text)

if __name__ == "__main__":
    asyncio.run(main())