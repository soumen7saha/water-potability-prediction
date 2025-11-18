FROM python:3.10-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY ./src /app/src
COPY ./models /app/models
COPY ./templates /app/templates

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY .python-version pyproject.toml uv.lock ./

RUN uv sync --locked

COPY main.py ./
# COPY main.py src/scripts/predict.py models/model.bin ./

RUN uv sync --frozen

EXPOSE 9696

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9696"]

