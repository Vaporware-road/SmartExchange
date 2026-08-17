from rest_framework_simplejwt.tokens import RefreshToken


def issue_tokens_for_user(user, impersonator=None):
    refresh = RefreshToken.for_user(user)
    refresh.access_token["token_version"] = getattr(user, "token_version", 0)
    if impersonator is not None:
        refresh["impersonator_id"] = impersonator.id
        refresh["impersonator_username"] = impersonator.username
        refresh.access_token["impersonator_id"] = impersonator.id
        refresh.access_token["impersonator_username"] = impersonator.username
    return refresh
