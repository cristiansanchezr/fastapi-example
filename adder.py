from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="adder-server", 
              stateless_http=True)

@mcp.tool(description="Add two integers")
def add_two_integers(a: int, b: int) -> int:
    """
    Use this tool to obtain the result of adding two integers.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The sum of the two integers.
    """
    return a + b