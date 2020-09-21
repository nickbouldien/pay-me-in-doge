FROM python:3.7-alpine

WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

COPY ./requirements.txt /code

# update and install deps
RUN apk update \
     && apk add --no-cache postgresql-libs \
     && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev jpeg-dev zlib-dev libjpeg \
     && pip install -r requirements.txt --no-cache-dir  \
     && apk --purge del .build-deps

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# copy project files
COPY . /code/

# add and run as a non-root user
RUN adduser -D appuser
USER appuser

ENTRYPOINT ["/docker-entrypoint.sh"]
