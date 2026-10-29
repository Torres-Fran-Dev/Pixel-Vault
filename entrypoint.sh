#!/bin/sh

echo "Ejecutando migraciones..."
python manage.py migrate --noinput

echo "Cargando los juegos oficiales..."
python manage.py cargar_juegos

echo "Iniciando el servidor de Pixel-Vault..."
exec "$@"