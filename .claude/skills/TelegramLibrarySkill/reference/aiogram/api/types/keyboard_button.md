# KeyboardButton

> Source: [https://docs.aiogram.dev/en/latest/api/types/keyboard_button.html](https://docs.aiogram.dev/en/latest/api/types/keyboard_button.html)

*class* aiogram.types.keyboard_button.KeyboardButton(*\**, *text: str*, *icon_custom_emoji_id: str | None = None*, *style: str | None = None*, *request_users: [KeyboardButtonRequestUsers](keyboard_button_request_users.html#aiogram.types.keyboard_button_request_users.KeyboardButtonRequestUsers "aiogram.types.keyboard_button_request_users.KeyboardButtonRequestUsers") | None = None*, *request_chat: [KeyboardButtonRequestChat](keyboard_button_request_chat.html#aiogram.types.keyboard_button_request_chat.KeyboardButtonRequestChat "aiogram.types.keyboard_button_request_chat.KeyboardButtonRequestChat") | None = None*, *request_managed_bot: [KeyboardButtonRequestManagedBot](keyboard_button_request_managed_bot.html#aiogram.types.keyboard_button_request_managed_bot.KeyboardButtonRequestManagedBot "aiogram.types.keyboard_button_request_managed_bot.KeyboardButtonRequestManagedBot") | None = None*, *request_contact: bool | None = None*, *request_location: bool | None = None*, *request_poll: [KeyboardButtonPollType](keyboard_button_poll_type.html#aiogram.types.keyboard_button_poll_type.KeyboardButtonPollType "aiogram.types.keyboard_button_poll_type.KeyboardButtonPollType") | None = None*, *web_app: [WebAppInfo](web_app_info.html#aiogram.types.web_app_info.WebAppInfo "aiogram.types.web_app_info.WebAppInfo") | None = None*, *request_user: [KeyboardButtonRequestUser](keyboard_button_request_user.html#aiogram.types.keyboard_button_request_user.KeyboardButtonRequestUser "aiogram.types.keyboard_button_request_user.KeyboardButtonRequestUser") | None = None*, *\*\*extra_data: Any*)
:   This object represents one button of the reply keyboard. At most one of the fields other than *text*, *icon_custom_emoji_id*, and *style* must be used to specify the type of the button. For simple text buttons, *String* can be used instead of this object to specify the button text.

    Source: <https://core.telegram.org/bots/api#keyboardbutton>

    text*: str*
    :   Text of the button. If none of the fields other than *text*, *icon_custom_emoji_id*, and *style* are used, it will be sent as a message when the button is pressed

    icon_custom_emoji_id*: str | None*
    :   *Optional*. Unique identifier of the custom emoji shown before the text of the button. Can only be used by bots that purchased additional usernames on [Fragment](https://fragment.com) or in the messages directly sent by the bot to private, group and supergroup chats if the owner of the bot has a Telegram Premium subscription

    style*: str | None*
    :   *Optional*. Style of the button. Must be one of ‘danger’ (red), ‘success’ (green) or ‘primary’ (blue). If omitted, then an app-specific style is used

    request_users*: [KeyboardButtonRequestUsers](keyboard_button_request_users.html#aiogram.types.keyboard_button_request_users.KeyboardButtonRequestUsers "aiogram.types.keyboard_button_request_users.KeyboardButtonRequestUsers") | None*
    :   *Optional*. If specified, pressing the button will open a list of suitable users. Identifiers of selected users will be sent to the bot in a ‘users_shared’ service message. Available in private chats only

    request_chat*: [KeyboardButtonRequestChat](keyboard_button_request_chat.html#aiogram.types.keyboard_button_request_chat.KeyboardButtonRequestChat "aiogram.types.keyboard_button_request_chat.KeyboardButtonRequestChat") | None*
    :   *Optional*. If specified, pressing the button will open a list of suitable chats. Tapping on a chat will send its identifier to the bot in a ‘chat_shared’ service message. Available in private chats only

    request_managed_bot*: [KeyboardButtonRequestManagedBot](keyboard_button_request_managed_bot.html#aiogram.types.keyboard_button_request_managed_bot.KeyboardButtonRequestManagedBot "aiogram.types.keyboard_button_request_managed_bot.KeyboardButtonRequestManagedBot") | None*
    :   *Optional*. If specified, pressing the button will ask the user to create and share a bot that will be managed by the current bot. Available for bots that enabled management of other bots in the [@BotFather](https://t.me/BotFather) Mini App. Available in private chats only

    request_contact*: bool | None*
    :   *Optional*. If `True`, the user’s phone number will be sent as a contact when the button is pressed. Available in private chats only

    request_location*: bool | None*
    :   *Optional*. If `True`, the user’s current location will be sent when the button is pressed. Available in private chats only

    request_poll*: [KeyboardButtonPollType](keyboard_button_poll_type.html#aiogram.types.keyboard_button_poll_type.KeyboardButtonPollType "aiogram.types.keyboard_button_poll_type.KeyboardButtonPollType") | None*
    :   *Optional*. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only

    web_app*: [WebAppInfo](web_app_info.html#aiogram.types.web_app_info.WebAppInfo "aiogram.types.web_app_info.WebAppInfo") | None*
    :   *Optional*. If specified, the described [Web App](https://core.telegram.org/bots/webapps) will be launched when the button is pressed. The Web App will be able to send a ‘web_app_data’ service message. Available in private chats only

    request_user*: [KeyboardButtonRequestUser](keyboard_button_request_user.html#aiogram.types.keyboard_button_request_user.KeyboardButtonRequestUser "aiogram.types.keyboard_button_request_user.KeyboardButtonRequestUser") | None*
    :   *Optional.* If specified, pressing the button will open a list of suitable users. Tapping on any user will send their identifier to the bot in a ‘user_shared’ service message. Available in private chats only

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>
