#!/bin/sh
cd myproject
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn --bind 0.0.0.0:80 myproject.wsgi:application
cd ..