# MenuButtonWebApp

> Source: [https://docs.aiogram.dev/en/latest/api/types/menu_button_web_app.html](https://docs.aiogram.dev/en/latest/api/types/menu_button_web_app.html)

*class* aiogram.types.menu_button_web_app.MenuButtonWebApp(*\**, *type: Literal[MenuButtonType.WEB_APP] = MenuButtonType.WEB_APP*, *text: str*, *web_app: [WebAppInfo](web_app_info.html#aiogram.types.web_app_info.WebAppInfo "aiogram.types.web_app_info.WebAppInfo")*, *\*\*extra_data: Any*)
:   Represents a menu button, which launches a [Web App](https://core.telegram.org/bots/webapps).

    Source: <https://core.telegram.org/bots/api#menubuttonwebapp>

    type*: Literal[MenuButtonType.WEB_APP]*
    :   Type of the button, must be *web_app*

    text*: str*
    :   Text on the button

    web_app*: [WebAppInfo](web_app_info.html#aiogram.types.web_app_info.WebAppInfo "aiogram.types.web_app_info.WebAppInfo")*
    :   Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method [`aiogram.methods.answer_web_app_query.AnswerWebAppQuery`](../methods/answer_web_app_query.html#aiogram.methods.answer_web_app_query.AnswerWebAppQuery "aiogram.methods.answer_web_app_query.AnswerWebAppQuery"). Alternatively, a `t.me` link to a Web App of the bot can be specified in the object instead of the Web App’s URL, in which case the Web App will be opened as if the user pressed the link
