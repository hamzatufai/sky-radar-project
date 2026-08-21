#!/usr/bin/env sh
set -eu
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt --timeout 120 --retries 5
echo "Setup complete. Next run: source .venv/bin/activate"
