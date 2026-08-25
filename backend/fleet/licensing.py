"""License keys for MrExchange installations.

A license key identifies one install to the owner panel. It is a bearer
identifier, not a secret that protects customer data: the only thing it grants
is the ability to POST non-sensitive metadata to the fleet check-in endpoint.
It is stored in the clear because the owner has to be able to read it back and
hand it to the customer during onboarding or a reissue.
"""

import secrets
import string

PREFIX = "MREX"
GROUPS = 4
GROUP_LEN = 4
# Crockford-style alphabet: no I/O/0/1, so a key read aloud or copied off an
# invoice does not come back wrong.
ALPHABET = "".join(c for c in string.ascii_uppercase + string.digits if c not in "IO01")


def generate_license_key():
    groups = (
        "".join(secrets.choice(ALPHABET) for _ in range(GROUP_LEN))
        for _ in range(GROUPS)
    )
    return "-".join([PREFIX, *groups])


def normalize_license_key(value):
    return str(value or "").strip().upper()
