## GLOBAL VARIABLES #################################################
ARG PYIMAGE=python:3.11-alpine3.17
# ARG PYIMAGE=python:3.11-slim-bullseye

#####################################################################
FROM ${PYIMAGE} as build

WORKDIR /tmp

COPY [ "pyproject.toml", "./" ]
RUN pip install poetry \
    && poetry config virtualenvs.options.always-copy true \
    && poetry config virtualenvs.in-project true \
    && poetry install --without dev

#####################################################################
# FROM python:python:3.11-slim-bullseye as production
FROM ${PYIMAGE} as production

ARG USERNAME=debian
ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app

COPY --from=build /tmp/.venv ./.venv
COPY . .

# ADD NON ROOT USER ON DEBIAN
# RUN useradd -m ${USERNAME} \
# && rm /bin/sh /bin/echo /bin/rm \
# && rm /bin/*


# ADD NON ROOT USER ON ALPINE
RUN adduser -D ${USERNAME} \
    # && rm /bin/sh /bin/bash /bin/echo /bin/rm \
    && rm /bin/*

USER ${USERNAME}

CMD [ "python", "main.py" ]
