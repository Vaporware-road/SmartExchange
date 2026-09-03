# InputContactMessageContent

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_contact_message_content.html](https://docs.aiogram.dev/en/latest/api/types/input_contact_message_content.html)

*class* aiogram.types.input_contact_message_content.InputContactMessageContent(*\**, *phone_number: str*, *first_name: str*, *last_name: str | None = None*, *vcard: str | None = None*, *\*\*extra_data: Any*)
:   Represents the [content](https://core.telegram.org/bots/api#inputmessagecontent) of a contact message to be sent as the result of an inline query.

    Source: <https://core.telegram.org/bots/api#inputcontactmessagecontent>

    phone_number*: str*
    :   Contact’s phone number

    first_name*: str*
    :   Contact’s first name

    last_name*: str | None*
    :   *Optional*. Contact’s last name

    vcard*: str | None*
    :   *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes
