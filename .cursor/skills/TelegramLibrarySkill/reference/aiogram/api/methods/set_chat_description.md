# setChatDescription

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_chat_description.html](https://docs.aiogram.dev/en/latest/api/methods/set_chat_description.html)

Returns: `bool`

*class* aiogram.methods.set_chat_description.SetChatDescription(*\**, *chat_id: int | str*, *description: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setchatdescription>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    description*: str | None*
    :   New chat description, 0-255 characters

## Usage

### As bot method

```
result: bool = await bot.set_chat_description(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_chat_description import SetChatDescription`
- alias: `from aiogram.methods import SetChatDescription`

#### With specific bot

```
result: bool = await bot(SetChatDescription(...))
```

#### As reply into Webhook in handler

```
return SetChatDescription(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.set_description()`](../types/chat.html#aiogram.types.chat.Chat.set_description "aiogram.types.chat.Chat.set_description")
