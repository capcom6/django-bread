# Copyright 2022 Aleksandr Soloshenko
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM python:3.9-alpine AS base

# RUN apk update && apk add mysql-client

FROM base AS build

# We need to build cffi, so we will use multi-stage build
RUN apk update && apk add --no-cache \
    gcc \
    libc-dev \
    make \
    git \
    libffi-dev \
    openssl-dev \
    python3-dev \
    libxml2-dev \
    libxslt-dev \
    mariadb-connector-c-dev \
    jpeg-dev

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

#################################
FROM base AS prod

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && apk add --no-cache \
    mariadb-connector-c-dev \
    libjpeg-turbo-dev

RUN pip install gunicorn

COPY --from=build /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY . .

USER guest

EXPOSE 8000

# CMD ["gunicorn", "-R", "-b", "0.0.0.0:8000", "bread.wsgi"]
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["./bin/migrate_run.sh"]

FROM base AS dev

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && apk add --no-cache \
    mariadb-connector-c-dev \
    libjpeg-turbo-dev

COPY --from=build /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

USER guest

VOLUME [ "/app" ]
EXPOSE 8000

# CMD ["gunicorn", "-R", "-b", "0.0.0.0:8000", "bread.wsgi"]
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["./bin/migrate_run.sh"]
