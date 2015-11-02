# -*- coding: utf-8 -*-
PYTHON=env/bin/python

build:
	virtualenv -p /usr/bin/python3 env
	${PYTHON} -m pip install -r requirements.txt
	${PYTHON} manage.py makemigrations
	${PYTHON} manage.py migrate
	${PYTHON} manage.py compilemessages
	@${PYTHON} manage.py collectstatic 2>&- || :
	npm install

runserver:
	${PYTHON} manage.py runserver 0.0.0.0:8000
