#!/bin/sh

docker buildx build --platform linux/amd64,linux/arm64 -f ./package/Dockerfile --target=prod -t capcom6/django-bread:${1} --push .
