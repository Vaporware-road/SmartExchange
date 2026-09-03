# Contact

> Source: [https://docs.aiogram.dev/en/latest/api/types/contact.html](https://docs.aiogram.dev/en/latest/api/types/contact.html)

*class* aiogram.types.contact.Contact(*\**, *phone_number: str*, *first_name: str*, *last_name: str | None = None*, *user_id: int | None = None*, *vcard: str | None = None*, *\*\*extra_data: Any*)
:   This object represents a phone contact.

    Source: <https://core.telegram.org/bots/api#contact>

    phone_number*: str*
    :   Contact’s phone number

    first_name*: str*
    :   Contact’s first name

    last_name*: str | None*
    :   *Optional*. Contact’s last name

    user_id*: int | None*
    :   *Optional*. Contact’s user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier

    vcard*: str | None*
    :   *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard)

    *property* full_name*: str*
