from asyncio import gather

from api.common import safe_request
from schemas.category_schemas import CategoryData, Category
from exceptions import MemCommerceAPIException


async def get_all_categories(base_url: str) -> list[Category]:
    url = f"{base_url}/categories/"
    data = await safe_request("GET", url)
    categories = [CategoryData(**category) for category in data]
    return categories


async def post_categories(categories_data: list[CategoryData], base_url: str) -> list[Category]:
    url = f"{base_url}/categories/"
    post_requests = [
        safe_request("POST", url, json=category_data.model_dump())
        for category_data in categories_data
    ]
    results = await gather(*post_requests)
    try:
        categories = [Category(**result) for result in results]
    except Exception as e:
        print(e)
        raise MemCommerceAPIException(f"Validation error {e}")

    return categories
