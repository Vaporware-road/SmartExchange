# setChatTitle

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_chat_title.html](https://docs.aiogram.dev/en/latest/api/methods/set_chat_title.html)

Returns: `bool`

*class* aiogram.methods.set_chat_title.SetChatTitle(*\**, *chat_id: int | str*, *title: str*, *\*\*extra_data: Any*)
:   Use this method to change the title of a chat. Titles can’t be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setchattitle>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    title*: str*
    :   New chat title, 1-128 characters

## Usage

### As bot method

```
result: bool = await bot.set_chat_title(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_chat_title import SetChatTitle`
- alias: `from aiogram.methods import SetChatTitle`

#### With specific bot

```
result: bool = await bot(SetChatTitle(...))
```

#### As reply into Webhook in handler

```
return SetChatTitle(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.set_title()`](../types/chat.html#aiogram.types.chat.Chat.set_title "aiogram.types.chat.Chat.set_title")
