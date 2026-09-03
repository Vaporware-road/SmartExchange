# BotCommandScopeChatAdministrators

> Source: [https://docs.aiogram.dev/en/latest/api/types/bot_command_scope_chat_administrators.html](https://docs.aiogram.dev/en/latest/api/types/bot_command_scope_chat_administrators.html)

*class* aiogram.types.bot_command_scope_chat_administrators.BotCommandScopeChatAdministrators(*\**, *type: Literal[BotCommandScopeType.CHAT_ADMINISTRATORS] = BotCommandScopeType.CHAT_ADMINISTRATORS*, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Represents the [scope](https://core.telegram.org/bots/api#botcommandscope) of bot commands, covering all administrators of a specific group or supergroup chat.

    Source: <https://core.telegram.org/bots/api#botcommandscopechatadministrators>

    type*: Literal[BotCommandScopeType.CHAT_ADMINISTRATORS]*
    :   Scope type, must be *chat_administrators*

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`. Channel direct messages chats and channel chats aren’t supported
