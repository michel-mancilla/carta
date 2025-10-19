#!/usr/bin/env bash

# 1. Instalación de Node y Construcción de Frontend
echo "-> Instalando dependencias de Node..."
# Instala Tailwind (la única dependencia de Node)
npm install

# Ejecuta el script 'build' recién añadido del package.json para generar el CSS final.
echo "-> Ejecutando npm run build para compilar CSS..."
npm run build 

# 2. Instalación de Python
echo "-> Instalando dependencias de Python..."
# Aquí se asegura la instalación de Django, Gunicorn, Whitenoise, etc.
pip install -r requirements.txt

# 3. Recolección de Archivos Estáticos de Django
# Esto recoge el CSS generado en el paso 1 junto con los estáticos de Django.
echo "-> Recolectando archivos estáticos de Django..."
python manage.py collectstatic --noinput --clear