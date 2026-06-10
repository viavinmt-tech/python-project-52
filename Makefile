.PHONY: install migrate collectstatic render-start build

install:
	uv pip install -r requirements.txt

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

render-start:
	uv run gunicorn task_manager.wsgi:application

build:
	./build.sh
