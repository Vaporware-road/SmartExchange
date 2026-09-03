# BotCommandScopeDefault

> Source: [https://docs.aiogram.dev/en/latest/api/types/bot_command_scope_default.html](https://docs.aiogram.dev/en/latest/api/types/bot_command_scope_default.html)

*class* aiogram.types.bot_command_scope_default.BotCommandScopeDefault(*\**, *type: Literal[BotCommandScopeType.DEFAULT] = BotCommandScopeType.DEFAULT*, *\*\*extra_data: Any*)
:   Represents the default [scope](https://core.telegram.org/bots/api#botcommandscope) of bot commands. Default commands are used if no commands with a [narrower scope](https://core.telegram.org/bots/api#determining-list-of-commands) are specified for the user.

    Source: <https://core.telegram.org/bots/api#botcommandscopedefault>

    type*: Literal[BotCommandScopeType.DEFAULT]*
    :   Scope type, must be *default*
