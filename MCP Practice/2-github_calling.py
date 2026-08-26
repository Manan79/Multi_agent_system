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
    # for tool in tools:
    #     print(tool.name)
    tools_used = next(
        t for t in tools
        if t.name == 'search_issues'
    )
#     result = await tools_used.ainvoke({
#     "owner": "Manan79",
#     "repo": "Multi_agent_system",
#     "path": "Memory"
# })
    result = await tools_used.ainvoke({
    "query": "repo:Manan79/Multi_agent_system"
})
    print(result)
    


if __name__ == "__main__":
    asyncio.run(main())