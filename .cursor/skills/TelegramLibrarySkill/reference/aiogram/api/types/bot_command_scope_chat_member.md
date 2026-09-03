# BotCommandScopeChatMember

> Source: [https://docs.aiogram.dev/en/latest/api/types/bot_command_scope_chat_member.html](https://docs.aiogram.dev/en/latest/api/types/bot_command_scope_chat_member.html)

*class* aiogram.types.bot_command_scope_chat_member.BotCommandScopeChatMember(*\**, *type: Literal[BotCommandScopeType.CHAT_MEMBER] = BotCommandScopeType.CHAT_MEMBER*, *chat_id: int | str*, *user_id: int*, *\*\*extra_data: Any*)
:   Represents the [scope](https://core.telegram.org/bots/api#botcommandscope) of bot commands, covering a specific member of a group or supergroup chat.

    Source: <https://core.telegram.org/bots/api#botcommandscopechatmember>

    type*: Literal[BotCommandScopeType.CHAT_MEMBER]*
    :   Scope type, must be *chat_member*

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`. Channel direct messages chats and channel chats aren’t supported

    user_id*: int*
    :   Unique identifier of the target user
