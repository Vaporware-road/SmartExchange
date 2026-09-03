# editChatInviteLink

> Source: [https://docs.aiogram.dev/en/latest/api/methods/edit_chat_invite_link.html](https://docs.aiogram.dev/en/latest/api/methods/edit_chat_invite_link.html)

Returns: `ChatInviteLink`

*class* aiogram.methods.edit_chat_invite_link.EditChatInviteLink(*\**, *chat_id: int | str*, *invite_link: str*, *name: str | None = None*, *expire_date: datetime | timedelta | int | None = None*, *member_limit: int | None = None*, *creates_join_request: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a [`aiogram.types.chat_invite_link.ChatInviteLink`](../types/chat_invite_link.html#aiogram.types.chat_invite_link.ChatInviteLink "aiogram.types.chat_invite_link.ChatInviteLink") object.

    Source: <https://core.telegram.org/bots/api#editchatinvitelink>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    invite_link*: str*
    :   The invite link to edit

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
result: ChatInviteLink = await bot.edit_chat_invite_link(...)
```

### Method as object

Imports:

- `from aiogram.methods.edit_chat_invite_link import EditChatInviteLink`
- alias: `from aiogram.methods import EditChatInviteLink`

#### With specific bot

```
result: ChatInviteLink = await bot(EditChatInviteLink(...))
```

#### As reply into Webhook in handler

```
return EditChatInviteLink(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.edit_invite_link()`](../types/chat.html#aiogram.types.chat.Chat.edit_invite_link "aiogram.types.chat.Chat.edit_invite_link")
