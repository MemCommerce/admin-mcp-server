from typing import Any

from httpx import AsyncClient, HTTPStatusError, RequestError

from exceptions import MemCommerceAPIException


async def safe_request(
    method: str,
    url: str,
    **kwargs: dict,
) -> Any:
    async with AsyncClient() as client:
        try:
            if method == "GET":
                response = await client.get(url, **kwargs)
            elif method == "POST":
                response = await client.post(url, **kwargs)
            else:
                raise ValueError(f"Unsupported method: {method}")

            response.raise_for_status()
            return response.json()

        except HTTPStatusError as e:
            raise MemCommerceAPIException(
                f"API error {e.response.status_code} at {url}: {e.response.text}"
            ) from e

        except RequestError as e:
            raise MemCommerceAPIException(
                f"Network error during request to {url}: {str(e)}"
            ) from e

        except Exception as e:
            raise MemCommerceAPIException(
                f"Unexpected error during request to {url}: {str(e)}"
            ) from e
