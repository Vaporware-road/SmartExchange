# WebAppData

> Source: [https://docs.aiogram.dev/en/latest/api/types/web_app_data.html](https://docs.aiogram.dev/en/latest/api/types/web_app_data.html)

*class* aiogram.types.web_app_data.WebAppData(*\**, *data: str*, *button_text: str*, *\*\*extra_data: Any*)
:   Describes data sent from a [Web App](https://core.telegram.org/bots/webapps) to the bot.

    Source: <https://core.telegram.org/bots/api#webappdata>

    data*: str*
    :   The data. Be aware that a bad client can send arbitrary data in this field

    button_text*: str*
    :   Text of the *web_app* keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field
