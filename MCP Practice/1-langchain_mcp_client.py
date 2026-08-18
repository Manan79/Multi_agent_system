import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    server_script = r"C:\Users\soodm\Desktop\Multi Agent System\MCP Practice\1-practice.py"

    client = MultiServerMCPClient(
        {
            "data_fetch_mcp": {
                "transport": "stdio",
                "command": r"C:\Users\soodm\Desktop\Multi Agent System\.venv\Scripts\python.exe",
                "args": [server_script],
            }
        }
    )

    tools = await client.get_tools()
    print("Available tools are:", tools)


if __name__ == "__main__":
    asyncio.run(main())