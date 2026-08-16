"""aiogram routers for SmartExchange customer bot."""

from __future__ import annotations

from aiogram import Router

from . import alerts, bridge, exchange, menu, profile, start


def build_root_router() -> Router:
    root = Router(name="customer_root")
    root.include_router(start.create_router())
    root.include_router(menu.create_router())
    root.include_router(profile.create_router())
    root.include_router(exchange.create_router())
    root.include_router(alerts.create_router())
    root.include_router(bridge.create_router())
    return root
