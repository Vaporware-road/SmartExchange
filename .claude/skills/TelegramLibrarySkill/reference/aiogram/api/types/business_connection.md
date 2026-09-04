# BusinessConnection

> Source: [https://docs.aiogram.dev/en/latest/api/types/business_connection.html](https://docs.aiogram.dev/en/latest/api/types/business_connection.html)

*class* aiogram.types.business_connection.BusinessConnection(*\**, *id: str*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *user_chat_id: int*, *date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *is_enabled: bool*, *rights: [BusinessBotRights](business_bot_rights.html#aiogram.types.business_bot_rights.BusinessBotRights "aiogram.types.business_bot_rights.BusinessBotRights") | None = None*, *can_reply: bool | None = None*, *\*\*extra_data: Any*)
:   Describes the connection of the bot with a business account.

    Source: <https://core.telegram.org/bots/api#businessconnection>

    id*: str*
    :   Unique identifier of the business connection

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Business account user that created the business connection

    user_chat_id*: int*
    :   Identifier of a private chat with the user who created the business connection. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier

    date*: DateTime*
    :   Date the connection was established in Unix time

    is_enabled*: bool*
    :   `True`, if the connection is active

    rights*: [BusinessBotRights](business_bot_rights.html#aiogram.types.business_bot_rights.BusinessBotRights "aiogram.types.business_bot_rights.BusinessBotRights") | None*
    :   *Optional*. Rights of the business bot

    can_reply*: bool | None*
    :   True, if the bot can act on behalf of the business account in chats that were active in the last 24 hours

        Deprecated since version API:9.0: <https://core.telegram.org/bots/api-changelog#april-11-2025>
