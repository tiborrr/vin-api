# First, build the application in the `/app` directory
FROM ghcr.io/astral-sh/uv:alpine AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Omit development dependencies by default
ARG UV_NO_DEV=1
ENV UV_NO_DEV=$UV_NO_DEV

# Configure the Python directory so it is consistent
ENV UV_PYTHON_INSTALL_DIR=/python

# Only use the managed Python version
ENV UV_PYTHON_PREFERENCE=only-managed

# Install Python before the project for caching
RUN uv python install 3.14

WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

# Then, use a final image without uv
FROM alpine:edge

# Install postgresql-client for pg_restore and cleanup
RUN apk update && apk add --no-cache postgresql18-client

# Setup a non-root user
# Using 10001 as the ID because 999 is commonly used by ping group in Alpine
RUN addgroup -g 10001 -S nonroot && \
    adduser -u 10001 -S nonroot -G nonroot -h /home/nonroot

# Copy the Python version
COPY --from=builder /python /python

# Copy the application from the builder
COPY --from=builder --chown=nonroot:nonroot /app /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Use the non-root user to run our application
USER nonroot

# Use `/app` as the working directory
WORKDIR /app

# Run the FastAPI application by default
CMD ["uvicorn", "vin_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
