# getChat

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_chat.html](https://docs.aiogram.dev/en/latest/api/methods/get_chat.html)

Returns: `ChatFullInfo`

*class* aiogram.methods.get_chat.GetChat(*\**, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Use this method to get up-to-date information about the chat. Returns a [`aiogram.types.chat_full_info.ChatFullInfo`](../types/chat_full_info.html#aiogram.types.chat_full_info.ChatFullInfo "aiogram.types.chat_full_info.ChatFullInfo") object on success.

    Source: <https://core.telegram.org/bots/api#getchat>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup or channel in the format `@username`

## Usage

### As bot method

```
result: ChatFullInfo = await bot.get_chat(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_chat import GetChat`
- alias: `from aiogram.methods import GetChat`

#### With specific bot

```
result: ChatFullInfo = await bot(GetChat(...))
```
