# RichTextCustomEmoji

> Source: [https://docs.aiogram.dev/en/latest/api/types/rich_text_custom_emoji.html](https://docs.aiogram.dev/en/latest/api/types/rich_text_custom_emoji.html)

*class* aiogram.types.rich_text_custom_emoji.RichTextCustomEmoji(*\**, *type: Literal[RichTextType.CUSTOM_EMOJI] = RichTextType.CUSTOM_EMOJI*, *custom_emoji_id: str*, *alternative_text: str*, *\*\*extra_data: Any*)
:   A custom emoji.

    Source: <https://core.telegram.org/bots/api#richtextcustomemoji>

    type*: Literal[RichTextType.CUSTOM_EMOJI]*
    :   Type of the rich text, always ‘custom_emoji’

    custom_emoji_id*: str*
    :   Unique identifier of the custom emoji. Use [`aiogram.methods.get_custom_emoji_stickers.GetCustomEmojiStickers`](../methods/get_custom_emoji_stickers.html#aiogram.methods.get_custom_emoji_stickers.GetCustomEmojiStickers "aiogram.methods.get_custom_emoji_stickers.GetCustomEmojiStickers") to get full information about the sticker

    alternative_text*: str*
    :   Alternative emoji for the custom emoji
