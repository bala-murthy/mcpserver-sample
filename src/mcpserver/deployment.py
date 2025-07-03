from mcp.server.fastmcp import FastMCP  


#Create a MCP Server
mcp = FastMCP("Demo-MCP Server")


 # Add a new Addition tool
@mcp.tool("MCPServer_Addition")
def addition(a: int, b: int) -> int:
    """
    Adds two integers together.
    """
    return a + b
