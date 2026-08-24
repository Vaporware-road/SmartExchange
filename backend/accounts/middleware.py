from django.conf import settings
from django.shortcuts import redirect


class LoginRequiredMiddleware:
    """Redirect anonymous users to login for Django admin only.

    API endpoints are deliberately exempt: DRF permission classes (AllowAny,
    IsAuthenticated, IsSuperAdminOrManagement, ...) own authentication there and
    return proper 401/403 responses. A redirect would turn every unauthenticated
    API call into a 302 to the SPA login page, breaking both the panel's clients
    and the public prices API. SPA routes are handled by the frontend router.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL

    def __call__(self, request):
        path = request.path_info
        if not request.user.is_authenticated:
            needs_auth = path.startswith('/admin/')
            if needs_auth:
                return redirect(self.login_url)
        return self.get_response(request)
