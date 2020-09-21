#!/bin/sh

# collect the static files
echo "collecting the static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying the database migrations"
python manage.py makemigrations

python manage.py migrate

# Start server
echo "Starting the server on port 8000"
gunicorn pay_me_in_doge.wsgi:application --workers=3 --bind 0.0.0.0:8000
