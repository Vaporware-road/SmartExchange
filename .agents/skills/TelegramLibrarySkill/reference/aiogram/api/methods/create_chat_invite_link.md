# createChatInviteLink

> Source: [https://docs.aiogram.dev/en/latest/api/methods/create_chat_invite_link.html](https://docs.aiogram.dev/en/latest/api/methods/create_chat_invite_link.html)

Returns: `ChatInviteLink`

*class* aiogram.methods.create_chat_invite_link.CreateChatInviteLink(*\**, *chat_id: int | str*, *name: str | None = None*, *expire_date: datetime | timedelta | int | None = None*, *member_limit: int | None = None*, *creates_join_request: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method [`aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink`](revoke_chat_invite_link.html#aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink "aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink"). Returns the new invite link as [`aiogram.types.chat_invite_link.ChatInviteLink`](../types/chat_invite_link.html#aiogram.types.chat_invite_link.ChatInviteLink "aiogram.types.chat_invite_link.ChatInviteLink") object.

    Source: <https://core.telegram.org/bots/api#createchatinvitelink>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    name*: str | None*
    :   Invite link name; 0-32 characters

    expire_date*: DateTimeUnion | None*
    :   Point in time (Unix timestamp) when the link will expire

    member_limit*: int | None*
    :   The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999

    creates_join_request*: bool | None*
    :   `True`, if users joining the chat via the link need to be approved by chat administrators. If `True`, *member_limit* can’t be specified

## Usage

### As bot method

```
result: ChatInviteLink = await bot.create_chat_invite_link(...)
```

### Method as object

Imports:

- `from aiogram.methods.create_chat_invite_link import CreateChatInviteLink`
- alias: `from aiogram.methods import CreateChatInviteLink`

#### With specific bot

```
result: ChatInviteLink = await bot(CreateChatInviteLink(...))
```

#### As reply into Webhook in handler

```
return CreateChatInviteLink(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.create_invite_link()`](../types/chat.html#aiogram.types.chat.Chat.create_invite_link "aiogram.types.chat.Chat.create_invite_link")
