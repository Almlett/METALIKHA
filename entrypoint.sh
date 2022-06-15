#!/bin/sh


python manage.py makemigrations
python manage.py migrate
yes|python manage.py collectstatic
exec "$@"