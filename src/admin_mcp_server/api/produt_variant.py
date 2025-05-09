from asyncio import gather

from api.common import safe_request
from schemas.product_variant_schemas import ProductVariantData, ProductVariant
from exceptions import MemCommerceAPIException


async def get_all_pvs(base_url: str) -> list[ProductVariant]:
    url = f"{base_url}/product-variants/"
    data = await safe_request("GET", url)
    product_variants = [ProductVariant(**pv) for pv in data]
    return product_variants


async def post_pvs(
    pvs_data: list[ProductVariantData], base_url: str
) -> list[ProductVariant]:
    url = f"{base_url}/product-variants/"
    post_requests = [
        safe_request("POST", url, json=pv_data.model_dump()) for pv_data in pvs_data
    ]
    results = await gather(*post_requests)
    try:
        product_variants = [ProductVariant(**result) for result in results]
    except Exception as e:
        print(e)
        raise MemCommerceAPIException(f"Validation error {e}")

    return product_variants
