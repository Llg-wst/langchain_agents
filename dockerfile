FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /ai_agents_lch

COPY pyproject.toml ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system --no-cache

COPY . .

CMD ["uv", "run","main.py"]