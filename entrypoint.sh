#! /bin/bash

set -e

cd /src

python3 manage.py test -v 2 && \
python3 manage.py makemigrations --noinput  # flask migrate
python3 manage.py migrate --noinput  # flask upgrade
python3 manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:8000
