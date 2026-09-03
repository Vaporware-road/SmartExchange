# TextQuote

> Source: [https://docs.aiogram.dev/en/latest/api/types/text_quote.html](https://docs.aiogram.dev/en/latest/api/types/text_quote.html)

*class* aiogram.types.text_quote.TextQuote(*\**, *text: str*, *position: int*, *entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *is_manual: bool | None = None*, *\*\*extra_data: Any*)
:   This object contains information about the quoted part of a message that is replied to by the given message.

    Source: <https://core.telegram.org/bots/api#textquote>

    text*: str*
    :   Text of the quoted part of a message that is replied to by the given message

    position*: int*
    :   Approximate quote position in the original message in UTF-16 code units as specified by the sender

    entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. Special entities that appear in the quote. Currently, only *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, *custom_emoji*, and *date_time* entities are kept in quotes

    is_manual*: bool | None*
    :   *Optional*. `True`, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server
