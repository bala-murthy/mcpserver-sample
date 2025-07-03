from mcp.server.fastmcp import FastMCP  


#Create a MCP Server
mcp = FastMCP("Demo-MCP Server")


# Adder a new Addition tool
@mcp.tool("MCP Addition")
def addition(a: int, b: int) -> int:
    """
    Adds two integers together.
    """
    return a + b
