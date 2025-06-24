FROM python:3.13.5-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN uv sync --locked

EXPOSE 8080

CMD ["uv", "run", "./src/admin_mcp_server/main.py", "--api-url", "https://be-memcommerce-667915768397.europe-west1.run.app"]