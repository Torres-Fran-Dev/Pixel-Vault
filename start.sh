#!/usr/bin/env bash
# Salir inmediatamente si hay un error
set -o errexit

python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Arrancar Gunicorn usando la carpeta core que descubrimos antes
gunicorn core.wsgi:application --bind 0.0.0.0:8000