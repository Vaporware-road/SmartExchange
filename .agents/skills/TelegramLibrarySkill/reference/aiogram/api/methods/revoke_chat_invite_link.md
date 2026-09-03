# revokeChatInviteLink

> Source: [https://docs.aiogram.dev/en/latest/api/methods/revoke_chat_invite_link.html](https://docs.aiogram.dev/en/latest/api/methods/revoke_chat_invite_link.html)

Returns: `ChatInviteLink`

*class* aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink(*\**, *chat_id: int | str*, *invite_link: str*, *\*\*extra_data: Any*)
:   Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as [`aiogram.types.chat_invite_link.ChatInviteLink`](../types/chat_invite_link.html#aiogram.types.chat_invite_link.ChatInviteLink "aiogram.types.chat_invite_link.ChatInviteLink") object.

    Source: <https://core.telegram.org/bots/api#revokechatinvitelink>

    chat_id*: ChatIdUnion*
    :   Unique identifier of the target chat or username of the target channel in the format `@username`

    invite_link*: str*
    :   The invite link to revoke

## Usage

### As bot method

```
result: ChatInviteLink = await bot.revoke_chat_invite_link(...)
```

### Method as object

Imports:

- `from aiogram.methods.revoke_chat_invite_link import RevokeChatInviteLink`
- alias: `from aiogram.methods import RevokeChatInviteLink`

#### With specific bot

```
result: ChatInviteLink = await bot(RevokeChatInviteLink(...))
```

#### As reply into Webhook in handler

```
return RevokeChatInviteLink(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.revoke_invite_link()`](../types/chat.html#aiogram.types.chat.Chat.revoke_invite_link "aiogram.types.chat.Chat.revoke_invite_link")
