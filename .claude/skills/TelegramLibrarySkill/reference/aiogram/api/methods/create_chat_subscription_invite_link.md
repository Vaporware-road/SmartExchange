# createChatSubscriptionInviteLink

> Source: [https://docs.aiogram.dev/en/latest/api/methods/create_chat_subscription_invite_link.html](https://docs.aiogram.dev/en/latest/api/methods/create_chat_subscription_invite_link.html)

Returns: `ChatInviteLink`

*class* aiogram.methods.create_chat_subscription_invite_link.CreateChatSubscriptionInviteLink(*\**, *chat_id: int | str*, *subscription_period: datetime | timedelta | int*, *subscription_price: int*, *name: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to create a [subscription invite link](https://telegram.org/blog/superchannels-star-reactions-subscriptions#star-subscriptions) for a channel chat. The bot must have the *can_invite_users* administrator rights. The link can be edited using the method [`aiogram.methods.edit_chat_subscription_invite_link.EditChatSubscriptionInviteLink`](edit_chat_subscription_invite_link.html#aiogram.methods.edit_chat_subscription_invite_link.EditChatSubscriptionInviteLink "aiogram.methods.edit_chat_subscription_invite_link.EditChatSubscriptionInviteLink") or revoked using the method [`aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink`](revoke_chat_invite_link.html#aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink "aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink"). Returns the new invite link as a [`aiogram.types.chat_invite_link.ChatInviteLink`](../types/chat_invite_link.html#aiogram.types.chat_invite_link.ChatInviteLink "aiogram.types.chat_invite_link.ChatInviteLink") object.

    Source: <https://core.telegram.org/bots/api#createchatsubscriptioninvitelink>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target channel chat or username of the target channel in the format `@username`

    subscription_period*: DateTimeUnion*
    :   The number of seconds the subscription will be active for before the next payment. Currently, it must always be 2592000 (30 days)

    subscription_price*: int*
    :   The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat; 1-10000

    name*: str | None*
    :   Invite link name; 0-32 characters

## Usage

### As bot method

```
result: ChatInviteLink = await bot.create_chat_subscription_invite_link(...)
```

### Method as object

Imports:

- `from aiogram.methods.create_chat_subscription_invite_link import CreateChatSubscriptionInviteLink`
- alias: `from aiogram.methods import CreateChatSubscriptionInviteLink`

#### With specific bot

```
result: ChatInviteLink = await bot(CreateChatSubscriptionInviteLink(...))
```

#### As reply into Webhook in handler

```
return CreateChatSubscriptionInviteLink(...)
```
