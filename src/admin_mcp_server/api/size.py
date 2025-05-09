from asyncio import gather

from api.common import safe_request
from schemas.size_schemas import SizeData, Size
from exceptions import MemCommerceAPIException


async def get_all_sizes(base_url: str) -> list[Size]:
    url = f"{base_url}/sizes/"
    data = await safe_request("GET", url)
    sizes = [Size(**size) for size in data]
    return sizes


async def post_sizes(sizes_data: list[SizeData], base_url: str) -> list[Size]:
    url = f"{base_url}/sizes/"
    post_requests = [
        safe_request("POST", url, json=size_data.model_dump())
        for size_data in sizes_data
    ]
    results = await gather(*post_requests)
    try:
        sizes = [Size(**result) for result in results]
    except Exception as e:
        print(e)
        raise MemCommerceAPIException(f"Validation error {e}")

    return sizes
