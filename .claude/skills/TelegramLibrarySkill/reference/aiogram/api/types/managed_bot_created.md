# ManagedBotCreated

> Source: [https://docs.aiogram.dev/en/latest/api/types/managed_bot_created.html](https://docs.aiogram.dev/en/latest/api/types/managed_bot_created.html)

*class* aiogram.types.managed_bot_created.ManagedBotCreated(*\**, *bot: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *\*\*extra_data: Any*)
:   This object contains information about the bot that was created to be managed by the current bot.

    Source: <https://core.telegram.org/bots/api#managedbotcreated>

    bot_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Information about the bot. The bot’s token can be fetched using the method [`aiogram.methods.get_managed_bot_token.GetManagedBotToken`](../methods/get_managed_bot_token.html#aiogram.methods.get_managed_bot_token.GetManagedBotToken "aiogram.methods.get_managed_bot_token.GetManagedBotToken")
