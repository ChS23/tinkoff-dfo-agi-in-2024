FROM python:3.12.2-slim-bullseye

WORKDIR /app

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN pip install --no-cache-dir poetry

COPY pyproject.toml /app/pyproject.toml

RUN poetry install

COPY . /app/api

CMD ["poetry", "run", "python", "-m", "api"]
