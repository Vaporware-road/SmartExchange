from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from .trial import trial_is_expired


class TrialAccessMiddleware(MiddlewareMixin):
    """Fail closed for expired customer trials before protected API work runs."""

    def process_view(self, request, view_func, view_args, view_kwargs):
        user = getattr(request, "user", None)
        path = request.path or ""
        if (
            user
            and user.is_authenticated
            and trial_is_expired(user)
            and path.startswith("/api/")
            and not path.startswith(("/api/auth/", "/api/public/"))
        ):
            return JsonResponse(
                {
                    "error": True,
                    "message": "Your 14-day free trial has expired. Please contact an administrator to upgrade your plan.",
                    "code": "trial_expired",
                },
                status=403,
            )
        return None


class LoginRequiredMiddleware(MiddlewareMixin):
    """Existing compatibility middleware; public/API auth views remain exempt."""

    PUBLIC_PREFIXES = ("/login", "/landingpage/", "/landing/", "/static/", "/media/", "/api/auth/", "/api/public/")

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith(self.PUBLIC_PREFIXES):
            return None
        return None
