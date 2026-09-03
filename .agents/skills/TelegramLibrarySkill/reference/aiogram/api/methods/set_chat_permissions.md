# setChatPermissions

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_chat_permissions.html](https://docs.aiogram.dev/en/latest/api/methods/set_chat_permissions.html)

Returns: `bool`

*class* aiogram.methods.set_chat_permissions.SetChatPermissions(*\**, *chat_id: int | str*, *permissions: [ChatPermissions](../types/chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions")*, *use_independent_chat_permissions: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the *can_restrict_members* administrator rights. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setchatpermissions>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    permissions*: [ChatPermissions](../types/chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions")*
    :   A JSON-serialized object for new default chat permissions

    use_independent_chat_permissions*: bool | None*
    :   Pass `True` if chat permissions are set independently. Otherwise, the *can_send_other_messages* and *can_add_web_page_previews* permissions will imply the *can_send_messages*, *can_send_audios*, *can_send_documents*, *can_send_photos*, *can_send_videos*, *can_send_video_notes*, and *can_send_voice_notes* permissions; the *can_send_polls* permission will imply the *can_send_messages* permission

## Usage

### As bot method

```
result: bool = await bot.set_chat_permissions(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_chat_permissions import SetChatPermissions`
- alias: `from aiogram.methods import SetChatPermissions`

#### With specific bot

```
result: bool = await bot(SetChatPermissions(...))
```

#### As reply into Webhook in handler

```
return SetChatPermissions(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.set_permissions()`](../types/chat.html#aiogram.types.chat.Chat.set_permissions "aiogram.types.chat.Chat.set_permissions")
