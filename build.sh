#!/usr/bin/env bash

# Solo Python
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear