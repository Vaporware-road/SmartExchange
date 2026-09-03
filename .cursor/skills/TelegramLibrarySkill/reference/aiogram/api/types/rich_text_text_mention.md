# RichTextTextMention

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_text_text_mention.html](https://docs.aiogram.dev/en/latest/api/types/rich_text_text_mention.html)

*class* aiogram.types.rich_text_text_mention.RichTextTextMention(*\**, *type: Literal[RichTextType.TEXT_MENTION] = RichTextType.TEXT_MENTION*, *text: RichTextUnion*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *\*\*extra_data: Any*)
:   A mention of a Telegram user by their identifier.

    Source: <https://core.telegram.org/bots/api#richtexttextmention>

    type*: Literal[RichTextType.TEXT_MENTION]*
    :   Type of the rich text, always ‘text_mention’

    text*: RichTextUnion*
    :   The text

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   The mentioned user
