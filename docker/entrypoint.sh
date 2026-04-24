#!/bin/sh
set -e

mkdir -p /app/backend/data /app/backend/public/media /app/backend/public/staticfiles

cd /app/backend
python manage.py migrate --noinput
python manage.py ensure_default_admin

python manage.py runserver 0.0.0.0:8000 &
DJANGO_PID=$!

cd /app/frontend
npm run dev -- --host 0.0.0.0 --port 5173 &
VITE_PID=$!

shutdown() {
  kill "$DJANGO_PID" "$VITE_PID" 2>/dev/null || true
  wait "$DJANGO_PID" 2>/dev/null || true
  wait "$VITE_PID" 2>/dev/null || true
}

trap shutdown INT TERM

while kill -0 "$DJANGO_PID" 2>/dev/null && kill -0 "$VITE_PID" 2>/dev/null; do
  sleep 1
done

shutdown
exit 1
