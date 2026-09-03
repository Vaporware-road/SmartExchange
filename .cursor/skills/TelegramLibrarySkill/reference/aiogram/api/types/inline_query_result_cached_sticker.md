# InlineQueryResultCachedSticker

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result_cached_sticker.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result_cached_sticker.html)

*class* aiogram.types.inline_query_result_cached_sticker.InlineQueryResultCachedSticker(*\**, *type: Literal[InlineQueryResultType.STICKER] = InlineQueryResultType.STICKER*, *id: str*, *sticker_file_id: str*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *input_message_content: [InputTextMessageContent](input_text_message_content.html#aiogram.types.input_text_message_content.InputTextMessageContent "aiogram.types.input_text_message_content.InputTextMessageContent") | [InputRichMessageContent](input_rich_message_content.html#aiogram.types.input_rich_message_content.InputRichMessageContent "aiogram.types.input_rich_message_content.InputRichMessageContent") | [InputLocationMessageContent](input_location_message_content.html#aiogram.types.input_location_message_content.InputLocationMessageContent "aiogram.types.input_location_message_content.InputLocationMessageContent") | [InputVenueMessageContent](input_venue_message_content.html#aiogram.types.input_venue_message_content.InputVenueMessageContent "aiogram.types.input_venue_message_content.InputVenueMessageContent") | [InputContactMessageContent](input_contact_message_content.html#aiogram.types.input_contact_message_content.InputContactMessageContent "aiogram.types.input_contact_message_content.InputContactMessageContent") | [InputInvoiceMessageContent](input_invoice_message_content.html#aiogram.types.input_invoice_message_content.InputInvoiceMessageContent "aiogram.types.input_invoice_message_content.InputInvoiceMessageContent") | None = None*, *\*\*extra_data: Any*)
:   Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the sticker.

    Source: <https://core.telegram.org/bots/api#inlinequeryresultcachedsticker>

    type*: Literal[InlineQueryResultType.STICKER]*
    :   Type of the result, must be *sticker*

    id*: str*
    :   Unique identifier for this result, 1-64 bytes

    sticker_file_id*: str*
    :   A valid file identifier of the sticker

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message

    input_message_content*: InputMessageContentUnion | None*
    :   *Optional*. Content of the message to be sent instead of the sticker
