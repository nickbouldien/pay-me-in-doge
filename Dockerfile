FROM python:3.7-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

COPY ./requirements.txt .

# update and install deps
RUN apk update \
     && apk add --no-cache postgresql-libs \
     && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev jpeg-dev zlib-dev libjpeg \
     && pip install -r requirements.txt --no-cache-dir  \
     && apk --purge del .build-deps

# copy project files
COPY . .

# add and run as a non-root user
RUN adduser -D appuser
USER appuser

# run gunicorn
CMD gunicorn pay_me_in_doge.wsgi:application --bind 0.0.0.0:$PORT
