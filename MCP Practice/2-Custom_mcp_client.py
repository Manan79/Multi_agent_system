import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    # server_script = r"C:\Users\soodm\Desktop\Multi Agent System\MCP Practice\1-practice.py"

    client = MultiServerMCPClient(
    {
            "data_fetch_mcp": {
                "transport": "stdio",
                "command": "uvx",
                "args": ["mcp-server-git"],
            }

    })
    tools = await client.get_tools()
    print("Available tools are:", len(tools))
    for tool in tools:
        print("Available tools:", tool.name)


if __name__ == "__main__":
    asyncio.run(main())