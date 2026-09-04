# InlineQueryResultDocument

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result_document.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result_document.html)

*class* aiogram.types.inline_query_result_document.InlineQueryResultDocument(*\**, *type: ~typing.Literal[InlineQueryResultType.DOCUMENT] = InlineQueryResultType.DOCUMENT*, *id: str*, *title: str*, *document_url: str*, *mime_type: str*, *caption: str | None = None*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *caption_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *description: str | None = None*, *reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | None = None*, *input_message_content: ~aiogram.types.input_text_message_content.InputTextMessageContent | ~aiogram.types.input_rich_message_content.InputRichMessageContent | ~aiogram.types.input_location_message_content.InputLocationMessageContent | ~aiogram.types.input_venue_message_content.InputVenueMessageContent | ~aiogram.types.input_contact_message_content.InputContactMessageContent | ~aiogram.types.input_invoice_message_content.InputInvoiceMessageContent | None = None*, *thumbnail_url: str | None = None*, *thumbnail_width: int | None = None*, *thumbnail_height: int | None = None*, *\*\*extra_data: ~typing.Any*)
:   Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the file. Currently, only **.PDF** and **.ZIP** files can be sent using this method.

    Source: <https://core.telegram.org/bots/api#inlinequeryresultdocument>

    type*: Literal[InlineQueryResultType.DOCUMENT]*
    :   Type of the result, must be *document*

    id*: str*
    :   Unique identifier for this result, 1-64 bytes

    title*: str*
    :   Title for the result

    document_url*: str*
    :   A valid URL for the file

    mime_type*: str*
    :   MIME type of the content of the file, either ‘application/pdf’ or ‘application/zip’

    caption*: str | None*
    :   *Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing

    parse_mode*: str | Default | None*
    :   *Optional*. Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    caption_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode*

    description*: str | None*
    :   *Optional*. Short description of the result

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message

    input_message_content*: InputMessageContentUnion | None*
    :   *Optional*. Content of the message to be sent instead of the file

    thumbnail_url*: str | None*
    :   *Optional*. URL of the thumbnail (JPEG only) for the file

    thumbnail_width*: int | None*
    :   *Optional*. Thumbnail width

    thumbnail_height*: int | None*
    :   *Optional*. Thumbnail height
