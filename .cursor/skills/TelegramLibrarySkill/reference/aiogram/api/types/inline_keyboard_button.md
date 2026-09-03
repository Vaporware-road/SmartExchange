# InlineKeyboardButton

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_keyboard_button.html](https://docs.aiogram.dev/en/latest/api/types/inline_keyboard_button.html)

*class* aiogram.types.inline_keyboard_button.InlineKeyboardButton(*\**, *text: str*, *icon_custom_emoji_id: str | None = None*, *style: str | None = None*, *url: str | None = None*, *callback_data: str | None = None*, *web_app: [WebAppInfo](web_app_info.html#aiogram.types.web_app_info.WebAppInfo "aiogram.types.web_app_info.WebAppInfo") | None = None*, *login_url: [LoginUrl](login_url.html#aiogram.types.login_url.LoginUrl "aiogram.types.login_url.LoginUrl") | None = None*, *switch_inline_query: str | None = None*, *switch_inline_query_current_chat: str | None = None*, *switch_inline_query_chosen_chat: [SwitchInlineQueryChosenChat](switch_inline_query_chosen_chat.html#aiogram.types.switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat "aiogram.types.switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat") | None = None*, *copy_text: [CopyTextButton](copy_text_button.html#aiogram.types.copy_text_button.CopyTextButton "aiogram.types.copy_text_button.CopyTextButton") | None = None*, *callback_game: [CallbackGame](callback_game.html#aiogram.types.callback_game.CallbackGame "aiogram.types.callback_game.CallbackGame") | None = None*, *pay: bool | None = None*, *\*\*extra_data: Any*)
:   This object represents one button of an inline keyboard. Exactly one of the fields other than *text*, *icon_custom_emoji_id*, and *style* must be used to specify the type of the button.

    Source: <https://core.telegram.org/bots/api#inlinekeyboardbutton>

    text*: str*
    :   Label text on the button

    icon_custom_emoji_id*: str | None*
    :   *Optional*. Unique identifier of the custom emoji shown before the text of the button. Can only be used by bots that purchased additional usernames on [Fragment](https://fragment.com) or in the messages directly sent by the bot to private, group and supergroup chats if the owner of the bot has a Telegram Premium subscription

    style*: str | None*
    :   *Optional*. Style of the button. Must be one of ‘danger’ (red), ‘success’ (green) or ‘primary’ (blue). If omitted, then an app-specific style is used

    url*: str | None*
    :   *Optional*. HTTP or tg:// URL to be opened when the button is pressed. Links `tg://user?id=<user_id>` can be used to mention a user by their identifier without using a username, if this is allowed by their privacy settings

    callback_data*: str | None*
    :   *Optional*. Data to be sent in a [callback query](https://core.telegram.org/bots/api#callbackquery) to the bot when the button is pressed, 1-64 bytes

    web_app*: [WebAppInfo](web_app_info.html#aiogram.types.web_app_info.WebAppInfo "aiogram.types.web_app_info.WebAppInfo") | None*
    :   *Optional*. Description of the [Web App](https://core.telegram.org/bots/webapps) that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method [`aiogram.methods.answer_web_app_query.AnswerWebAppQuery`](../methods/answer_web_app_query.html#aiogram.methods.answer_web_app_query.AnswerWebAppQuery "aiogram.methods.answer_web_app_query.AnswerWebAppQuery"). Available only in private chats between a user and the bot. Not supported for messages sent on behalf of a business account

    login_url*: [LoginUrl](login_url.html#aiogram.types.login_url.LoginUrl "aiogram.types.login_url.LoginUrl") | None*
    :   *Optional*. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the [Telegram Login Widget](https://core.telegram.org/widgets/login)

    switch_inline_query*: str | None*
    :   *Optional*. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot’s username and the specified inline query in the input field. May be empty, in which case just the bot’s username will be inserted. Not supported for messages sent in channel direct messages chats and on behalf of a business account

    switch_inline_query_current_chat*: str | None*
    :   *Optional*. If set, pressing the button will insert the bot’s username and the specified inline query in the current chat’s input field. May be empty, in which case only the bot’s username will be inserted

    switch_inline_query_chosen_chat*: [SwitchInlineQueryChosenChat](switch_inline_query_chosen_chat.html#aiogram.types.switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat "aiogram.types.switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat") | None*
    :   *Optional*. If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot’s username and the specified inline query in the input field. Not supported for messages sent in channel direct messages chats and on behalf of a business account

    copy_text*: [CopyTextButton](copy_text_button.html#aiogram.types.copy_text_button.CopyTextButton "aiogram.types.copy_text_button.CopyTextButton") | None*
    :   *Optional*. Description of the button that copies the specified text to the clipboard

    callback_game*: [CallbackGame](callback_game.html#aiogram.types.callback_game.CallbackGame "aiogram.types.callback_game.CallbackGame") | None*
    :   *Optional*. Description of the game that will be launched when the user presses the button

    pay*: bool | None*
    :   *Optional*. Specify `True`, to send a [Pay button](https://core.telegram.org/bots/api#payments). Substrings ‘⭐’ and ‘XTR’ in the buttons’s text will be replaced with a Telegram Star icon
