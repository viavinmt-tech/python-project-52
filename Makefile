.PHONY: install migrate collectstatic render-start build lint test test-coverage

install:
	uv pip install --system -r pyproject.toml
	uv pip install --system coverage

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic --noinput

render-start:
	gunicorn task_manager.wsgi:application

build:
	./build.sh

lint:
	ruff check task_manager

test:
	python manage.py test

test-coverage:
	coverage run manage.py test
	coverage xml
