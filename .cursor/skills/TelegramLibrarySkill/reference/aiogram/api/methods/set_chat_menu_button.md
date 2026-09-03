# setChatMenuButton

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_chat_menu_button.html](https://docs.aiogram.dev/en/latest/api/methods/set_chat_menu_button.html)

Returns: `bool`

*class* aiogram.methods.set_chat_menu_button.SetChatMenuButton(*\**, *chat_id: int | None = None*, *menu_button: Annotated[[MenuButtonCommands](../types/menu_button_commands.html#aiogram.types.menu_button_commands.MenuButtonCommands "aiogram.types.menu_button_commands.MenuButtonCommands") | [MenuButtonWebApp](../types/menu_button_web_app.html#aiogram.types.menu_button_web_app.MenuButtonWebApp "aiogram.types.menu_button_web_app.MenuButtonWebApp") | [MenuButtonDefault](../types/menu_button_default.html#aiogram.types.menu_button_default.MenuButtonDefault "aiogram.types.menu_button_default.MenuButtonDefault"), FieldInfo(annotation=NoneType, required=True, discriminator='type')] | None = None*, *\*\*extra_data: Any*)
:   Use this method to change the bot’s menu button in a private chat, or the default menu button. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setchatmenubutton>

    chat_id*: int | None*
    :   Unique identifier for the target private chat. If not specified, the bot’s default menu button will be changed

    menu_button*: MenuButtonUnion | None*
    :   A JSON-serialized object for the bot’s new menu button. Defaults to [`aiogram.types.menu_button_default.MenuButtonDefault`](../types/menu_button_default.html#aiogram.types.menu_button_default.MenuButtonDefault "aiogram.types.menu_button_default.MenuButtonDefault")

## Usage

### As bot method

```
result: bool = await bot.set_chat_menu_button(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_chat_menu_button import SetChatMenuButton`
- alias: `from aiogram.methods import SetChatMenuButton`

#### With specific bot

```
result: bool = await bot(SetChatMenuButton(...))
```

#### As reply into Webhook in handler

```
return SetChatMenuButton(...)
```
