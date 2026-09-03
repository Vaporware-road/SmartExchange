# InlineQueryResultVoice

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result_voice.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result_voice.html)

*class* aiogram.types.inline_query_result_voice.InlineQueryResultVoice(*\**, *type: ~typing.Literal[InlineQueryResultType.VOICE] = InlineQueryResultType.VOICE*, *id: str*, *voice_url: str*, *title: str*, *caption: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *voice_duration: int | None = None*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | None = None*, *input_message_content: ~aiogram.types.input_text_message_content.InputTextMessageContent | ~aiogram.types.input_rich_message_content.InputRichMessageContent | ~aiogram.types.input_location_message_content.InputLocationMessageContent | ~aiogram.types.input_venue_message_content.InputVenueMessageContent | ~aiogram.types.input_contact_message_content.InputContactMessageContent | ~aiogram.types.input_invoice_message_content.InputInvoiceMessageContent | None = None*, *\*\*extra_data: ~typing.Any*)
:   Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the the voice message.

    Source: <https://core.telegram.org/bots/api#inlinequeryresultvoice>

    type*: Literal[InlineQueryResultType.VOICE]*
    :   Type of the result, must be *voice*

    id*: str*
    :   Unique identifier for this result, 1-64 bytes

    voice_url*: str*
    :   A valid URL for the voice recording

    title*: str*
    :   Recording title

    caption*: str | None*
    :   *Optional*. Caption, 0-1024 characters after entities parsing

    parse_mode*: str | Default | None*
    :   *Optional*. Mode for parsing entities in the voice message caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*

    voice_duration*: int | None*
    :   *Optional*. Recording duration in seconds

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message

    input_message_content*: InputMessageContentUnion | None*
    :   *Optional*. Content of the message to be sent instead of the voice recording
