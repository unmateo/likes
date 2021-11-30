#!make
include .env
export $(shell sed 's/=.*//' .env)

.DEFAULT_GOAL := help

help:
	make --help

db-update:
	python manage.py makemigrations

db-migrate:
	python manage.py migrate

db-reset:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	rm db.sqlite3

create-super-user:
	python manage.py createsuperuser --username $(SUPERUSER_USERNAME) --email $(SUPERUSER_EMAIL) 

up:
	python manage.py runserver
