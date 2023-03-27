#!/bin/bash

cd /app/src

python manage.py migrate

if [[ $ENVIRONMENT = "dev" ]]
then
    gunicorn -w 8 -b '0.0.0.0:8000' --forwarded-allow-ips="*" --timeout 500 backend_creditcard.wsgi --reload
else
    gunicorn -w 16 -b '0.0.0.0:8000' --forwarded-allow-ips="*" --timeout 500 backend_creditcard.wsgi
fi