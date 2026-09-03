# setMyDefaultAdministratorRights

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_my_default_administrator_rights.html](https://docs.aiogram.dev/en/latest/api/methods/set_my_default_administrator_rights.html)

Returns: `bool`

*class* aiogram.methods.set_my_default_administrator_rights.SetMyDefaultAdministratorRights(*\**, *rights: [ChatAdministratorRights](../types/chat_administrator_rights.html#aiogram.types.chat_administrator_rights.ChatAdministratorRights "aiogram.types.chat_administrator_rights.ChatAdministratorRights") | None = None*, *for_channels: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to change the default administrator rights requested by the bot when it’s added as an administrator to groups or channels. These rights will be suggested to users, but they are free to modify the list before adding the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setmydefaultadministratorrights>

    rights*: [ChatAdministratorRights](../types/chat_administrator_rights.html#aiogram.types.chat_administrator_rights.ChatAdministratorRights "aiogram.types.chat_administrator_rights.ChatAdministratorRights") | None*
    :   A JSON-serialized object describing new default administrator rights. If not specified, the default administrator rights will be cleared

    for_channels*: bool | None*
    :   Pass `True` to change the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be changed

## Usage

### As bot method

```
result: bool = await bot.set_my_default_administrator_rights(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_my_default_administrator_rights import SetMyDefaultAdministratorRights`
- alias: `from aiogram.methods import SetMyDefaultAdministratorRights`

#### With specific bot

```
result: bool = await bot(SetMyDefaultAdministratorRights(...))
```

#### As reply into Webhook in handler

```
return SetMyDefaultAdministratorRights(...)
```
