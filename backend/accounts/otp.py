"""Issue and check the six-digit codes used to prove an address or a number.

Email is the primary channel because every signup has one; SMS is the fallback
for an account that only gave a phone. The code itself never touches the
database or a log line — only its hash — so the delivery function is the single
place it exists in clear text.
"""
import logging
import secrets

from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

from .models import OtpCode
from .sms import send_sms

logger = logging.getLogger(__name__)


def _generate_code():
    """A uniformly random code with its leading zeros intact."""
    upper = 10 ** OtpCode.CODE_LENGTH
    return str(secrets.randbelow(upper)).zfill(OtpCode.CODE_LENGTH)


def choose_channel(user):
    """Email when there is one, otherwise SMS; ``None`` when neither works."""
    if (user.email or "").strip():
        return OtpCode.CHANNEL_EMAIL
    if (user.phone or "").strip():
        return OtpCode.CHANNEL_SMS
    return None


def issue_code(user, purpose=OtpCode.PURPOSE_VERIFY_EMAIL):
    """Send a fresh code and return ``(otp, delivered)``.

    Any code still outstanding for the same purpose is retired first, so the
    most recent message is always the one that works and an old screenshot is
    not a second key.
    """
    channel = choose_channel(user)
    if channel is None:
        return None, False

    now = timezone.now()
    OtpCode.objects.filter(
        user=user, purpose=purpose, consumed_at__isnull=True
    ).update(consumed_at=now)

    code = _generate_code()
    destination = (
        user.email.strip() if channel == OtpCode.CHANNEL_EMAIL else user.phone.strip()
    )
    otp = OtpCode.objects.create(
        user=user,
        purpose=purpose,
        code_hash=make_password(code),
        sent_to=destination,
        channel=channel,
        expires_at=now + timezone.timedelta(seconds=OtpCode.TTL_SECONDS),
    )
    return otp, _deliver(user, otp, code)


def _deliver(user, otp, code):
    minutes = OtpCode.TTL_SECONDS // 60
    if otp.channel == OtpCode.CHANNEL_SMS:
        return send_sms(otp.sent_to, f"{code} is your MrExchange code. It expires in {minutes} minutes.")

    context = {"user": user, "code": code, "minutes": minutes}
    try:
        message = EmailMultiAlternatives(
            subject=render_to_string("accounts/email/otp_subject.txt", context).strip(),
            body=render_to_string("accounts/email/otp_body.txt", context),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[otp.sent_to],
        )
        message.attach_alternative(
            render_to_string("accounts/email/otp_body.html", context), "text/html"
        )
        message.send(fail_silently=False)
        return True
    except Exception:
        # No code in the log line: this is the one place it exists in clear text.
        logger.exception("otp: could not email the code to user %s", user.pk)
        return False


def verify_code(user, code, purpose=OtpCode.PURPOSE_VERIFY_EMAIL):
    """``(ok, reason)`` — ``reason`` is a stable code for the client on failure."""
    otp = (
        OtpCode.objects.filter(user=user, purpose=purpose, consumed_at__isnull=True)
        .order_by("-created_at")
        .first()
    )
    if otp is None:
        return False, "otp_not_requested"
    if otp.expires_at <= timezone.now():
        return False, "otp_expired"
    if otp.attempts >= OtpCode.MAX_ATTEMPTS:
        return False, "otp_too_many_attempts"

    submitted = (code or "").strip()
    if not check_password(submitted, otp.code_hash):
        otp.attempts += 1
        otp.save(update_fields=["attempts"])
        return False, "otp_invalid"

    otp.consumed_at = timezone.now()
    otp.save(update_fields=["consumed_at"])
    return True, ""
