# getChatMember

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_chat_member.html](https://docs.aiogram.dev/en/latest/api/methods/get_chat_member.html)

Returns: `ResultChatMemberUnion`

*class* aiogram.methods.get_chat_member.GetChatMember(*\**, *chat_id: int | str*, *user_id: int*, *\*\*extra_data: Any*)
:   Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a [`aiogram.types.chat_member.ChatMember`](../types/chat_member.html#aiogram.types.chat_member.ChatMember "aiogram.types.chat_member.ChatMember") object on success.

    Source: <https://core.telegram.org/bots/api#getchatmember>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup or channel in the format `@username`

    user_id*: int*
    :   Unique identifier of the target user

## Usage

### As bot method

```
result: ResultChatMemberUnion = await bot.get_chat_member(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_chat_member import GetChatMember`
- alias: `from aiogram.methods import GetChatMember`

#### With specific bot

```
result: ResultChatMemberUnion = await bot(GetChatMember(...))
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.get_member()`](../types/chat.html#aiogram.types.chat.Chat.get_member "aiogram.types.chat.Chat.get_member")
