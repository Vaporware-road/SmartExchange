# ChatMemberRestricted

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_member_restricted.html](https://docs.aiogram.dev/en/latest/api/types/chat_member_restricted.html)

*class* aiogram.types.chat_member_restricted.ChatMemberRestricted(*\**, *status: Literal[ChatMemberStatus.RESTRICTED] = ChatMemberStatus.RESTRICTED*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *is_member: bool*, *can_send_messages: bool*, *can_send_audios: bool*, *can_send_documents: bool*, *can_send_photos: bool*, *can_send_videos: bool*, *can_send_video_notes: bool*, *can_send_voice_notes: bool*, *can_send_polls: bool*, *can_send_other_messages: bool*, *can_add_web_page_previews: bool*, *can_react_to_messages: bool*, *can_edit_tag: bool*, *can_change_info: bool*, *can_invite_users: bool*, *can_pin_messages: bool*, *can_manage_topics: bool*, *until_date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *tag: str | None = None*, *\*\*extra_data: Any*)
:   Represents a [chat member](https://core.telegram.org/bots/api#chatmember) that is under certain restrictions in the chat. Supergroups only.

    Source: <https://core.telegram.org/bots/api#chatmemberrestricted>

    status*: Literal[ChatMemberStatus.RESTRICTED]*
    :   The member’s status in the chat, always ‘restricted’

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Information about the user

    is_member*: bool*
    :   `True`, if the user is a member of the chat at the moment of the request

    can_send_messages*: bool*
    :   `True`, if the user is allowed to send text messages, rich messages, contacts, giveaways, giveaway winners, invoices, locations and venues

    can_send_audios*: bool*
    :   `True`, if the user is allowed to send audios

    can_send_documents*: bool*
    :   `True`, if the user is allowed to send documents

    can_send_photos*: bool*
    :   `True`, if the user is allowed to send photos

    can_send_videos*: bool*
    :   `True`, if the user is allowed to send videos

    can_send_video_notes*: bool*
    :   `True`, if the user is allowed to send video notes

    can_send_voice_notes*: bool*
    :   `True`, if the user is allowed to send voice notes

    can_send_polls*: bool*
    :   `True`, if the user is allowed to send polls and checklists

    can_send_other_messages*: bool*
    :   `True`, if the user is allowed to send animations, games, stickers and use inline bots

    can_add_web_page_previews*: bool*
    :   `True`, if the user is allowed to add web page previews to their messages

    can_react_to_messages*: bool*
    :   `True`, if the user is allowed to react to messages

    can_edit_tag*: bool*
    :   `True`, if the user is allowed to edit their own tag

    can_change_info*: bool*
    :   `True`, if the user is allowed to change the chat title, photo and other settings

    can_invite_users*: bool*
    :   `True`, if the user is allowed to invite new users to the chat

    can_pin_messages*: bool*
    :   `True`, if the user is allowed to pin messages

    can_manage_topics*: bool*
    :   `True`, if the user is allowed to create forum topics

    until_date*: DateTime*
    :   Date when restrictions will be lifted for this user; Unix time. If 0, then the user is restricted forever

    tag*: str | None*
    :   *Optional*. Tag of the member
