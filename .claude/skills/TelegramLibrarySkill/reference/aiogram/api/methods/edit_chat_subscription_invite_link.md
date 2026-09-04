# editChatSubscriptionInviteLink

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_chat_subscription_invite_link.html](https://docs.aiogram.dev/en/latest/api/methods/edit_chat_subscription_invite_link.html)

Returns: `ChatInviteLink`

*class* aiogram.methods.edit_chat_subscription_invite_link.EditChatSubscriptionInviteLink(*\**, *chat_id: int | str*, *invite_link: str*, *name: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to edit a subscription invite link created by the bot. The bot must have the *can_invite_users* administrator rights. Returns the edited invite link as a [`aiogram.types.chat_invite_link.ChatInviteLink`](../types/chat_invite_link.html#aiogram.types.chat_invite_link.ChatInviteLink "aiogram.types.chat_invite_link.ChatInviteLink") object.

    Source: <https://core.telegram.org/bots/api#editchatsubscriptioninvitelink>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    invite_link*: str*
    :   The invite link to edit

    name*: str | None*
    :   Invite link name; 0-32 characters

## Usage

### As bot method

```
result: ChatInviteLink = await bot.edit_chat_subscription_invite_link(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_chat_subscription_invite_link import EditChatSubscriptionInviteLink`
- alias: `from aiogram.methods import EditChatSubscriptionInviteLink`

#### With specific bot

```
result: ChatInviteLink = await bot(EditChatSubscriptionInviteLink(...))
```

#### As reply into Webhook in handler

```
return EditChatSubscriptionInviteLink(...)
```
