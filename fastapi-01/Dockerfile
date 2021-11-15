# base
FROM python:3.9-alpine AS base
RUN pip install --upgrade pip

# poetry requirement
FROM python:3.9 AS requirement
RUN pip install --upgrade pip

RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* ./

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# venv builder
FROM base AS builder

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY --from=requirement /requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# development
FROM base AS development

COPY --from=builder /opt/venv /opt/venv

ENV PYTHONPATH=/app:/opt/venv
ENV PATH=/opt/venv/bin/:$PATH

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY src /src
WORKDIR /src

# RUN useradd appuser && chown -R appuser /src
# USER appuser

EXPOSE 8000
