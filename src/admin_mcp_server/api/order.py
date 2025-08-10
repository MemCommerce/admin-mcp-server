from api.common import safe_request
from schemas.order_schemas import Order


async def get_orders(
    base_url: str,
    page: int = 1,
    limit: int = 10,
    status: str | None = None,
) -> list[Order]:
    url = f"{base_url}/orders/"
    params = {"page": page, "limit": limit}
    if status is not None:
        params["status"] = status
    data = await safe_request("GET", url, params=params)
    items = data["items"] if isinstance(data, dict) and "items" in data else data
    return [Order(**order) for order in items]


async def mark_order_delivered(order_id: str, base_url: str) -> Order:
    url = f"{base_url}/orders/{order_id}/delivered"
    data = await safe_request("PATCH", url)
    return Order(**data)
