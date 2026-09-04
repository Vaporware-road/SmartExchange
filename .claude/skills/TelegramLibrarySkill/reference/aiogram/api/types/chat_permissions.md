# ChatPermissions

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_permissions.html](https://docs.aiogram.dev/en/latest/api/types/chat_permissions.html)

*class* aiogram.types.chat_permissions.ChatPermissions(*\**, *can_send_messages: bool | None = None*, *can_send_audios: bool | None = None*, *can_send_documents: bool | None = None*, *can_send_photos: bool | None = None*, *can_send_videos: bool | None = None*, *can_send_video_notes: bool | None = None*, *can_send_voice_notes: bool | None = None*, *can_send_polls: bool | None = None*, *can_send_other_messages: bool | None = None*, *can_add_web_page_previews: bool | None = None*, *can_react_to_messages: bool | None = None*, *can_edit_tag: bool | None = None*, *can_change_info: bool | None = None*, *can_invite_users: bool | None = None*, *can_pin_messages: bool | None = None*, *can_manage_topics: bool | None = None*, *\*\*extra_data: Any*)
:   Describes actions that a non-administrator user is allowed to take in a chat.

    Source: <https://core.telegram.org/bots/api#chatpermissions>

    can_send_messages*: bool | None*
    :   *Optional*. `True`, if the user is allowed to send text messages, rich messages, contacts, giveaways, giveaway winners, invoices, locations and venues

    can_send_audios*: bool | None*
    :   *Optional*. `True`, if the user is allowed to send audios

    can_send_documents*: bool | None*
    :   *Optional*. `True`, if the user is allowed to send documents

    can_send_photos*: bool | None*
    :   *Optional*. `True`, if the user is allowed to send photos

    can_send_videos*: bool | None*
    :   *Optional*. `True`, if the user is allowed to send videos

    can_send_video_notes*: bool | None*
    :   *Optional*. `True`, if the user is allowed to send video notes

    can_send_voice_notes*: bool | None*
    :   *Optional*. `True`, if the user is allowed to send voice notes

    can_send_polls*: bool | None*
    :   *Optional*. `True`, if the user is allowed to send polls and checklists

    can_send_other_messages*: bool | None*
    :   *Optional*. `True`, if the user is allowed to send animations, games, stickers and use inline bots

    can_add_web_page_previews*: bool | None*
    :   *Optional*. `True`, if the user is allowed to add web page previews to their messages

    can_react_to_messages*: bool | None*
    :   *Optional*. `True`, if the user is allowed to react to messages. If omitted, defaults to the value of *can_send_messages*

    can_edit_tag*: bool | None*
    :   *Optional*. `True`, if the user is allowed to edit their own tag. If omitted, defaults to the value of *can_pin_messages*

    can_change_info*: bool | None*
    :   *Optional*. `True`, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups

    can_invite_users*: bool | None*
    :   *Optional*. `True`, if the user is allowed to invite new users to the chat

    can_pin_messages*: bool | None*
    :   *Optional*. `True`, if the user is allowed to pin messages. Ignored in public supergroups

    can_manage_topics*: bool | None*
    :   *Optional*. `True`, if the user is allowed to create forum topics. If omitted, defaults to the value of can_pin_messages
