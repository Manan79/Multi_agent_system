import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
import os
load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            
        "github": {
            "transport": "http",
            "url": "http://localhost:8082",
            "headers": {
                "Authorization": f"Bearer {os.environ['GITHUB_PERSONAL_ACCESS_TOKEN']}"
            }
        }

        }
    )

    tools = await client.get_tools()
    # print("Available tools are:", tools)
    for tool in tools:
        print(tool.name)
    


if __name__ == "__main__":
    asyncio.run(main())