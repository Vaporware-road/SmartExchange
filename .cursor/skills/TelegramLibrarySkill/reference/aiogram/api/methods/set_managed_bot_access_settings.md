# setManagedBotAccessSettings

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_managed_bot_access_settings.html](https://docs.aiogram.dev/en/latest/api/methods/set_managed_bot_access_settings.html)

Returns: `bool`

*class* aiogram.methods.set_managed_bot_access_settings.SetManagedBotAccessSettings(*\**, *user_id: int*, *is_access_restricted: bool*, *added_user_ids: list[int] | None = None*, *\*\*extra_data: Any*)
:   Use this method to change the access settings of a managed bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setmanagedbotaccesssettings>

    user_id*: int*
    :   User identifier of the managed bot whose access settings will be changed

    is_access_restricted*: bool*
    :   Pass `True` if only selected users can access the bot. The bot’s owner can always access it

    added_user_ids*: list[int] | None*
    :   A JSON-serialized list of up to 10 identifiers of users who will have access to the bot in addition to its owner. Ignored if *is_access_restricted* is `False`

## Usage

### As bot method

```
result: bool = await bot.set_managed_bot_access_settings(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_managed_bot_access_settings import SetManagedBotAccessSettings`
- alias: `from aiogram.methods import SetManagedBotAccessSettings`

#### With specific bot

```
result: bool = await bot(SetManagedBotAccessSettings(...))
```

#### As reply into Webhook in handler

```
return SetManagedBotAccessSettings(...)
```
