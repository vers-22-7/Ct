FROM python:3.13-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY . /app
RUN rm -rf /app/.venv
WORKDIR /app
RUN uv sync --frozen --no-cache
EXPOSE 80
ENV PYTHONPATH=src
CMD ["/app/.venv/bin/fastapi", "run", "src/main.py", "--port", "80", "--host", "0.0.0.0"]
