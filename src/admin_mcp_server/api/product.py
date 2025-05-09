from asyncio import gather

from api.common import safe_request
from schemas.product_schemas import ProductData, Product
from exceptions import MemCommerceAPIException


async def get_all_products(base_url: str) -> list[Product]:
    url = f"{base_url}/products/"
    data = await safe_request("GET", url)
    products = [Product(**product) for product in data]
    return products


async def post_products(
    products_data: list[ProductData], base_url: str
) -> list[Product]:
    url = f"{base_url}/products/"
    post_requests = [
        safe_request("POST", url, json=product_data.model_dump())
        for product_data in products_data
    ]
    results = await gather(*post_requests)
    try:
        products = [Product(**result) for result in results]
    except Exception as e:
        print(e)
        raise MemCommerceAPIException(f"Validation error {e}")

    return products
