from typing import Union, Any

from mcp.server.fastmcp import Context
from mcp.types import CallToolResult, TextContent

from config import mcp, AppContext
from exceptions import MemCommerceAPIException
from schemas.size_schemas import Size, SizeData
from api.sizes import get_all_sizes, post_sizes


@mcp.tool()
async def make_get_all_sizes_request(
    ctx: Context[Any, AppContext],
) -> Union[list[Size], CallToolResult]:
    """
    Retrieve all available sizes from the MemCommerce API with proper error handling.

    In the MemCommerce system, 'sizes' represent standard clothing or accessory
    dimensions (e.g., XS, S, M, L, XL) used to define product variants. This
    data is typically displayed on product pages, used in filters, and needed
    when managing inventory and variant creation.

    Returns:
        Union[list[Size], CallToolResult]: A list of sizes on success,
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


@mcp.tool()
async def add_sizes(
    sizes_labels: list[str], ctx: Context[Any, AppContext]
) -> Union[list[Size], CallToolResult]:
    """
    Add one or more new product sizes to the MemCommerce system.

    In MemCommerce, sizes represent variant options for clothing and other products 
    (e.g., XS, S, M, L, XL). This tool allows agents or automated flows to bulk-create 
    new size entries by providing their labels (e.g., ["XXL", "4XL"]).

    Args:
        sizes_labels (list[str]): A list of size labels to create.

    Returns:
        Union[list[Size], CallToolResult]: A list of newly created Size objects on success,
        or a CallToolResult indicating an API error.
    """
    api_url = ctx.request_context.lifespan_context.memcommerce_api_url
    sizes_data = [SizeData(label=label) for label in sizes_labels]
    try:
        sizes = await post_sizes(sizes_data, api_url)
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
