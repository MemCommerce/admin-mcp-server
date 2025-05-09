from asyncio import gather

from api.common import safe_request
from schemas.color_schemas import ColorData, Color
from exceptions import MemCommerceAPIException


async def get_all_colors(base_url: str) -> list[Color]:
    url = f"{base_url}/colors/"
    data = await safe_request("GET", url)
    colors = [Color(**color) for color in data]
    return colors


async def post_colors(colors_data: list[ColorData], base_url: str) -> list[Color]:
    url = f"{base_url}/colors/"
    post_requests = [
        safe_request("POST", url, json=color_data.model_dump())
        for color_data in colors_data
    ]
    results = await gather(*post_requests)
    try:
        colors = [Color(**result) for result in results]
    except Exception as e:
        print(e)
        raise MemCommerceAPIException(f"Validation error {e}")

    return colors
