# BotAccessSettings

> Source: [https://docs.aiogram.dev/en/latest/api/types/bot_access_settings.html](https://docs.aiogram.dev/en/latest/api/types/bot_access_settings.html)

*class* aiogram.types.bot_access_settings.BotAccessSettings(*\**, *is_access_restricted: bool*, *added_users: list[[User](user.html#aiogram.types.user.User "aiogram.types.user.User")] | None = None*, *\*\*extra_data: Any*)
:   This object describes the access settings of a bot.

    Source: <https://core.telegram.org/bots/api#botaccesssettings>

    is_access_restricted*: bool*
    :   `True`, if only selected users can access the bot. The bot’s owner can always access it

    added_users*: list[[User](user.html#aiogram.types.user.User "aiogram.types.user.User")] | None*
    :   *Optional*. The list of other users who have access to the bot if the access is restricted
