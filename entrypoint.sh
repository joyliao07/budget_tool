#! /bin/bash

set -e

cd /src

coverage run --source='.' manage.py test -v 2
coverage report
python3 manage.py makemigrations --noinput  # flask migrate
python3 manage.py migrate --noinput  # flask upgrade
python3 manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:8000
