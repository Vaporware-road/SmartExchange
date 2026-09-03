# RichTextAnchorLink

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_text_anchor_link.html](https://docs.aiogram.dev/en/latest/api/types/rich_text_anchor_link.html)

*class* aiogram.types.rich_text_anchor_link.RichTextAnchorLink(*\**, *type: Literal[RichTextType.ANCHOR_LINK] = RichTextType.ANCHOR_LINK*, *text: RichTextUnion*, *anchor_name: str*, *\*\*extra_data: Any*)
:   A link to an anchor.

    Source: <https://core.telegram.org/bots/api#richtextanchorlink>

    type*: Literal[RichTextType.ANCHOR_LINK]*
    :   Type of the rich text, always ‘anchor_link’

    text*: RichTextUnion*
    :   The link text

    anchor_name*: str*
    :   The name of the anchor. If the name is empty, then the link brings back to the top of the message
