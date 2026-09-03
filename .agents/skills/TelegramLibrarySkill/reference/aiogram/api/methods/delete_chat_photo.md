# deleteChatPhoto

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_chat_photo.html](https://docs.aiogram.dev/en/latest/api/methods/delete_chat_photo.html)

Returns: `bool`

*class* aiogram.methods.delete_chat_photo.DeleteChatPhoto(*\**, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Use this method to delete a chat photo. Photos can’t be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deletechatphoto>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

## Usage

### As bot method

```
result: bool = await bot.delete_chat_photo(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_chat_photo import DeleteChatPhoto`
- alias: `from aiogram.methods import DeleteChatPhoto`

#### With specific bot

```
result: bool = await bot(DeleteChatPhoto(...))
```

#### As reply into Webhook in handler

```
return DeleteChatPhoto(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.delete_photo()`](../types/chat.html#aiogram.types.chat.Chat.delete_photo "aiogram.types.chat.Chat.delete_photo")
