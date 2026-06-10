.PHONY: install migrate collectstatic render-start build

install:
	uv pip install --system -r requirements.txt

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic --noinput

render-start:
	gunicorn task_manager.wsgi:application

build:
	./build.sh
