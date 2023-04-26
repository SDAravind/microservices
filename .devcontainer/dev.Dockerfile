FROM python:3.11-slim-bullseye

RUN apt update \
    && apt install -y make git
