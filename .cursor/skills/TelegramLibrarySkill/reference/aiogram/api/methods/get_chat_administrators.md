# getChatAdministrators

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_chat_administrators.html](https://docs.aiogram.dev/en/latest/api/methods/get_chat_administrators.html)

Returns: `list[ResultChatMemberUnion]`

*class* aiogram.methods.get_chat_administrators.GetChatAdministrators(*\**, *chat_id: int | str*, *return_bots: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to get a list of administrators in a chat. Returns an Array of [`aiogram.types.chat_member.ChatMember`](../types/chat_member.html#aiogram.types.chat_member.ChatMember "aiogram.types.chat_member.ChatMember") objects.

    Source: <https://core.telegram.org/bots/api#getchatadministrators>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup or channel in the format `@username`

    return_bots*: bool | None*
    :   Pass `True` to additionally receive all bots that are administrators of the chat. By default, bots other than the current bot are omitted

## Usage

### As bot method

```
result: list[ResultChatMemberUnion] = await bot.get_chat_administrators(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_chat_administrators import GetChatAdministrators`
- alias: `from aiogram.methods import GetChatAdministrators`

#### With specific bot

```
result: list[ResultChatMemberUnion] = await bot(GetChatAdministrators(...))
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.get_administrators()`](../types/chat.html#aiogram.types.chat.Chat.get_administrators "aiogram.types.chat.Chat.get_administrators")
