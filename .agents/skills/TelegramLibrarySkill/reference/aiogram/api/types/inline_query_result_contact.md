# InlineQueryResultContact

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result_contact.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result_contact.html)

*class* aiogram.types.inline_query_result_contact.InlineQueryResultContact(*\**, *type: Literal[InlineQueryResultType.CONTACT] = InlineQueryResultType.CONTACT*, *id: str*, *phone_number: str*, *first_name: str*, *last_name: str | None = None*, *vcard: str | None = None*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *input_message_content: [InputTextMessageContent](input_text_message_content.html#aiogram.types.input_text_message_content.InputTextMessageContent "aiogram.types.input_text_message_content.InputTextMessageContent") | [InputRichMessageContent](input_rich_message_content.html#aiogram.types.input_rich_message_content.InputRichMessageContent "aiogram.types.input_rich_message_content.InputRichMessageContent") | [InputLocationMessageContent](input_location_message_content.html#aiogram.types.input_location_message_content.InputLocationMessageContent "aiogram.types.input_location_message_content.InputLocationMessageContent") | [InputVenueMessageContent](input_venue_message_content.html#aiogram.types.input_venue_message_content.InputVenueMessageContent "aiogram.types.input_venue_message_content.InputVenueMessageContent") | [InputContactMessageContent](input_contact_message_content.html#aiogram.types.input_contact_message_content.InputContactMessageContent "aiogram.types.input_contact_message_content.InputContactMessageContent") | [InputInvoiceMessageContent](input_invoice_message_content.html#aiogram.types.input_invoice_message_content.InputInvoiceMessageContent "aiogram.types.input_invoice_message_content.InputInvoiceMessageContent") | None = None*, *thumbnail_url: str | None = None*, *thumbnail_width: int | None = None*, *thumbnail_height: int | None = None*, *\*\*extra_data: Any*)
:   Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the contact.

    Source: <https://core.telegram.org/bots/api#inlinequeryresultcontact>

    type*: Literal[InlineQueryResultType.CONTACT]*
    :   Type of the result, must be *contact*

    id*: str*
    :   Unique identifier for this result, 1-64 Bytes

    phone_number*: str*
    :   Contact’s phone number

    first_name*: str*
    :   Contact’s first name

    last_name*: str | None*
    :   *Optional*. Contact’s last name

    vcard*: str | None*
    :   *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message

    input_message_content*: InputMessageContentUnion | None*
    :   *Optional*. Content of the message to be sent instead of the contact

    thumbnail_url*: str | None*
    :   *Optional*. Url of the thumbnail for the result

    thumbnail_width*: int | None*
    :   *Optional*. Thumbnail width

    thumbnail_height*: int | None*
    :   *Optional*. Thumbnail height
