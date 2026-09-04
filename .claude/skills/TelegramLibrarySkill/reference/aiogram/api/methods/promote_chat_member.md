# promoteChatMember

> Source: [https://docs.aiogram.dev/en/latest/api/methods/promote_chat_member.html](https://docs.aiogram.dev/en/latest/api/methods/promote_chat_member.html)

Returns: `bool`

*class* aiogram.methods.promote_chat_member.PromoteChatMember(*\**, *chat_id: int | str*, *user_id: int*, *is_anonymous: bool | None = None*, *can_manage_chat: bool | None = None*, *can_delete_messages: bool | None = None*, *can_manage_video_chats: bool | None = None*, *can_restrict_members: bool | None = None*, *can_promote_members: bool | None = None*, *can_change_info: bool | None = None*, *can_invite_users: bool | None = None*, *can_post_stories: bool | None = None*, *can_edit_stories: bool | None = None*, *can_delete_stories: bool | None = None*, *can_post_messages: bool | None = None*, *can_edit_messages: bool | None = None*, *can_pin_messages: bool | None = None*, *can_manage_topics: bool | None = None*, *can_manage_direct_messages: bool | None = None*, *can_manage_tags: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass `False` for all boolean parameters to demote a user. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#promotechatmember>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target channel in the format `@username`

    user_id*: int*
    :   Unique identifier of the target user

    is_anonymous*: bool | None*
    :   Pass `True` if the administrator’s presence in the chat is hidden

    can_manage_chat*: bool | None*
    :   Pass `True` if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages, ignore slow mode, and send messages to the chat without paying Telegram Stars. Implied by any other administrator privilege

    can_delete_messages*: bool | None*
    :   Pass `True` if the administrator can delete messages of other users

    can_manage_video_chats*: bool | None*
    :   Pass `True` if the administrator can manage video chats

    can_restrict_members*: bool | None*
    :   Pass `True` if the administrator can restrict, ban or unban chat members, or access supergroup statistics. For backward compatibility, defaults to `True` for promotions of channel administrators

    can_promote_members*: bool | None*
    :   Pass `True` if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by him)

    can_change_info*: bool | None*
    :   Pass `True` if the administrator can change chat title, photo and other settings

    can_invite_users*: bool | None*
    :   Pass `True` if the administrator can invite new users to the chat

    can_post_stories*: bool | None*
    :   Pass `True` if the administrator can post stories to the chat

    can_edit_stories*: bool | None*
    :   Pass `True` if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat’s story archive

    can_delete_stories*: bool | None*
    :   Pass `True` if the administrator can delete stories posted by other users

    can_post_messages*: bool | None*
    :   Pass `True` if the administrator can post messages in the channel, approve suggested posts, or access channel statistics; for channels only

    can_edit_messages*: bool | None*
    :   Pass `True` if the administrator can edit messages of other users and can pin messages; for channels only

    can_pin_messages*: bool | None*
    :   Pass `True` if the administrator can pin messages; for supergroups only

    can_manage_topics*: bool | None*
    :   Pass `True` if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only

    can_manage_direct_messages*: bool | None*
    :   Pass `True` if the administrator can manage direct messages within the channel and decline suggested posts; for channels only

    can_manage_tags*: bool | None*
    :   Pass `True` if the administrator can edit the tags of regular members; for groups and supergroups only

## Usage

### As bot method

```
result: bool = await bot.promote_chat_member(...)
```

### Method as object

Imports:

- `from aiogram.methods.promote_chat_member import PromoteChatMember`
- alias: `from aiogram.methods import PromoteChatMember`

#### With specific bot

```
result: bool = await bot(PromoteChatMember(...))
```

#### As reply into Webhook in handler

```
return PromoteChatMember(...)
```

### As shortcut from received object

- [`aiogram.types.chat.Chat.promote()`](../types/chat.html#aiogram.types.chat.Chat.promote "aiogram.types.chat.Chat.promote")
