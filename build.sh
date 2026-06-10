#!/usr/bin/env bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

uv pip install -r requirements.txt
