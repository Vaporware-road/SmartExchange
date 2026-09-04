# InlineQueryResultCachedPhoto

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result_cached_photo.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result_cached_photo.html)

*class* aiogram.types.inline_query_result_cached_photo.InlineQueryResultCachedPhoto(*\**, *type: ~typing.Literal[InlineQueryResultType.PHOTO] = InlineQueryResultType.PHOTO*, *id: str*, *photo_file_id: str*, *title: str | None = None*, *description: str | None = None*, *caption: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *show_caption_above_media: bool | ~aiogram.client.default.Default | None = <Default('show_caption_above_media')>*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | None = None*, *input_message_content: ~aiogram.types.input_text_message_content.InputTextMessageContent | ~aiogram.types.input_rich_message_content.InputRichMessageContent | ~aiogram.types.input_location_message_content.InputLocationMessageContent | ~aiogram.types.input_venue_message_content.InputVenueMessageContent | ~aiogram.types.input_contact_message_content.InputContactMessageContent | ~aiogram.types.input_invoice_message_content.InputInvoiceMessageContent | None = None*, *\*\*extra_data: ~typing.Any*)
:   Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the photo.

    Source: <https://core.telegram.org/bots/api#inlinequeryresultcachedphoto>

    type*: Literal[InlineQueryResultType.PHOTO]*
    :   Type of the result, must be *photo*

    id*: str*
    :   Unique identifier for this result, 1-64 bytes

    photo_file_id*: str*
    :   A valid file identifier of the photo

    title*: str | None*
    :   *Optional*. Title for the result

    description*: str | None*
    :   *Optional*. Short description of the result

    caption*: str | None*
    :   *Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing

    parse_mode*: str | Default | None*
    :   *Optional*. Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*

    show_caption_above_media*: bool | Default | None*
    :   *Optional*. Pass `True` if the caption must be shown above the message media

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message

    input_message_content*: InputMessageContentUnion | None*
    :   *Optional*. Content of the message to be sent instead of the photo
