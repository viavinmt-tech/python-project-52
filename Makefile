.PHONY: install migrate collectstatic render-start build

render-start:
	gunicorn task_manager.wsgi:application

build:
	./build.sh
