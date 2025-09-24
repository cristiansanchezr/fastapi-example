from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="suber-server", 
              stateless_http=True)

@mcp.tool(description="Subtract two integers")
def sub_two_integers(a: int, b: int) -> int:
    """
    Use this tool to obtain the result of subtracting two integers.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The difference of the two integers.
    """
    return a - b