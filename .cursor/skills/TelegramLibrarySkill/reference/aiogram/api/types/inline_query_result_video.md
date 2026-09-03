# InlineQueryResultVideo

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result_video.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result_video.html)

*class* aiogram.types.inline_query_result_video.InlineQueryResultVideo(*\**, *type: ~typing.Literal[InlineQueryResultType.VIDEO] = InlineQueryResultType.VIDEO*, *id: str*, *video_url: str*, *mime_type: str*, *thumbnail_url: str*, *title: str*, *caption: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *show_caption_above_media: bool | ~aiogram.client.default.Default | None = <Default('show_caption_above_media')>*, *video_width: int | None = None*, *video_height: int | None = None*, *video_duration: int | None = None*, *description: str | None = None*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | None = None*, *input_message_content: ~aiogram.types.input_text_message_content.InputTextMessageContent | ~aiogram.types.input_rich_message_content.InputRichMessageContent | ~aiogram.types.input_location_message_content.InputLocationMessageContent | ~aiogram.types.input_venue_message_content.InputVenueMessageContent | ~aiogram.types.input_contact_message_content.InputContactMessageContent | ~aiogram.types.input_invoice_message_content.InputInvoiceMessageContent | None = None*, *\*\*extra_data: ~typing.Any*)
:   Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the video.

    > If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you **must** replace its content using *input_message_content*.

    Source: <https://core.telegram.org/bots/api#inlinequeryresultvideo>

    type*: Literal[InlineQueryResultType.VIDEO]*
    :   Type of the result, must be *video*

    id*: str*
    :   Unique identifier for this result, 1-64 bytes

    video_url*: str*
    :   A valid URL for the embedded video player or video file

    mime_type*: str*
    :   MIME type of the content of the video URL, ‘text/html’ or ‘video/mp4’

    thumbnail_url*: str*
    :   URL of the thumbnail (JPEG only) for the video

    title*: str*
    :   Title for the result

    caption*: str | None*
    :   *Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing

    parse_mode*: str | Default | None*
    :   *Optional*. Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*

    show_caption_above_media*: bool | Default | None*
    :   *Optional*. Pass `True` if the caption must be shown above the message media

    video_width*: int | None*
    :   *Optional*. Video width

    video_height*: int | None*
    :   *Optional*. Video height

    video_duration*: int | None*
    :   *Optional*. Video duration in seconds

    description*: str | None*
    :   *Optional*. Short description of the result

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message

    input_message_content*: InputMessageContentUnion | None*
    :   *Optional*. Content of the message to be sent instead of the video. This field is **required** if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video)
