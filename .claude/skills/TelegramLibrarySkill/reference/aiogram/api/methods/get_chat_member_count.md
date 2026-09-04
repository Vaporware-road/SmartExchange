# getChatMemberCount

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_chat_member_count.html](https://docs.aiogram.dev/en/latest/api/methods/get_chat_member_count.html)

Returns: `int`

*class* aiogram.methods.get_chat_member_count.GetChatMemberCount(*\**, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Use this method to get the number of members in a chat. Returns *Integer* on success.

    Source: <https://core.telegram.org/bots/api#getchatmembercount>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup or channel in the format `@username`

## Usage

### As bot method

```
result: int = await bot.get_chat_member_count(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_chat_member_count import GetChatMemberCount`
- alias: `from aiogram.methods import GetChatMemberCount`

#### With specific bot

```
result: int = await bot(GetChatMemberCount(...))
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.get_member_count()`](../types/chat.html#aiogram.types.chat.Chat.get_member_count "aiogram.types.chat.Chat.get_member_count")
