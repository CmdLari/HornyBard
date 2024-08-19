# syntax=docker/dockerfile:1
# Build steps
FROM python:3.11.9-alpine3.20 as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install native dependencies
RUN apk update && apk add gcc python3-dev musl-dev linux-headers pcre-dev

# install dependencies
RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# Final image
FROM python:3.11.9-alpine3.20

ENV APP_HOME=/home/discord/app
ENV UID=990
ENV GID=990
RUN apk add --no-cache pcre su-exec && \
    addgroup -g $GID -S discord && adduser -u $UID -S discord -G discord && \
    mkdir -p $APP_HOME

WORKDIR $APP_HOME

RUN --mount=type=bind,from=builder,source=/usr/src/app/wheels,target=/wheels \
    pip install --no-cache /wheels/*

COPY hornyBard.py .
COPY docker-entrypoint.sh .

ENTRYPOINT ["/home/discord/app/docker-entrypoint.sh"]
