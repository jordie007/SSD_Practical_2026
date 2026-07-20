#!/bin/sh
set -e

if [ ! -d "/app/.git" ]; then
    git init
    git add .
    git commit -m "Initial commit" || true
fi

exec python app.py
