# getChatMenuButton

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_chat_menu_button.html](https://docs.aiogram.dev/en/latest/api/methods/get_chat_menu_button.html)

Returns: `ResultMenuButtonUnion`

*class* aiogram.methods.get_chat_menu_button.GetChatMenuButton(*\**, *chat_id: int | None = None*, *\*\*extra_data: Any*)
:   Use this method to get the current value of the bot’s menu button in a private chat, or the default menu button. Returns [`aiogram.types.menu_button.MenuButton`](../types/menu_button.html#aiogram.types.menu_button.MenuButton "aiogram.types.menu_button.MenuButton") on success.

    Source: <https://core.telegram.org/bots/api#getchatmenubutton>

    chat_id*: int | None*
    :   Unique identifier for the target private chat. If not specified, the bot’s default menu button will be returned

## Usage

### As bot method

```
result: ResultMenuButtonUnion = await bot.get_chat_menu_button(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_chat_menu_button import GetChatMenuButton`
- alias: `from aiogram.methods import GetChatMenuButton`

#### With specific bot

```
result: ResultMenuButtonUnion = await bot(GetChatMenuButton(...))
```
