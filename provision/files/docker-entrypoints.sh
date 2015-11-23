#!/bin/bash

python manage.py bower install --no-color
python manage.py compress --force
python manage.py collectstatic --no-color --noinput
python manage.py migrate
python manage.py loaddata kombucha_manager/fixtures/dev.json --no-color
python manage.py test
honcho start
