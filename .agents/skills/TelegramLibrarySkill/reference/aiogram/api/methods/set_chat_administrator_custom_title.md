# setChatAdministratorCustomTitle

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_chat_administrator_custom_title.html](https://docs.aiogram.dev/en/latest/api/methods/set_chat_administrator_custom_title.html)

Returns: `bool`

*class* aiogram.methods.set_chat_administrator_custom_title.SetChatAdministratorCustomTitle(*\**, *chat_id: int | str*, *user_id: int*, *custom_title: str*, *\*\*extra_data: Any*)
:   Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setchatadministratorcustomtitle>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    user_id*: int*
    :   Unique identifier of the target user

    custom_title*: str*
    :   New custom title for the administrator; 0-16 characters, emoji are not allowed

## Usage

### As bot method

```
result: bool = await bot.set_chat_administrator_custom_title(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_chat_administrator_custom_title import SetChatAdministratorCustomTitle`
- alias: `from aiogram.methods import SetChatAdministratorCustomTitle`

#### With specific bot

```
result: bool = await bot(SetChatAdministratorCustomTitle(...))
```

#### As reply into Webhook in handler

```
return SetChatAdministratorCustomTitle(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.set_administrator_custom_title()`](../types/chat.html#aiogram.types.chat.Chat.set_administrator_custom_title "aiogram.types.chat.Chat.set_administrator_custom_title")
