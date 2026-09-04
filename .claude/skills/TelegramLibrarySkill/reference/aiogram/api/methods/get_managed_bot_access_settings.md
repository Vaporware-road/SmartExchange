# getManagedBotAccessSettings

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_managed_bot_access_settings.html](https://docs.aiogram.dev/en/latest/api/methods/get_managed_bot_access_settings.html)

Returns: `BotAccessSettings`

*class* aiogram.methods.get_managed_bot_access_settings.GetManagedBotAccessSettings(*\**, *user_id: int*, *\*\*extra_data: Any*)
:   Use this method to get the access settings of a managed bot. Returns a [`aiogram.types.bot_access_settings.BotAccessSettings`](../types/bot_access_settings.html#aiogram.types.bot_access_settings.BotAccessSettings "aiogram.types.bot_access_settings.BotAccessSettings") object on success.

    Source: <https://core.telegram.org/bots/api#getmanagedbotaccesssettings>

    user_id*: int*
    :   User identifier of the managed bot whose access settings will be returned

## Usage

### As bot method

```
result: BotAccessSettings = await bot.get_managed_bot_access_settings(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_managed_bot_access_settings import GetManagedBotAccessSettings`
- alias: `from aiogram.methods import GetManagedBotAccessSettings`

#### With specific bot

```
result: BotAccessSettings = await bot(GetManagedBotAccessSettings(...))
```
