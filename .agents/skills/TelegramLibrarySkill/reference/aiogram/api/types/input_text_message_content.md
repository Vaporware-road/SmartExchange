# InputTextMessageContent

> Source: [https://docs.aiogram.dev/en/latest/api/types/input_text_message_content.html](https://docs.aiogram.dev/en/latest/api/types/input_text_message_content.html)

*class* aiogram.types.input_text_message_content.InputTextMessageContent(*\**, *message_text: str*, *parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *link_preview_options: ~aiogram.types.link_preview_options.LinkPreviewOptions | ~aiogram.client.default.Default | None = <Default('link_preview')>*, *disable_web_page_preview: bool | None = None*, *\*\*extra_data: ~typing.Any*)
:   Represents the [content](https://core.telegram.org/bots/api#inputmessagecontent) of a text message to be sent as the result of an inline query.

    Source: <https://core.telegram.org/bots/api#inputtextmessagecontent>

    message_text*: str*
    :   Text of the message to be sent, 1-4096 characters

    parse_mode*: str | Default | None*
    :   *Optional*. Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. List of special entities that appear in message text, which can be specified instead of *parse_mode*

    link_preview_options*: [LinkPreviewOptions](link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | Default | None*
    :   *Optional*. Link preview generation options for the message

    disable_web_page_preview*: bool | None*
    :   *Optional*. Disables link previews for links in the sent message

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>
