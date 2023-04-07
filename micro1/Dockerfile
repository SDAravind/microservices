ARG PYIMAGE=python:3.11-alpine3.17
FROM ${PYIMAGE} as build

WORKDIR /tmp

COPY ["pyproject.toml", "./"]
RUN pip install poetry \
    && poetry config virtualenvs.in-project true \
    && poetry install --without dev

FROM ${PYIMAGE} as production

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY --from=build /tmp/.venv ./.venv
COPY . .

CMD ["python", "main.py"]
