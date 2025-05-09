from typing import Union, Any

from mcp.server.fastmcp import Context
from mcp.types import CallToolResult, TextContent

from config import mcp, AppContext
from exceptions import MemCommerceAPIException
from schemas.size_schemas import Size, SizeData
from schemas.category_schemas import Category, CategoryData
from schemas.color_schemas import Color, ColorData
from schemas.product_schemas import Product, ProductData
from api.sizes import get_all_sizes, post_sizes
from api.categories import get_all_categories, post_categories
from api.colors import get_all_colors, post_colors
from api.product import get_all_products, post_products


@mcp.tool()
async def make_get_all_products_request(
    ctx: Context[Any, AppContext],
) -> Union[list[Product], CallToolResult]:
    """
    Retrieve all existing products from the MemCommerce API.

    Products in MemCommerce are individual items assigned to a category
    and associated with brand and description details. This tool fetches
    the full list of registered products for use in variant creation,
    inventory management, or listing.

    Returns:
        Union[list[Product], CallToolResult]: A list of Product objects on success,
        or a CallToolResult indicating an API error.
    """
    api_url = ctx.request_context.lifespan_context.memcommerce_api_url

    try:
        products = await get_all_products(api_url)
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"MemCommerce API Error: {e}")],
        )

    return products


@mcp.tool()
async def add_products(
    products_data: list[ProductData],
    ctx: Context[Any, AppContext],
) -> Union[list[Product], CallToolResult]:
    """
    Add one or more new products to the MemCommerce system.

    In MemCommerce, products represent individual items that can be sold, such as
    specific T-shirts, shoes, or accessories. Each product has a name, brand, description,
    and is assigned to an existing category.

    Args:
        products_data (list[ProductData]): A list of ProductData objects, each containing:
            - `name`: The product name (e.g., "Adidas Sport T-Shirt")
            - `brand`: Brand label (e.g., "Adidas")
            - `description`: Textual description
            - `category_id`: UUID of the category to which the product belongs

    Returns:
        Union[list[Product], CallToolResult]: A list of created Product objects,
        or a CallToolResult indicating an API error.
    """
    api_url = ctx.request_context.lifespan_context.memcommerce_api_url

    try:
        products = await post_products(products_data, api_url)
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"MemCommerce API Error: {e}")],
        )

    return products


@mcp.tool()
async def make_get_all_colors_request(
    ctx: Context[Any, AppContext],
) -> Union[list[Color], CallToolResult]:
    """
    Retrieve all available product colors from the MemCommerce API.

    In MemCommerce, colors represent variant options for products based on their
    visual appearance (e.g., "Black", "White", "Navy"). Each color typically
    includes a label and a corresponding hex code for UI representation. This tool
    fetches the full list of colors currently registered in the system.

    Args:
        ctx (Context): The MCP context, which includes the lifespan context
        containing the MemCommerce API URL.

    Returns:
        Union[list[Color], CallToolResult]: A list of Color objects on success,
        or a CallToolResult indicating an API error.
    """
    api_url = ctx.request_context.lifespan_context.memcommerce_api_url

    try:
        colors = await get_all_colors(api_url)
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"MemCommerce API Error: {e}")],
        )

    return colors


@mcp.tool()
async def add_colors(
    colors_data: list[ColorData],
    ctx: Context[Any, AppContext],
) -> Union[list[Color], CallToolResult]:
    """
    Add one or more new product colors to the MemCommerce system.

    In MemCommerce, colors are used to define visual variants of a product
    (e.g., "Red", "Blue", "Black"), each associated with a hex color code
    for accurate representation in the UI. This tool allows agents or automation
    to create new color entries by providing structured color data.

    Args:
        colors_data (list[ColorData]): A list of ColorData objects, each containing
            a `name` (e.g., "Navy Blue") and a `hex` value (e.g., "#001F3F").

    Returns:
        Union[list[Color], CallToolResult]: A list of newly created Color objects on success,
        or a CallToolResult indicating an API error.
    """
    api_url = ctx.request_context.lifespan_context.memcommerce_api_url

    try:
        colors = await post_colors(colors_data, api_url)
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"MemCommerce API Error: {e}")],
        )

    return colors


@mcp.tool()
async def add_categories(
    categories_data: list[CategoryData],
    ctx: Context[Any, AppContext],
) -> Union[list[Category], CallToolResult]:
    """
    Add one or more new product categories to the MemCommerce system.

    In MemCommerce, categories are used to group products into collections
    like "Hats", "Jackets", or "Socks". Each category requires a name and
    an optional description. This tool allows agents or automation to create
    multiple categories at once by providing a list of structured category data.

    Args:
        categories_data (list[CategoryData]): A list of CategoryData objects, each containing
            a `name` and a `description`.

    Returns:
        Union[list[Category], CallToolResult]: A list of newly created Category objects on success,
        or a CallToolResult indicating an API error.
    """
    api_url = ctx.request_context.lifespan_context.memcommerce_api_url

    try:
        categories = await post_categories(categories_data, api_url)
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"MemCommerce API Error: {e}")],
        )

    return categories


@mcp.tool()
async def make_get_all_categories_request(
    ctx: Context[Any, AppContext],
) -> Union[list[Category], CallToolResult]:
    """
    Retrieve all available product categories from the MemCommerce API.

    In the MemCommerce system, categories represent high-level groupings of
    products such as "T-Shirts", "Shoes", or "Accessories". This data is used
    to organize products on the storefront and enables category-based navigation
    and filtering.

    Returns:
        Union[list[Category], CallToolResult]: A list of Category objects on success,
        or a CallToolResult indicating an API error.
    """
    api_url = ctx.request_context.lifespan_context.memcommerce_api_url

    try:
        categories = await get_all_categories(api_url)
    except MemCommerceAPIException as e:
        return CallToolResult(
            isError=True,
            content=[TextContent(type="text", text=f"MemCommerce API Error: {e}")],
        )

    return categories


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
