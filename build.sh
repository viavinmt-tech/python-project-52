#!/usr/bin/env bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

uv venv
uv pip install -r requirements.txt
./.venv/bin/python manage.py collectstatic --noinput
./.venv/bin/python manage.py migrate --noinput
