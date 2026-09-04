# KeyboardButtonRequestChat

> Source: [https://docs.aiogram.dev/en/latest/api/types/keyboard_button_request_chat.html](https://docs.aiogram.dev/en/latest/api/types/keyboard_button_request_chat.html)

*class* aiogram.types.keyboard_button_request_chat.KeyboardButtonRequestChat(*\**, *request_id: int*, *chat_is_channel: bool*, *chat_is_forum: bool | None = None*, *chat_has_username: bool | None = None*, *chat_is_created: bool | None = None*, *user_administrator_rights: [ChatAdministratorRights](chat_administrator_rights.html#aiogram.types.chat_administrator_rights.ChatAdministratorRights "aiogram.types.chat_administrator_rights.ChatAdministratorRights") | None = None*, *bot_administrator_rights: [ChatAdministratorRights](chat_administrator_rights.html#aiogram.types.chat_administrator_rights.ChatAdministratorRights "aiogram.types.chat_administrator_rights.ChatAdministratorRights") | None = None*, *bot_is_member: bool | None = None*, *request_title: bool | None = None*, *request_username: bool | None = None*, *request_photo: bool | None = None*, *\*\*extra_data: Any*)
:   This object defines the criteria used to request a suitable chat. Information about the selected chat will be shared with the bot when the corresponding button is pressed. The bot will be granted requested rights in the chat if appropriate. [More about requesting chats »](https://core.telegram.org/bots/features#chat-and-user-selection).

    Source: <https://core.telegram.org/bots/api#keyboardbuttonrequestchat>

    request_id*: int*
    :   Signed 32-bit identifier of the request, which will be received back in the [`aiogram.types.chat_shared.ChatShared`](chat_shared.html#aiogram.types.chat_shared.ChatShared "aiogram.types.chat_shared.ChatShared") object. Must be unique within the message

    chat_is_channel*: bool*
    :   Pass `True` to request a channel chat, pass `False` to request a group or a supergroup chat

    chat_is_forum*: bool | None*
    :   *Optional*. Pass `True` to request a forum supergroup, pass `False` to request a non-forum chat. If not specified, no additional restrictions are applied

    chat_has_username*: bool | None*
    :   *Optional*. Pass `True` to request a supergroup or a channel with a username, pass `False` to request a chat without a username. If not specified, no additional restrictions are applied

    chat_is_created*: bool | None*
    :   *Optional*. Pass `True` to request a chat owned by the user. Otherwise, no additional restrictions are applied

    user_administrator_rights*: [ChatAdministratorRights](chat_administrator_rights.html#aiogram.types.chat_administrator_rights.ChatAdministratorRights "aiogram.types.chat_administrator_rights.ChatAdministratorRights") | None*
    :   *Optional*. A JSON-serialized object listing the required administrator rights of the user in the chat. The rights must be a superset of *bot_administrator_rights*. If not specified, no additional restrictions are applied

    bot_administrator_rights*: [ChatAdministratorRights](chat_administrator_rights.html#aiogram.types.chat_administrator_rights.ChatAdministratorRights "aiogram.types.chat_administrator_rights.ChatAdministratorRights") | None*
    :   *Optional*. A JSON-serialized object listing the required administrator rights of the bot in the chat. The rights must be a subset of *user_administrator_rights*. If not specified, no additional restrictions are applied

    bot_is_member*: bool | None*
    :   *Optional*. Pass `True` to request a chat with the bot as a member. Otherwise, no additional restrictions are applied

    request_title*: bool | None*
    :   *Optional*. Pass `True` to request the chat’s title

    request_username*: bool | None*
    :   *Optional*. Pass `True` to request the chat’s username

    request_photo*: bool | None*
    :   *Optional*. Pass `True` to request the chat’s photo
