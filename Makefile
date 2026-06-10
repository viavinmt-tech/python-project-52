.PHONY: install migrate collectstatic render-start build

install:
	uv pip install -r requirements.txt

migrate:
	uv run --no-project python manage.py migrate

collectstatic:
	uv run --no-project python manage.py collectstatic --noinput

render-start:
	uv run --no-project gunicorn task_manager.wsgi:application

build:
	./build.sh
