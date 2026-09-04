# InlineQueryResultCachedGif

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result_cached_gif.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result_cached_gif.html)

*class* aiogram.types.inline_query_result_cached_gif.InlineQueryResultCachedGif(*\**, *type: ~typing.Literal[InlineQueryResultType.GIF] = InlineQueryResultType.GIF*, *id: str*, *gif_file_id: str*, *title: str | None = None*, *caption: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *show_caption_above_media: bool | ~aiogram.client.default.Default | None = <Default('show_caption_above_media')>*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | None = None*, *input_message_content: ~aiogram.types.input_text_message_content.InputTextMessageContent | ~aiogram.types.input_rich_message_content.InputRichMessageContent | ~aiogram.types.input_location_message_content.InputLocationMessageContent | ~aiogram.types.input_venue_message_content.InputVenueMessageContent | ~aiogram.types.input_contact_message_content.InputContactMessageContent | ~aiogram.types.input_invoice_message_content.InputInvoiceMessageContent | None = None*, *\*\*extra_data: ~typing.Any*)
:   Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with specified content instead of the animation.

    Source: <https://core.telegram.org/bots/api#inlinequeryresultcachedgif>

    type*: Literal[InlineQueryResultType.GIF]*
    :   Type of the result, must be *gif*

    id*: str*
    :   Unique identifier for this result, 1-64 bytes

    gif_file_id*: str*
    :   A valid file identifier for the GIF file

    title*: str | None*
    :   *Optional*. Title for the result

    caption*: str | None*
    :   *Optional*. Caption of the GIF file to be sent, 0-1024 characters after entities parsing

    parse_mode*: str | Default | None*
    :   *Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*

    show_caption_above_media*: bool | Default | None*
    :   *Optional*. Pass `True` if the caption must be shown above the message media

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message

    input_message_content*: InputMessageContentUnion | None*
    :   *Optional*. Content of the message to be sent instead of the GIF animation
