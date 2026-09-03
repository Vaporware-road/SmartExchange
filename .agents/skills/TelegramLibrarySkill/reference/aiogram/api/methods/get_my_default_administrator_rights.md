# getMyDefaultAdministratorRights

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_my_default_administrator_rights.html](https://docs.aiogram.dev/en/latest/api/methods/get_my_default_administrator_rights.html)

Returns: `ChatAdministratorRights`

*class* aiogram.methods.get_my_default_administrator_rights.GetMyDefaultAdministratorRights(*\**, *for_channels: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to get the current default administrator rights of the bot. Returns [`aiogram.types.chat_administrator_rights.ChatAdministratorRights`](../types/chat_administrator_rights.html#aiogram.types.chat_administrator_rights.ChatAdministratorRights "aiogram.types.chat_administrator_rights.ChatAdministratorRights") on success.

    Source: <https://core.telegram.org/bots/api#getmydefaultadministratorrights>

    for_channels*: bool | None*
    :   Pass `True` to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned

## Usage

### As bot method

```
result: ChatAdministratorRights = await bot.get_my_default_administrator_rights(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_my_default_administrator_rights import GetMyDefaultAdministratorRights`
- alias: `from aiogram.methods import GetMyDefaultAdministratorRights`

#### With specific bot

```
result: ChatAdministratorRights = await bot(GetMyDefaultAdministratorRights(...))
```
