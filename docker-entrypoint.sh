#!/bin/sh

# collect the static files
echo "collecting the static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying the database migrations"
python manage.py makemigrations

python manage.py migrate

# Start server
echo "Starting the server on port: $PORT"
#python manage.py runserver 0.0.0.0:8000
gunicorn pay_me_in_doge.wsgi:application --bind 0.0.0.0:8000