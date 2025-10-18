
#!/usr/bin/env bash

echo "Construyendo aplicación..."
python3 -m pip install -r requirements.txt

echo "Migrando Base de Datos..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Recopilando archivos estáticos..."
python3 manage.py collectstatic --noinput
