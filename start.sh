#!/usr/bin/env bash
set -o errexit

python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Carga automática de los 18 juegos oficiales de Pixel-Vault
python manage.py cargar_juegos

# Crea un superusuario automáticamente si no existe
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'tucontraseña123')"

# Arrancar Gunicorn
gunicorn core.wsgi:application --bind 0.0.0.0:8000