from api.common import safe_request


async def get_all_sizes(base_url):
    url = f"{base_url}/sizes/"
    return await safe_request("GET", url)
