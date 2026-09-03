# setChatStickerSet

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_chat_sticker_set.html](https://docs.aiogram.dev/en/latest/api/methods/set_chat_sticker_set.html)

Returns: `bool`

*class* aiogram.methods.set_chat_sticker_set.SetChatStickerSet(*\**, *chat_id: int | str*, *sticker_set_name: str*, *\*\*extra_data: Any*)
:   Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field *can_set_sticker_set* optionally returned in [`aiogram.methods.get_chat.GetChat`](get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat") requests to check if the bot can use this method. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setchatstickerset>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    sticker_set_name*: str*
    :   Name of the sticker set to be set as the group sticker set

## Usage

### As bot method

```
result: bool = await bot.set_chat_sticker_set(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_chat_sticker_set import SetChatStickerSet`
- alias: `from aiogram.methods import SetChatStickerSet`

#### With specific bot

```
result: bool = await bot(SetChatStickerSet(...))
```

#### As reply into Webhook in handler

```
return SetChatStickerSet(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.set_sticker_set()`](../types/chat.html#aiogram.types.chat.Chat.set_sticker_set "aiogram.types.chat.Chat.set_sticker_set")
