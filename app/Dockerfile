FROM python:3.11.7-slim

RUN addgroup --gid 10001 history_bot_user && \
    adduser --uid 10001 --gid 10001 --disabled-password --gecos "" history_bot_user

WORKDIR /usr/src/app

ENV PYTHONPATH=/usr/src/app/src

COPY /requirements/base.txt /requirements/

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install -U pip setuptools wheel && \
    pip install -r /requirements/base.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --chown=history_bot_user:history_bot_user . .

USER history_bot_user