# setChatPhoto

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_chat_photo.html](https://docs.aiogram.dev/en/latest/api/methods/set_chat_photo.html)

Returns: `bool`

*class* aiogram.methods.set_chat_photo.SetChatPhoto(*\**, *chat_id: int | str*, *photo: [InputFile](../types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *\*\*extra_data: Any*)
:   Use this method to set a new profile photo for the chat. Photos can’t be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setchatphoto>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    photo*: [InputFile](../types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*
    :   New chat photo, uploaded using multipart/form-data

## Usage

### As bot method

```
result: bool = await bot.set_chat_photo(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_chat_photo import SetChatPhoto`
- alias: `from aiogram.methods import SetChatPhoto`

#### With specific bot

```
result: bool = await bot(SetChatPhoto(...))
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.set_photo()`](../types/chat.html#aiogram.types.chat.Chat.set_photo "aiogram.types.chat.Chat.set_photo")
