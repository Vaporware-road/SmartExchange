from celery import shared_task
from django.utils import timezone


@shared_task
def expire_trials_task():
    from .models import CustomUser

    now = timezone.now()
    users = CustomUser.objects.filter(
        is_active=True,
        trial_expires_at__isnull=False,
        trial_expires_at__lte=now,
    ).exclude(role=CustomUser.ROLE_SUPER_ADMIN).exclude(is_superuser=True)
    count = users.update(is_active=False, trial_expiry_notified_at=now)
    return {"deactivated": count}
