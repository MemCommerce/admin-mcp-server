from typing import Union, Any

from mcp.server.fastmcp import Context
from mcp.types import CallToolResult, TextContent

from config import mcp, AppContext
from exceptions import MemCommerceAPIException
from api.sizes import get_all_sizes


@mcp.tool()
async def make_get_all_sizes_request(
    ctx: Context[Any, AppContext],
) -> Union[dict, CallToolResult]:
    """
    Retrieve all available sizes from the MemCommerce API with proper error handling.

    In the MemCommerce system, 'sizes' represent standard clothing or accessory 
    dimensions (e.g., XS, S, M, L, XL) used to define product variants. This 
    data is typically displayed on product pages, used in filters, and needed 
    when managing inventory and variant creation.

    Returns:
        Union[dict[str, Any], CallToolResult]: A dictionary of sizes on success,
        or a CallToolResult error on failure.
    """
    api_url = ctx.request_context.lifespan_context.memcommerce_api_url

    try:
        sizes = await get_all_sizes(api_url)
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"Weatherstack API Error {e}")],
        )

    return sizes


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
