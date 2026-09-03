# RichTextMention

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_text_mention.html](https://docs.aiogram.dev/en/latest/api/types/rich_text_mention.html)

*class* aiogram.types.rich_text_mention.RichTextMention(*\**, *type: Literal[RichTextType.MENTION] = RichTextType.MENTION*, *text: RichTextUnion*, *username: str*, *\*\*extra_data: Any*)
:   A mention by a username.

    Source: <https://core.telegram.org/bots/api#richtextmention>

    type*: Literal[RichTextType.MENTION]*
    :   Type of the rich text, always ‘mention’

    text*: RichTextUnion*
    :   The text

    username*: str*
    :   The username
