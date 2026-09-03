# BotCommandScopeChat

> Source: [https://docs.aiogram.dev/en/latest/api/types/bot_command_scope_chat.html](https://docs.aiogram.dev/en/latest/api/types/bot_command_scope_chat.html)

*class* aiogram.types.bot_command_scope_chat.BotCommandScopeChat(*\**, *type: Literal[BotCommandScopeType.CHAT] = BotCommandScopeType.CHAT*, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Represents the [scope](https://core.telegram.org/bots/api#botcommandscope) of bot commands, covering a specific chat.

    Source: <https://core.telegram.org/bots/api#botcommandscopechat>

    type*: Literal[BotCommandScopeType.CHAT]*
    :   Scope type, must be *chat*

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`. Channel direct messages chats and channel chats aren’t supported
