# BotCommand

> Source: [https://docs.aiogram.dev/en/latest/api/types/bot_command.html](https://docs.aiogram.dev/en/latest/api/types/bot_command.html)

*class* aiogram.types.bot_command.BotCommand(*\**, *command: str*, *description: str*, *is_ephemeral: bool | None = None*, *\*\*extra_data: Any*)
:   This object represents a bot command.

    Source: <https://core.telegram.org/bots/api#botcommand>

    command*: str*
    :   Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores

    description*: str*
    :   Description of the command; 1-256 characters

    is_ephemeral*: bool | None*
    :   *Optional*. `True`, if the command sends an ephemeral message, which can be seen only by the sender of the message and the bot
