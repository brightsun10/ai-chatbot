#!/bin/bash
python manage.py migrate --noinput
python manage.py makemigrations chatbot
python manage.py collectstatic --noinput
exec gunicorn dashboard.wsgi:application --bind 0.0.0.0:$PORT
