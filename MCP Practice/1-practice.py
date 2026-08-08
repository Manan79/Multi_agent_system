from fastmcp import FastMCP

mcp = FastMCP()


@mcp.tool()
def fetch():
    """This tool is to fetch the data manually"""
    return {"data": "Hello from MCP"}


if __name__ == "__main__":
    mcp.run(transport='stdio')




