#!/bin/bash
python manage.py migrate
python manage.py loaddata kombucha_manager dev --no-color
python manage.py runserver 0.0.0.0:8000
