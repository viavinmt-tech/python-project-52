#!/usr/bin/env bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
