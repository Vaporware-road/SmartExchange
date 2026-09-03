# ManagedBotUpdated

> Source: [https://docs.aiogram.dev/en/latest/api/types/managed_bot_updated.html](https://docs.aiogram.dev/en/latest/api/types/managed_bot_updated.html)

*class* aiogram.types.managed_bot_updated.ManagedBotUpdated(*\**, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *bot: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *\*\*extra_data: Any*)
:   This object contains information about the creation, token update, or owner update of a bot that is managed by the current bot.

    Source: <https://core.telegram.org/bots/api#managedbotupdated>

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   User that created the bot

    bot_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Information about the bot. Token of the bot can be fetched using the method [`aiogram.methods.get_managed_bot_token.GetManagedBotToken`](../methods/get_managed_bot_token.html#aiogram.methods.get_managed_bot_token.GetManagedBotToken "aiogram.methods.get_managed_bot_token.GetManagedBotToken")
