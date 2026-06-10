.PHONY: install migrate collectstatic render-start build

VENV = .venv

install:
	uv venv --clear
	uv pip install --python $(VENV)/bin/python -r requirements.txt

migrate:
	$(VENV)/bin/python manage.py migrate

collectstatic:
	$(VENV)/bin/python manage.py collectstatic --noinput

render-start:
	$(VENV)/bin/gunicorn task_manager.wsgi:application

build:
	./build.sh
