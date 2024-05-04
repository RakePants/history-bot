FROM python:3.11.7-slim

RUN addgroup --gid 10001 embedding_user && \
    adduser --uid 10001 --gid 10001 --disabled-password --gecos "" embedding_user

WORKDIR /usr/src/embedding_model

ENV PYTHONPATH=/usr/src/embedding_model/src

COPY /requirements/base.txt /requirements/

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install -r /requirements/base.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --chown=embedding_user:embedding_user . .

USER embedding_user