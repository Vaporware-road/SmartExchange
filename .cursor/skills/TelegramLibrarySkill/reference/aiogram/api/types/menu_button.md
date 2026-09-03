# MenuButton

> Source: [https://docs.aiogram.dev/en/latest/api/types/menu_button.html](https://docs.aiogram.dev/en/latest/api/types/menu_button.html)

*class* aiogram.types.menu_button.MenuButton(*\**, *type: str*, *text: str | None = None*, *web_app: [WebAppInfo](web_app_info.html#aiogram.types.web_app_info.WebAppInfo "aiogram.types.web_app_info.WebAppInfo") | None = None*, *\*\*extra_data: Any*)
:   This object describes the bot’s menu button in a private chat. It should be one of

    > - [`aiogram.types.menu_button_commands.MenuButtonCommands`](menu_button_commands.html#aiogram.types.menu_button_commands.MenuButtonCommands "aiogram.types.menu_button_commands.MenuButtonCommands")
    > - [`aiogram.types.menu_button_web_app.MenuButtonWebApp`](menu_button_web_app.html#aiogram.types.menu_button_web_app.MenuButtonWebApp "aiogram.types.menu_button_web_app.MenuButtonWebApp")
    > - [`aiogram.types.menu_button_default.MenuButtonDefault`](menu_button_default.html#aiogram.types.menu_button_default.MenuButtonDefault "aiogram.types.menu_button_default.MenuButtonDefault")

    If a menu button other than [`aiogram.types.menu_button_default.MenuButtonDefault`](menu_button_default.html#aiogram.types.menu_button_default.MenuButtonDefault "aiogram.types.menu_button_default.MenuButtonDefault") is set for a private chat, then it is applied in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot commands.

    Source: <https://core.telegram.org/bots/api#menubutton>

    type*: str*
    :   Type of the button

    text*: str | None*
    :   *Optional*. Text on the button

    web_app*: [WebAppInfo](web_app_info.html#aiogram.types.web_app_info.WebAppInfo "aiogram.types.web_app_info.WebAppInfo") | None*
    :   *Optional*. Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method [`aiogram.methods.answer_web_app_query.AnswerWebAppQuery`](../methods/answer_web_app_query.html#aiogram.methods.answer_web_app_query.AnswerWebAppQuery "aiogram.methods.answer_web_app_query.AnswerWebAppQuery"). Alternatively, a `t.me` link to a Web App of the bot can be specified in the object instead of the Web App’s URL, in which case the Web App will be opened as if the user pressed the link
