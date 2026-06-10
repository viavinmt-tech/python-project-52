.PHONY: build render-start

build:
	./build.sh

render-start:
	./.venv/bin/gunicorn task_manager.wsgi:application
