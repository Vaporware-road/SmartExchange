# SwitchInlineQueryChosenChat

> Source: [https://docs.aiogram.dev/en/latest/api/types/switch_inline_query_chosen_chat.html](https://docs.aiogram.dev/en/latest/api/types/switch_inline_query_chosen_chat.html)

*class* aiogram.types.switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat(*\**, *query: str | None = None*, *allow_user_chats: bool | None = None*, *allow_bot_chats: bool | None = None*, *allow_group_chats: bool | None = None*, *allow_channel_chats: bool | None = None*, *\*\*extra_data: Any*)
:   This object represents an inline button that switches the current user to inline mode in a chosen chat, with an optional default inline query.

    Source: <https://core.telegram.org/bots/api#switchinlinequerychosenchat>

    query*: str | None*
    :   *Optional*. The default inline query to be inserted in the input field. If left empty, only the bot’s username will be inserted

    allow_user_chats*: bool | None*
    :   *Optional*. `True`, if private chats with users can be chosen

    allow_bot_chats*: bool | None*
    :   *Optional*. `True`, if private chats with bots can be chosen

    allow_group_chats*: bool | None*
    :   *Optional*. `True`, if group and supergroup chats can be chosen

    allow_channel_chats*: bool | None*
    :   *Optional*. `True`, if channel chats can be chosen
