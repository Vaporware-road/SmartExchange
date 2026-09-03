# restrictChatMember

> Source: [https://docs.aiogram.dev/en/latest/api/methods/restrict_chat_member.html](https://docs.aiogram.dev/en/latest/api/methods/restrict_chat_member.html)

Returns: `bool`

*class* aiogram.methods.restrict_chat_member.RestrictChatMember(*\**, *chat_id: int | str*, *user_id: int*, *permissions: [ChatPermissions](../types/chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions")*, *use_independent_chat_permissions: bool | None = None*, *until_date: datetime | timedelta | int | None = None*, *\*\*extra_data: Any*)
:   Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass `True` for all permissions to lift restrictions from a user. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#restrictchatmember>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    user_id*: int*
    :   Unique identifier of the target user

    permissions*: [ChatPermissions](../types/chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions")*
    :   A JSON-serialized object for new user permissions

    use_independent_chat_permissions*: bool | None*
    :   Pass `True` if chat permissions are set independently. Otherwise, the *can_send_other_messages* and *can_add_web_page_previews* permissions will imply the *can_send_messages*, *can_send_audios*, *can_send_documents*, *can_send_photos*, *can_send_videos*, *can_send_video_notes*, and *can_send_voice_notes* permissions; the *can_send_polls* permission will imply the *can_send_messages* permission

    until_date*: DateTimeUnion | None*
    :   Date when restrictions will be lifted for the user; Unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever

## Usage

### As bot method

```
result: bool = await bot.restrict_chat_member(...)
```

### Method as object

Imports:

- `from aiogram.methods.restrict_chat_member import RestrictChatMember`
- alias: `from aiogram.methods import RestrictChatMember`

#### With specific bot

```
result: bool = await bot(RestrictChatMember(...))
```

#### As reply into Webhook in handler

```
return RestrictChatMember(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.restrict()`](../types/chat.html#aiogram.types.chat.Chat.restrict "aiogram.types.chat.Chat.restrict")
