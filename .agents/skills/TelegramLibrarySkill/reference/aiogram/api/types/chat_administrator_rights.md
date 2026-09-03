# ChatAdministratorRights

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_administrator_rights.html](https://docs.aiogram.dev/en/latest/api/types/chat_administrator_rights.html)

*class* aiogram.types.chat_administrator_rights.ChatAdministratorRights(*\**, *is_anonymous: bool*, *can_manage_chat: bool*, *can_delete_messages: bool*, *can_manage_video_chats: bool*, *can_restrict_members: bool*, *can_promote_members: bool*, *can_change_info: bool*, *can_invite_users: bool*, *can_post_stories: bool*, *can_edit_stories: bool*, *can_delete_stories: bool*, *can_post_messages: bool | None = None*, *can_edit_messages: bool | None = None*, *can_pin_messages: bool | None = None*, *can_manage_topics: bool | None = None*, *can_manage_direct_messages: bool | None = None*, *can_manage_tags: bool | None = None*, *\*\*extra_data: Any*)
:   Represents the rights of an administrator in a chat.

    Source: <https://core.telegram.org/bots/api#chatadministratorrights>

    is_anonymous*: bool*
    :   `True`, if the user’s presence in the chat is hidden

    can_manage_chat*: bool*
    :   `True`, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages, ignore slow mode, and send messages to the chat without paying Telegram Stars. Implied by any other administrator privilege

    can_delete_messages*: bool*
    :   `True`, if the administrator can delete messages of other users

    can_manage_video_chats*: bool*
    :   `True`, if the administrator can manage video chats

    can_restrict_members*: bool*
    :   `True`, if the administrator can restrict, ban or unban chat members, or access supergroup statistics

    can_promote_members*: bool*
    :   `True`, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user)

    can_change_info*: bool*
    :   `True`, if the user is allowed to change the chat title, photo and other settings

    can_invite_users*: bool*
    :   `True`, if the user is allowed to invite new users to the chat

    can_post_stories*: bool*
    :   `True`, if the administrator can post stories to the chat

    can_edit_stories*: bool*
    :   `True`, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat’s story archive

    can_delete_stories*: bool*
    :   `True`, if the administrator can delete stories posted by other users

    can_post_messages*: bool | None*
    :   *Optional*. `True`, if the administrator can post messages in the channel, approve suggested posts, or access channel statistics; for channels only

    can_edit_messages*: bool | None*
    :   *Optional*. `True`, if the administrator can edit messages of other users and can pin messages; for channels only

    can_pin_messages*: bool | None*
    :   *Optional*. `True`, if the user is allowed to pin messages; for groups and supergroups only

    can_manage_topics*: bool | None*
    :   *Optional*. `True`, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only

    can_manage_direct_messages*: bool | None*
    :   *Optional*. `True`, if the administrator can manage direct messages of the channel and decline suggested posts; for channels only

    can_manage_tags*: bool | None*
    :   *Optional*. `True`, if the administrator can edit the tags of regular members; for groups and supergroups only. If omitted, defaults to the value of can_pin_messages
