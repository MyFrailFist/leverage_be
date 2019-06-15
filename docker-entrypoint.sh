#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
#python manage.py collectstatic --noinput
gunicorn main_app.wsgi -c ./conf/gunicorn.ini