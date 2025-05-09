import argparse
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass

from mcp.server.fastmcp import FastMCP


@dataclass
class AppContext:
    memcommerce_api_url: str


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    parser = argparse.ArgumentParser(
        description="MCP app for MemCommerce Admin operations."
    )
    parser.add_argument(
        "--api-url", dest="api_url", help="The API URL of MemCommerce Backend."
    )
    args = parser.parse_args()

    if not args.api_url:
        raise Exception("The --api-url arg was not provided!")

    yield AppContext(memcommerce_api_url=args.api_url)


mcp = FastMCP("MemCommerce Admin MCP server", lifespan=app_lifespan)
