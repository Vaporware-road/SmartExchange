# ChatInviteLink

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_invite_link.html](https://docs.aiogram.dev/en/latest/api/types/chat_invite_link.html)

*class* aiogram.types.chat_invite_link.ChatInviteLink(*\**, *invite_link: str*, *creator: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *creates_join_request: bool*, *is_primary: bool*, *is_revoked: bool*, *name: str | None = None*, *expire_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *member_limit: int | None = None*, *pending_join_request_count: int | None = None*, *subscription_period: int | None = None*, *subscription_price: int | None = None*, *\*\*extra_data: Any*)
:   Represents an invite link for a chat.

    Source: <https://core.telegram.org/bots/api#chatinvitelink>

    invite_link*: str*
    :   The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with ‘…’

    creator*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Creator of the link

    creates_join_request*: bool*
    :   `True`, if users joining the chat via the link need to be approved by chat administrators

    is_primary*: bool*
    :   `True`, if the link is primary

    is_revoked*: bool*
    :   `True`, if the link is revoked

    name*: str | None*
    :   *Optional*. Invite link name

    expire_date*: DateTime | None*
    :   *Optional*. Point in time (Unix timestamp) when the link will expire or has been expired

    member_limit*: int | None*
    :   *Optional*. The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999

    pending_join_request_count*: int | None*
    :   *Optional*. Number of pending join requests created using this link

    subscription_period*: int | None*
    :   *Optional*. The number of seconds the subscription will be active for before the next payment

    subscription_price*: int | None*
    :   *Optional*. The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat using the link
