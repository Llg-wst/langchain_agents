# Use official uv image instead of installing uv via pip
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /ai_agents_lch

# Copy just dependency files first
COPY pyproject.toml ./

# Install dependencies with cache mount
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system --no-cache .

# Copy the rest of the application code
COPY . . 

# Command to run the application
CMD ["uv", "run", "python","main.py"]