# deleteChatStickerSet

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_chat_sticker_set.html](https://docs.aiogram.dev/en/latest/api/methods/delete_chat_sticker_set.html)

Returns: `bool`

*class* aiogram.methods.delete_chat_sticker_set.DeleteChatStickerSet(*\**, *chat_id: int | str*, *\*\*extra_data: Any*)
:   Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field *can_set_sticker_set* optionally returned in [`aiogram.methods.get_chat.GetChat`](get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat") requests to check if the bot can use this method. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deletechatstickerset>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

## Usage

### As bot method

```
result: bool = await bot.delete_chat_sticker_set(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_chat_sticker_set import DeleteChatStickerSet`
- alias: `from aiogram.methods import DeleteChatStickerSet`

#### With specific bot

```
result: bool = await bot(DeleteChatStickerSet(...))
```

#### As reply into Webhook in handler

```
return DeleteChatStickerSet(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.delete_sticker_set()`](../types/chat.html#aiogram.types.chat.Chat.delete_sticker_set "aiogram.types.chat.Chat.delete_sticker_set")
