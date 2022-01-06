#!make
include .env
export $(shell sed 's/=.*//' .env)

.DEFAULT_GOAL := help

help:
	make --help

db-clean:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	rm db.sqlite3

db-check:
	python manage.py makemigrations

db-migrate:
	python manage.py migrate

db-restore: db-clean db-check db-migrate

create-super-user:
	python manage.py createsuperuser

up:
	python manage.py runserver

test:

	python manage.py test tests/

import:
	python manage.py import $(FILENAME)
