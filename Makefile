.PHONY: install migrate collectstatic render-start build lint test-coverage

install:
	uv sync

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

render-start:
	uv run gunicorn task_manager.wsgi:application

build:
	./build.sh

lint:
	uv run ruff check task_manager --fix

test-coverage:
	uv run coverage run manage.py test
	uv run coverage xml
