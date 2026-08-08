import os 
from mcp.client.stdio import stdio_client
from mcp import client , ClientSession , StdioServerParameters
import asyncio


server_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , "1-practice.py")

print(server_path)

server_param = StdioServerParameters(
    command="python",
    args=[str(server_path)],
    env = {}
)

async def main():
    async with stdio_client(server_param) as (read,write):
        async with ClientSession(read , write) as session :
            await session.initialize()

            tools = await session.list_tools()

            print(tools)


if __name__ == "__main__":
    asyncio.run(main())
