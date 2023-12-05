FROM python:3.10-bookworm

WORKDIR /TextRecognition
COPY ./poetry.lock ./pyproject.toml ./


ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
    && apt-get upgrade -y

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .