#!/bin/sh

PORT=${PORT:-8000}
HOST=${HOST:-0.0.0.0}

gunicorn --bind ${HOST}:${PORT} --workers $(nproc) bread.wsgi
