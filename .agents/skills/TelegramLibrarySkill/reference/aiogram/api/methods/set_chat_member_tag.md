# setChatMemberTag

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_chat_member_tag.html](https://docs.aiogram.dev/en/latest/api/methods/set_chat_member_tag.html)

Returns: `bool`

*class* aiogram.methods.set_chat_member_tag.SetChatMemberTag(*\**, *chat_id: int | str*, *user_id: int*, *tag: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to set a tag for a regular member in a group or a supergroup. The bot must be an administrator in the chat for this to work and must have the *can_manage_tags* administrator right. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setchatmembertag>

    chat_id*: int | str*
    :   Unique identifier for the target chat or username of the target supergroup in the format `@username`

    user_id*: int*
    :   Unique identifier of the target user

    tag*: str | None*
    :   New tag for the member; 0-16 characters, emoji are not allowed

## Usage

### As bot method

```
result: bool = await bot.set_chat_member_tag(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_chat_member_tag import SetChatMemberTag`
- alias: `from aiogram.methods import SetChatMemberTag`

#### With specific bot

```
result: bool = await bot(SetChatMemberTag(...))
```

#### As reply into Webhook in handler

```
return SetChatMemberTag(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.set_member_tag()`](../types/chat.html#aiogram.types.chat.Chat.set_member_tag "aiogram.types.chat.Chat.set_member_tag")
