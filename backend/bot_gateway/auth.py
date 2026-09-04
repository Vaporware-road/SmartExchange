from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from bot_gateway.services.auth_tokens import get_customer_from_token


class BotCustomerAuthentication(BaseAuthentication):
    """Authenticate bot customers via short-lived JWT (not staff tokens)."""

    keyword = "Bearer"

    def authenticate(self, request):
        auth = request.headers.get("Authorization", "")
        if not auth.startswith(f"{self.keyword} "):
            return None
        token = auth[len(self.keyword) + 1 :].strip()
        if not token:
            return None
        customer = get_customer_from_token(token)
        if not customer:
            raise AuthenticationFailed("Invalid or expired bot token")
        return (customer, token)
