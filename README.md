# Installation Steps

To Install "Sample MCP Addition Server, run the following command:

    uvx --from git+https://github.com/bala-murthy/mcpserver-sample.git mcp-server

This will fetch and setup the mcp-server from the above GitHub repo.

Or to add to your MCP Host, add the following in your config file in addition to existing MCP servers:

  "MCP-Server-Addition":{
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/bala-murthy/mcpserver-sample.git",
        "mcp-server"
      ]
    }