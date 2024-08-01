FROM python:3.12-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV="/opt/.venv"
ENV PATH="/opt/venv/bin:$PATH"
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_NO_INTERACTION=1
ENV POETRY_CACHE_DIR="/tmp/poetry_cache"

ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

FROM base as builder

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    curl=7.* \
    && curl -sSL https://install.python-poetry.org | python - \
    && poetry --version \
    && apt-get clean -y

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN python3 -m venv "$VIRTUAL_ENV" && poetry install && rm -rf "$POETRY_CACHE_DIR"

COPY . ./
RUN chmod +x "entrypoint.sh"


FROM builder as development

WORKDIR /app

RUN poetry install && rm -rf "$POETRY_CACHE_DIR"

CMD ["/bin/bash", "entrypoint.sh"]


FROM builder as production


CMD ["/bin/bash", "entrypoint.sh"]
