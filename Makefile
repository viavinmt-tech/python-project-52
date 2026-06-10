.PHONY: install migrate collectstatic render-start build

install:
	uv pip install -r requirements.txt

migrate:
	./.venv/bin/python manage.py migrate --noinput

collectstatic:
	./.venv/bin/python manage.py collectstatic --noinput

render-start:
	./.venv/bin/python manage.py migrate --noinput
	./.venv/bin/python manage.py collectstatic --noinput
	./.venv/bin/gunicorn task_manager.wsgi:application

build:
	./build.sh
