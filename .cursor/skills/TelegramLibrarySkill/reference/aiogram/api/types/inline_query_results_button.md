# InlineQueryResultsButton

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_results_button.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_results_button.html)

*class* aiogram.types.inline_query_results_button.InlineQueryResultsButton(*\**, *text: str*, *web_app: [WebAppInfo](web_app_info.html#aiogram.types.web_app_info.WebAppInfo "aiogram.types.web_app_info.WebAppInfo") | None = None*, *start_parameter: str | None = None*, *\*\*extra_data: Any*)
:   This object represents a button to be shown above inline query results. You **must** use exactly one of the optional fields.

    Source: <https://core.telegram.org/bots/api#inlinequeryresultsbutton>

    text*: str*
    :   Label text on the button

    web_app*: [WebAppInfo](web_app_info.html#aiogram.types.web_app_info.WebAppInfo "aiogram.types.web_app_info.WebAppInfo") | None*
    :   *Optional*. Description of the [Web App](https://core.telegram.org/bots/webapps) that will be launched when the user presses the button. The Web App will be able to switch back to the inline mode using the method [switchInlineQuery](https://core.telegram.org/bots/webapps#initializing-mini-apps) inside the Web App

    start_parameter*: str | None*
    :   *Optional*. [Deep-linking](https://core.telegram.org/bots/features#deep-linking) parameter for the /start message sent to the bot when a user presses the button. 1-64 characters, only `A-Z`, `a-z`, `0-9`, `_` and `-` are allowed
