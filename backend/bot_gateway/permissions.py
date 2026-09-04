from rest_framework.permissions import BasePermission

from bot_gateway.models import BotCustomer


class IsBotCustomer(BasePermission):
    def has_permission(self, request, view):
        return isinstance(getattr(request, "user", None), BotCustomer)
