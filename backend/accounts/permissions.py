"""
Role-Based Access Control (RBAC) for the panel.

Roles (see accounts.models.CustomUser.ROLE_*):
- SUPER_ADMIN (super_admin): Full access to all endpoints.
- MANAGEMENT (management): Instagram Hub, Telegram Channels, Price Hub (read/write),
  Finalize, Analysis. No access to User Management or Site Settings.
- EMPLOYEE (employee): Read-only access to Price Hub and Dashboard (Finalize dashboard,
  Analysis). No access to Telegram Setup, Instagram Hub configuration, or Finalizing prices.

Permission mapping:
- User Management (list/create/update users, force logout, activity logs): IsSuperAdmin
- Site Settings (site settings, bots, channels, logs): IsSuperAdmin
- Instagram Hub (preview, status, config): IsSuperAdminOrManagement
- Finalize (dashboard read): IsAuthenticated; (category/special/all finalize): IsSuperAdminOrManagement
- Price Hub (list/detail/history): IsAuthenticated; (update/bulk-update): IsSuperAdminOrManagement
- Telegram app (channels, send message, bots, auto-post): IsSuperAdminOrManagement
- Analysis dashboard: IsAuthenticated

Frontend permission config: frontend/src/config/permissions.js
"""
import logging

from rest_framework import permissions

logger = logging.getLogger(__name__)


class IsSuperAdmin(permissions.BasePermission):
    """
    Allows access only to users with role super_admin.
    Used for User Management API and Site Settings.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            logger.info(
                "IsSuperAdmin: denied (user=%s, authenticated=%s)",
                getattr(request.user, "username", None) if request.user else None,
                getattr(request.user, "is_authenticated", False) if request.user else False,
            )
            return False
        role = getattr(request.user, "role", None)
        allowed = role == "super_admin"
        logger.info(
            "IsSuperAdmin: user=%s role=%r allowed=%s",
            request.user.username,
            role,
            allowed,
        )
        return allowed


class IsSuperAdminOrManagement(permissions.BasePermission):
    """
    Allows access only to users with role super_admin or management.
    Used for: Instagram Hub, Telegram setup/channels, Finalize actions,
    Price Hub write (update/bulk-update), Template editor.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            logger.info(
                "IsSuperAdminOrManagement: denied (user=%s, authenticated=%s)",
                getattr(request.user, "username", None) if request.user else None,
                getattr(request.user, "is_authenticated", False) if request.user else False,
            )
            return False
        role = getattr(request.user, "role", None)
        allowed = role in ("super_admin", "management")
        logger.info(
            "IsSuperAdminOrManagement: user=%s role=%r allowed=%s",
            request.user.username,
            role,
            allowed,
        )
        return allowed
