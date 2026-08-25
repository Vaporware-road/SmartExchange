#!/usr/bin/env bash
# ──────────────────────────────────────────────────────────────
#  MrExchange — Development Helper
#
#  Usage:
#    ./dev.sh          — Start dev environment (builds first time)
#    ./dev.sh up       — Same as above
#    ./dev.sh down     — Stop and remove containers
#    ./dev.sh logs     — Tail logs from all services
#    ./dev.sh rebuild  — Force rebuild images and restart
#    ./dev.sh shell    — Open a bash shell in the app container
# ──────────────────────────────────────────────────────────────
set -euo pipefail

COMPOSE="docker compose -f docker-compose.dev.yml"
ACTION="${1:-up}"

case "$ACTION" in
  up|start)
    echo "🚀 Starting MrExchange dev environment..."
    echo "   Frontend (HMR):  http://localhost:5252"
    echo "   Backend API:     http://localhost:5252/api/"
    echo "   Django Admin:    http://localhost:5252/admin/"
    echo ""
    echo "   Login:  admin / admin"
    echo ""
    $COMPOSE up --build -d
    echo ""
    echo "✅ Dev environment running!"
    echo "   Edit files in ./backend or ./frontend — changes appear instantly."
    echo "   Frontend: Vite HMR (hot module replacement)"
    echo "   Backend:  Django runserver (auto-reload on file change)"
    ;;
  down|stop)
    echo "🛑 Stopping dev environment..."
    $COMPOSE down
    echo "✅ Stopped."
    ;;
  logs)
    $COMPOSE logs -f --tail=50
    ;;
  rebuild)
    echo "🔄 Rebuilding images and restarting..."
    $COMPOSE down
    $COMPOSE up --build -d
    echo "✅ Rebuilt and running."
    ;;
  shell)
    $COMPOSE exec app bash
    ;;
  *)
    echo "Usage: ./dev.sh [up|down|logs|rebuild|shell]"
    exit 1
    ;;
esac
