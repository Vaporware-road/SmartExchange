# MessageEntity

> Source: [https://docs.aiogram.dev/en/latest/api/types/message_entity.html](https://docs.aiogram.dev/en/latest/api/types/message_entity.html)

*class* aiogram.types.message_entity.MessageEntity(*\**, *type: str*, *offset: int*, *length: int*, *url: str | None = None*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *language: str | None = None*, *custom_emoji_id: str | None = None*, *unix_time: int | None = None*, *date_time_format: str | None = None*, *\*\*extra_data: Any*)
:   This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    Source: <https://core.telegram.org/bots/api#messageentity>

    type*: str*
    :   Type of the entity. Currently, can be ‘mention’ (`@username`), ‘hashtag’ (`#hashtag` or `#hashtag@chatusername`), ‘cashtag’ (`$USD` or `$USD@chatusername`), ‘bot_command’ (`/start@jobs_bot`), ‘url’ (`https://telegram.org`), ‘email’ (`do-not-reply@telegram.org`), ‘phone_number’ (`+1-212-555-0123`), ‘bold’ (**bold text**), ‘italic’ (*italic text*), ‘underline’ (underlined text), ‘strikethrough’ (strikethrough text), ‘spoiler’ (spoiler message), ‘blockquote’ (block quotation), ‘expandable_blockquote’ (collapsed-by-default block quotation), ‘code’ (monowidth string), ‘pre’ (monowidth block), ‘text_link’ (for clickable text URLs), ‘text_mention’ (for users [without usernames](https://telegram.org/blog/edit#new-mentions)), ‘custom_emoji’ (for inline custom emoji stickers), or ‘date_time’ (for formatted date and time)

    offset*: int*
    :   Offset in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length) to the start of the entity

    length*: int*
    :   Length of the entity in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length)

    url*: str | None*
    :   *Optional*. For ‘text_link’ only, URL that will be opened after user taps on the text

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. For ‘text_mention’ only, the mentioned user

    language*: str | None*
    :   *Optional*. For ‘pre’ only, the programming language of the entity text

    custom_emoji_id*: str | None*
    :   *Optional*. For ‘custom_emoji’ only, unique identifier of the custom emoji. Use [`aiogram.methods.get_custom_emoji_stickers.GetCustomEmojiStickers`](../methods/get_custom_emoji_stickers.html#aiogram.methods.get_custom_emoji_stickers.GetCustomEmojiStickers "aiogram.methods.get_custom_emoji_stickers.GetCustomEmojiStickers") to get full information about the sticker

    unix_time*: int | None*
    :   *Optional*. For ‘date_time’ only, the Unix time associated with the entity

    date_time_format*: str | None*
    :   *Optional*. For ‘date_time’ only, the string that defines the formatting of the date and time. See [date-time entity formatting](https://core.telegram.org/bots/api#date-time-entity-formatting) for more details

    extract_from(*text: str*) → str
