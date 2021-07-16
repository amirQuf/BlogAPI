#!/bin/bash

python3 -m venv venv
source venv/bin/activate
python3 manage.py makemigration
python3 manage.py migrate
python3 manage.py runserver
