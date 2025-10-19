#!/usr/bin/env bash

# 1. Instalación de Python y Dependencias
echo "-> Instalando dependencias de Python..."
pip install -r requirements.txt

# 2. Recolección de Archivos Estáticos
echo "-> Recolectando archivos estáticos de Django..."
python manage.py collectstatic --noinput --clear