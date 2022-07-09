#!/bin/sh

PORT=${PORT:-8000}
HOST=${HOST:-0.0.0.0}

make init-dev && \
    python3 manage.py migrate && \
    python3 manage.py runserver ${HOST}:${PORT}
