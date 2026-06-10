.PHONY: install migrate collectstatic render-start build

PYTHON = /opt/render/project/python/Python-3.12.13/bin/python3.12

install:
	uv pip install --system -r requirements.txt

migrate:
	$(PYTHON) manage.py migrate

collectstatic:
	$(PYTHON) manage.py collectstatic --noinput

render-start:
	gunicorn task_manager.wsgi:application

build:
	./build.sh
