# InlineQueryResultMpeg4Gif

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result_mpeg4_gif.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result_mpeg4_gif.html)

*class* aiogram.types.inline_query_result_mpeg4_gif.InlineQueryResultMpeg4Gif(*\**, *type: ~typing.Literal[InlineQueryResultType.MPEG4_GIF] = InlineQueryResultType.MPEG4_GIF*, *id: str*, *mpeg4_url: str*, *thumbnail_url: str*, *mpeg4_width: int | None = None*, *mpeg4_height: int | None = None*, *mpeg4_duration: int | None = None*, *thumbnail_mime_type: str | None = None*, *title: str | None = None*, *caption: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *show_caption_above_media: bool | ~aiogram.client.default.Default | None = <Default('show_caption_above_media')>*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | None = None*, *input_message_content: ~aiogram.types.input_text_message_content.InputTextMessageContent | ~aiogram.types.input_rich_message_content.InputRichMessageContent | ~aiogram.types.input_location_message_content.InputLocationMessageContent | ~aiogram.types.input_venue_message_content.InputVenueMessageContent | ~aiogram.types.input_contact_message_content.InputContactMessageContent | ~aiogram.types.input_invoice_message_content.InputInvoiceMessageContent | None = None*, *\*\*extra_data: ~typing.Any*)
:   Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the animation.

    Source: <https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif>

    type*: Literal[InlineQueryResultType.MPEG4_GIF]*
    :   Type of the result, must be *mpeg4_gif*

    id*: str*
    :   Unique identifier for this result, 1-64 bytes

    mpeg4_url*: str*
    :   A valid URL for the MPEG4 file

    thumbnail_url*: str*
    :   URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result

    mpeg4_width*: int | None*
    :   *Optional*. Video width

    mpeg4_height*: int | None*
    :   *Optional*. Video height

    mpeg4_duration*: int | None*
    :   *Optional*. Video duration in seconds

    thumbnail_mime_type*: str | None*
    :   *Optional*. MIME type of the thumbnail, must be one of ‘image/jpeg’, ‘image/gif’, or ‘video/mp4’. Defaults to ‘image/jpeg’

    title*: str | None*
    :   *Optional*. Title for the result

    caption*: str | None*
    :   *Optional*. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing

    parse_mode*: str | Default | None*
    :   *Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*

    show_caption_above_media*: bool | Default | None*
    :   *Optional*. Pass `True` if the caption must be shown above the message media

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message

    input_message_content*: InputMessageContentUnion | None*
    :   *Optional*. Content of the message to be sent instead of the video animation
