# Chat

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat.html](https://docs.aiogram.dev/en/latest/api/types/chat.html)

*class* aiogram.types.chat.Chat(*\**, *id: int*, *type: str*, *title: str | None = None*, *username: str | None = None*, *first_name: str | None = None*, *last_name: str | None = None*, *is_forum: bool | None = None*, *is_direct_messages: bool | None = None*, *accent_color_id: int | None = None*, *active_usernames: list[str] | None = None*, *available_reactions: list[Annotated[[ReactionTypeEmoji](reaction_type_emoji.html#aiogram.types.reaction_type_emoji.ReactionTypeEmoji "aiogram.types.reaction_type_emoji.ReactionTypeEmoji") | [ReactionTypeCustomEmoji](reaction_type_custom_emoji.html#aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji "aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji") | [ReactionTypePaid](reaction_type_paid.html#aiogram.types.reaction_type_paid.ReactionTypePaid "aiogram.types.reaction_type_paid.ReactionTypePaid"), FieldInfo(annotation=NoneType, required=True, discriminator='type')]] | None = None*, *background_custom_emoji_id: str | None = None*, *bio: str | None = None*, *birthdate: [Birthdate](birthdate.html#aiogram.types.birthdate.Birthdate "aiogram.types.birthdate.Birthdate") | None = None*, *business_intro: [BusinessIntro](business_intro.html#aiogram.types.business_intro.BusinessIntro "aiogram.types.business_intro.BusinessIntro") | None = None*, *business_location: [BusinessLocation](business_location.html#aiogram.types.business_location.BusinessLocation "aiogram.types.business_location.BusinessLocation") | None = None*, *business_opening_hours: [BusinessOpeningHours](business_opening_hours.html#aiogram.types.business_opening_hours.BusinessOpeningHours "aiogram.types.business_opening_hours.BusinessOpeningHours") | None = None*, *can_set_sticker_set: bool | None = None*, *custom_emoji_sticker_set_name: str | None = None*, *description: str | None = None*, *emoji_status_custom_emoji_id: str | None = None*, *emoji_status_expiration_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *has_aggressive_anti_spam_enabled: bool | None = None*, *has_hidden_members: bool | None = None*, *has_private_forwards: bool | None = None*, *has_protected_content: bool | None = None*, *has_restricted_voice_and_video_messages: bool | None = None*, *has_visible_history: bool | None = None*, *invite_link: str | None = None*, *join_by_request: bool | None = None*, *join_to_send_messages: bool | None = None*, *linked_chat_id: int | None = None*, *location: [ChatLocation](chat_location.html#aiogram.types.chat_location.ChatLocation "aiogram.types.chat_location.ChatLocation") | None = None*, *message_auto_delete_time: int | None = None*, *permissions: [ChatPermissions](chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions") | None = None*, *personal_chat: [Chat](#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *photo: [ChatPhoto](chat_photo.html#aiogram.types.chat_photo.ChatPhoto "aiogram.types.chat_photo.ChatPhoto") | None = None*, *pinned_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *profile_accent_color_id: int | None = None*, *profile_background_custom_emoji_id: str | None = None*, *slow_mode_delay: int | None = None*, *sticker_set_name: str | None = None*, *unrestrict_boost_count: int | None = None*, *\*\*extra_data: Any*)
:   This object represents a chat.

    Source: <https://core.telegram.org/bots/api#chat>

    id*: int*
    :   Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier

    type*: str*
    :   Type of the chat, can be either ‘private’, ‘group’, ‘supergroup’ or ‘channel’

    title*: str | None*
    :   *Optional*. Title, for supergroups, channels and group chats

    username*: str | None*
    :   *Optional*. Username, for private chats, supergroups and channels if available

    first_name*: str | None*
    :   *Optional*. First name of the other party in a private chat

    last_name*: str | None*
    :   *Optional*. Last name of the other party in a private chat

    is_forum*: bool | None*
    :   *Optional*. `True`, if the supergroup chat is a forum (has [topics](https://telegram.org/blog/topics-in-groups-collectible-usernames#topics-in-groups) enabled)

    is_direct_messages*: bool | None*
    :   *Optional*. `True`, if the chat is the direct messages chat of a channel

    accent_color_id*: int | None*
    :   *Optional*. Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See [accent colors](https://core.telegram.org/bots/api#accent-colors) for more details. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat"). Always returned in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    active_usernames*: list[str] | None*
    :   *Optional*. If non-empty, the list of all [active chat usernames](https://telegram.org/blog/topics-in-groups-collectible-usernames#collectible-usernames); for private chats, supergroups and channels. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    available_reactions*: list[ReactionTypeUnion] | None*
    :   *Optional*. List of available reactions allowed in the chat. If omitted, then all [emoji reactions](https://core.telegram.org/bots/api#reactiontypeemoji) are allowed. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    background_custom_emoji_id*: str | None*
    :   *Optional*. Custom emoji identifier of emoji chosen by the chat for the reply header and link preview background. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    bio*: str | None*
    :   *Optional*. Bio of the other party in a private chat. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    birthdate*: [Birthdate](birthdate.html#aiogram.types.birthdate.Birthdate "aiogram.types.birthdate.Birthdate") | None*
    :   *Optional*. For private chats, the date of birth of the user. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    business_intro*: [BusinessIntro](business_intro.html#aiogram.types.business_intro.BusinessIntro "aiogram.types.business_intro.BusinessIntro") | None*
    :   *Optional*. For private chats with business accounts, the intro of the business. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    business_location*: [BusinessLocation](business_location.html#aiogram.types.business_location.BusinessLocation "aiogram.types.business_location.BusinessLocation") | None*
    :   *Optional*. For private chats with business accounts, the location of the business. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    business_opening_hours*: [BusinessOpeningHours](business_opening_hours.html#aiogram.types.business_opening_hours.BusinessOpeningHours "aiogram.types.business_opening_hours.BusinessOpeningHours") | None*
    :   *Optional*. For private chats with business accounts, the opening hours of the business. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    can_set_sticker_set*: bool | None*
    :   *Optional*. `True`, if the bot can change the group sticker set. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    custom_emoji_sticker_set_name*: str | None*
    :   *Optional*. For supergroups, the name of the group’s custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    description*: str | None*
    :   *Optional*. Description, for groups, supergroups and channel chats. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    emoji_status_custom_emoji_id*: str | None*
    :   *Optional*. Custom emoji identifier of the emoji status of the chat or the other party in a private chat. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    emoji_status_expiration_date*: DateTime | None*
    :   *Optional*. Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    has_aggressive_anti_spam_enabled*: bool | None*
    :   *Optional*. `True`, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    has_hidden_members*: bool | None*
    :   *Optional*. `True`, if non-administrators can only get the list of bots and administrators in the chat. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    has_private_forwards*: bool | None*
    :   *Optional*. `True`, if privacy settings of the other party in the private chat allows to use `tg://user?id=<user_id>` links only in chats with the user. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    has_protected_content*: bool | None*
    :   *Optional*. `True`, if messages from the chat can’t be forwarded to other chats. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    has_restricted_voice_and_video_messages*: bool | None*
    :   *Optional*. `True`, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    has_visible_history*: bool | None*
    :   *Optional*. `True`, if new chat members will have access to old messages; available only to chat administrators. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    invite_link*: str | None*
    :   *Optional*. Primary invite link, for groups, supergroups and channel chats. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    join_by_request*: bool | None*
    :   *Optional*. `True`, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    join_to_send_messages*: bool | None*
    :   *Optional*. `True`, if users need to join the supergroup before they can send messages. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    linked_chat_id*: int | None*
    :   *Optional*. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    location*: [ChatLocation](chat_location.html#aiogram.types.chat_location.ChatLocation "aiogram.types.chat_location.ChatLocation") | None*
    :   *Optional*. For supergroups, the location to which the supergroup is connected. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    message_auto_delete_time*: int | None*
    :   *Optional*. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    permissions*: [ChatPermissions](chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions") | None*
    :   *Optional*. Default chat member permissions, for groups and supergroups. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    personal_chat*: [Chat](#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. For private chats, the personal channel of the user. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    photo*: [ChatPhoto](chat_photo.html#aiogram.types.chat_photo.ChatPhoto "aiogram.types.chat_photo.ChatPhoto") | None*
    :   *Optional*. Chat photo. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    pinned_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. The most recent pinned message (by sending date). Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    profile_accent_color_id*: int | None*
    :   *Optional*. Identifier of the accent color for the chat’s profile background. See [profile accent colors](https://core.telegram.org/bots/api#profile-accent-colors) for more details. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    profile_background_custom_emoji_id*: str | None*
    :   *Optional*. Custom emoji identifier of the emoji chosen by the chat for its profile background. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    slow_mode_delay*: int | None*
    :   *Optional*. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    sticker_set_name*: str | None*
    :   *Optional*. For supergroups, name of group sticker set. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    unrestrict_boost_count*: int | None*
    :   *Optional*. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions. Returned only in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat")

        Deprecated since version API:7.3: <https://core.telegram.org/bots/api-changelog#may-6-2024>

    *property* shifted_id*: int*
    :   Returns shifted chat ID (positive and without “-100” prefix).
        Mostly used for private links like t.me/c/chat_id/message_id

        Currently supergroup/channel IDs have 10-digit ID after “-100” prefix removed.
        However, these IDs might become 11-digit in future. So, first we remove “-100”
        prefix and count remaining number length. Then we multiple
        -1 \* 10 ^ (number_length + 2)
        Finally, self.id is substracted from that number

    *property* full_name*: str*
    :   Get full name of the Chat.

        For private chat it is first_name + last_name.
        For other chat types it is title.

    ban_sender_chat(*sender_chat_id: int*, *\*\*kwargs: Any*) → [BanChatSenderChat](../methods/ban_chat_sender_chat.html#aiogram.methods.ban_chat_sender_chat.BanChatSenderChat "aiogram.methods.ban_chat_sender_chat.BanChatSenderChat")
    :   Shortcut for method [`aiogram.methods.ban_chat_sender_chat.BanChatSenderChat`](../methods/ban_chat_sender_chat.html#aiogram.methods.ban_chat_sender_chat.BanChatSenderChat "aiogram.methods.ban_chat_sender_chat.BanChatSenderChat")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to ban a channel chat in a supergroup or a channel. Until the chat is [unbanned](https://core.telegram.org/bots/api#unbanchatsenderchat), the owner of the banned chat won’t be able to send messages on behalf of **any of their channels**. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#banchatsenderchat>

        Parameters:
        :   **sender_chat_id** – Unique identifier of the target sender chat

        Returns:
        :   instance of method [`aiogram.methods.ban_chat_sender_chat.BanChatSenderChat`](../methods/ban_chat_sender_chat.html#aiogram.methods.ban_chat_sender_chat.BanChatSenderChat "aiogram.methods.ban_chat_sender_chat.BanChatSenderChat")

    unban_sender_chat(*sender_chat_id: int*, *\*\*kwargs: Any*) → [UnbanChatSenderChat](../methods/unban_chat_sender_chat.html#aiogram.methods.unban_chat_sender_chat.UnbanChatSenderChat "aiogram.methods.unban_chat_sender_chat.UnbanChatSenderChat")
    :   Shortcut for method [`aiogram.methods.unban_chat_sender_chat.UnbanChatSenderChat`](../methods/unban_chat_sender_chat.html#aiogram.methods.unban_chat_sender_chat.UnbanChatSenderChat "aiogram.methods.unban_chat_sender_chat.UnbanChatSenderChat")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#unbanchatsenderchat>

        Parameters:
        :   **sender_chat_id** – Unique identifier of the target sender chat

        Returns:
        :   instance of method [`aiogram.methods.unban_chat_sender_chat.UnbanChatSenderChat`](../methods/unban_chat_sender_chat.html#aiogram.methods.unban_chat_sender_chat.UnbanChatSenderChat "aiogram.methods.unban_chat_sender_chat.UnbanChatSenderChat")

    get_administrators(*return_bots: bool | None = None*, *\*\*kwargs: Any*) → [GetChatAdministrators](../methods/get_chat_administrators.html#aiogram.methods.get_chat_administrators.GetChatAdministrators "aiogram.methods.get_chat_administrators.GetChatAdministrators")
    :   Shortcut for method [`aiogram.methods.get_chat_administrators.GetChatAdministrators`](../methods/get_chat_administrators.html#aiogram.methods.get_chat_administrators.GetChatAdministrators "aiogram.methods.get_chat_administrators.GetChatAdministrators")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to get a list of administrators in a chat. Returns an Array of [`aiogram.types.chat_member.ChatMember`](chat_member.html#aiogram.types.chat_member.ChatMember "aiogram.types.chat_member.ChatMember") objects.

        Source: <https://core.telegram.org/bots/api#getchatadministrators>

        Parameters:
        :   **return_bots** – Pass `True` to additionally receive all bots that are administrators of the chat. By default, bots other than the current bot are omitted

        Returns:
        :   instance of method [`aiogram.methods.get_chat_administrators.GetChatAdministrators`](../methods/get_chat_administrators.html#aiogram.methods.get_chat_administrators.GetChatAdministrators "aiogram.methods.get_chat_administrators.GetChatAdministrators")

    delete_message(*message_id: int*, *\*\*kwargs: Any*) → [DeleteMessage](../methods/delete_message.html#aiogram.methods.delete_message.DeleteMessage "aiogram.methods.delete_message.DeleteMessage")
    :   Shortcut for method [`aiogram.methods.delete_message.DeleteMessage`](../methods/delete_message.html#aiogram.methods.delete_message.DeleteMessage "aiogram.methods.delete_message.DeleteMessage")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to delete a message, including service messages, with the following limitations:

        - A message can only be deleted if it was sent less than 48 hours ago.
        - Service messages about a supergroup, channel, or forum topic creation can’t be deleted.
        - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
        - Bots can delete outgoing messages in private chats, groups, and supergroups.
        - Bots can delete incoming messages in private chats.
        - Bots granted *can_post_messages* permissions can delete outgoing messages in channels.
        - If the bot is an administrator of a group, it can delete any message there.
        - If the bot has *can_delete_messages* administrator right in a supergroup or a channel, it can delete any message there.
        - If the bot has *can_manage_direct_messages* administrator right in a channel, it can delete any message in the corresponding direct messages chat.

        Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#deletemessage>

        Parameters:
        :   **message_id** – Identifier of the message to delete

        Returns:
        :   instance of method [`aiogram.methods.delete_message.DeleteMessage`](../methods/delete_message.html#aiogram.methods.delete_message.DeleteMessage "aiogram.methods.delete_message.DeleteMessage")

    revoke_invite_link(*invite_link: str*, *\*\*kwargs: Any*) → [RevokeChatInviteLink](../methods/revoke_chat_invite_link.html#aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink "aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink")
    :   Shortcut for method [`aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink`](../methods/revoke_chat_invite_link.html#aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink "aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as [`aiogram.types.chat_invite_link.ChatInviteLink`](chat_invite_link.html#aiogram.types.chat_invite_link.ChatInviteLink "aiogram.types.chat_invite_link.ChatInviteLink") object.

        Source: <https://core.telegram.org/bots/api#revokechatinvitelink>

        Parameters:
        :   **invite_link** – The invite link to revoke

        Returns:
        :   instance of method [`aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink`](../methods/revoke_chat_invite_link.html#aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink "aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink")

    edit_invite_link(*invite_link: str*, *name: str | None = None*, *expire_date: DateTimeUnion | None = None*, *member_limit: int | None = None*, *creates_join_request: bool | None = None*, *\*\*kwargs: Any*) → [EditChatInviteLink](../methods/edit_chat_invite_link.html#aiogram.methods.edit_chat_invite_link.EditChatInviteLink "aiogram.methods.edit_chat_invite_link.EditChatInviteLink")
    :   Shortcut for method [`aiogram.methods.edit_chat_invite_link.EditChatInviteLink`](../methods/edit_chat_invite_link.html#aiogram.methods.edit_chat_invite_link.EditChatInviteLink "aiogram.methods.edit_chat_invite_link.EditChatInviteLink")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a [`aiogram.types.chat_invite_link.ChatInviteLink`](chat_invite_link.html#aiogram.types.chat_invite_link.ChatInviteLink "aiogram.types.chat_invite_link.ChatInviteLink") object.

        Source: <https://core.telegram.org/bots/api#editchatinvitelink>

        Parameters:
        :   - **invite_link** – The invite link to edit
            - **name** – Invite link name; 0-32 characters
            - **expire_date** – Point in time (Unix timestamp) when the link will expire
            - **member_limit** – The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
            - **creates_join_request** – `True`, if users joining the chat via the link need to be approved by chat administrators. If `True`, *member_limit* can’t be specified

        Returns:
        :   instance of method [`aiogram.methods.edit_chat_invite_link.EditChatInviteLink`](../methods/edit_chat_invite_link.html#aiogram.methods.edit_chat_invite_link.EditChatInviteLink "aiogram.methods.edit_chat_invite_link.EditChatInviteLink")

    create_invite_link(*name: str | None = None*, *expire_date: DateTimeUnion | None = None*, *member_limit: int | None = None*, *creates_join_request: bool | None = None*, *\*\*kwargs: Any*) → [CreateChatInviteLink](../methods/create_chat_invite_link.html#aiogram.methods.create_chat_invite_link.CreateChatInviteLink "aiogram.methods.create_chat_invite_link.CreateChatInviteLink")
    :   Shortcut for method [`aiogram.methods.create_chat_invite_link.CreateChatInviteLink`](../methods/create_chat_invite_link.html#aiogram.methods.create_chat_invite_link.CreateChatInviteLink "aiogram.methods.create_chat_invite_link.CreateChatInviteLink")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method [`aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink`](../methods/revoke_chat_invite_link.html#aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink "aiogram.methods.revoke_chat_invite_link.RevokeChatInviteLink"). Returns the new invite link as [`aiogram.types.chat_invite_link.ChatInviteLink`](chat_invite_link.html#aiogram.types.chat_invite_link.ChatInviteLink "aiogram.types.chat_invite_link.ChatInviteLink") object.

        Source: <https://core.telegram.org/bots/api#createchatinvitelink>

        Parameters:
        :   - **name** – Invite link name; 0-32 characters
            - **expire_date** – Point in time (Unix timestamp) when the link will expire
            - **member_limit** – The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
            - **creates_join_request** – `True`, if users joining the chat via the link need to be approved by chat administrators. If `True`, *member_limit* can’t be specified

        Returns:
        :   instance of method [`aiogram.methods.create_chat_invite_link.CreateChatInviteLink`](../methods/create_chat_invite_link.html#aiogram.methods.create_chat_invite_link.CreateChatInviteLink "aiogram.methods.create_chat_invite_link.CreateChatInviteLink")

    export_invite_link(*\*\*kwargs: Any*) → [ExportChatInviteLink](../methods/export_chat_invite_link.html#aiogram.methods.export_chat_invite_link.ExportChatInviteLink "aiogram.methods.export_chat_invite_link.ExportChatInviteLink")
    :   Shortcut for method [`aiogram.methods.export_chat_invite_link.ExportChatInviteLink`](../methods/export_chat_invite_link.html#aiogram.methods.export_chat_invite_link.ExportChatInviteLink "aiogram.methods.export_chat_invite_link.ExportChatInviteLink")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as *String* on success.

        > Note: Each administrator in a chat generates their own invite links. Bots can’t use invite links generated by other administrators. If you want your bot to work with invite links, it will need to generate its own link using [`aiogram.methods.export_chat_invite_link.ExportChatInviteLink`](../methods/export_chat_invite_link.html#aiogram.methods.export_chat_invite_link.ExportChatInviteLink "aiogram.methods.export_chat_invite_link.ExportChatInviteLink") or by calling the [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat") method. If your bot needs to generate a new primary invite link replacing its previous one, use [`aiogram.methods.export_chat_invite_link.ExportChatInviteLink`](../methods/export_chat_invite_link.html#aiogram.methods.export_chat_invite_link.ExportChatInviteLink "aiogram.methods.export_chat_invite_link.ExportChatInviteLink") again.

        Source: <https://core.telegram.org/bots/api#exportchatinvitelink>

        Returns:
        :   instance of method [`aiogram.methods.export_chat_invite_link.ExportChatInviteLink`](../methods/export_chat_invite_link.html#aiogram.methods.export_chat_invite_link.ExportChatInviteLink "aiogram.methods.export_chat_invite_link.ExportChatInviteLink")

    do(*action: str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *\*\*kwargs: Any*) → [SendChatAction](../methods/send_chat_action.html#aiogram.methods.send_chat_action.SendChatAction "aiogram.methods.send_chat_action.SendChatAction")
    :   Shortcut for method [`aiogram.methods.send_chat_action.SendChatAction`](../methods/send_chat_action.html#aiogram.methods.send_chat_action.SendChatAction "aiogram.methods.send_chat_action.SendChatAction")
        will automatically fill method attributes:

        - `chat_id`

        Use this method when you need to tell the user that something is happening on the bot’s side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns `True` on success.

        > Example: The [ImageBot](https://t.me/imagebot) needs some time to process a request and upload the image. Instead of sending a text message along the lines of ‘Retrieving image, please wait…’, the bot may use [`aiogram.methods.send_chat_action.SendChatAction`](../methods/send_chat_action.html#aiogram.methods.send_chat_action.SendChatAction "aiogram.methods.send_chat_action.SendChatAction") with *action* = *upload_photo*. The user will see a ‘sending photo’ status for the bot.

        We only recommend using this method when a response from the bot will take a **noticeable** amount of time to arrive.

        Source: <https://core.telegram.org/bots/api#sendchataction>

        Parameters:
        :   - **action** – Type of action to broadcast. Choose one, depending on what the user is about to receive: *typing* for [text messages](https://core.telegram.org/bots/api#sendmessage), *upload_photo* for [photos](https://core.telegram.org/bots/api#sendphoto), *record_video* or *upload_video* for [videos](https://core.telegram.org/bots/api#sendvideo), *record_voice* or *upload_voice* for [voice notes](https://core.telegram.org/bots/api#sendvoice), *upload_document* for [general files](https://core.telegram.org/bots/api#senddocument), *choose_sticker* for [stickers](https://core.telegram.org/bots/api#sendsticker), *find_location* for [location data](https://core.telegram.org/bots/api#sendlocation), *record_video_note* or *upload_video_note* for [video notes](https://core.telegram.org/bots/api#sendvideonote)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the action will be sent
            - **message_thread_id** – Unique identifier for the target message thread or topic of a forum; for supergroups and private chats of bots with forum topic mode enabled only

        Returns:
        :   instance of method [`aiogram.methods.send_chat_action.SendChatAction`](../methods/send_chat_action.html#aiogram.methods.send_chat_action.SendChatAction "aiogram.methods.send_chat_action.SendChatAction")

    delete_sticker_set(*\*\*kwargs: Any*) → [DeleteChatStickerSet](../methods/delete_chat_sticker_set.html#aiogram.methods.delete_chat_sticker_set.DeleteChatStickerSet "aiogram.methods.delete_chat_sticker_set.DeleteChatStickerSet")
    :   Shortcut for method [`aiogram.methods.delete_chat_sticker_set.DeleteChatStickerSet`](../methods/delete_chat_sticker_set.html#aiogram.methods.delete_chat_sticker_set.DeleteChatStickerSet "aiogram.methods.delete_chat_sticker_set.DeleteChatStickerSet")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field *can_set_sticker_set* optionally returned in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat") requests to check if the bot can use this method. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#deletechatstickerset>

        Returns:
        :   instance of method [`aiogram.methods.delete_chat_sticker_set.DeleteChatStickerSet`](../methods/delete_chat_sticker_set.html#aiogram.methods.delete_chat_sticker_set.DeleteChatStickerSet "aiogram.methods.delete_chat_sticker_set.DeleteChatStickerSet")

    set_sticker_set(*sticker_set_name: str*, *\*\*kwargs: Any*) → [SetChatStickerSet](../methods/set_chat_sticker_set.html#aiogram.methods.set_chat_sticker_set.SetChatStickerSet "aiogram.methods.set_chat_sticker_set.SetChatStickerSet")
    :   Shortcut for method [`aiogram.methods.set_chat_sticker_set.SetChatStickerSet`](../methods/set_chat_sticker_set.html#aiogram.methods.set_chat_sticker_set.SetChatStickerSet "aiogram.methods.set_chat_sticker_set.SetChatStickerSet")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field *can_set_sticker_set* optionally returned in [`aiogram.methods.get_chat.GetChat`](../methods/get_chat.html#aiogram.methods.get_chat.GetChat "aiogram.methods.get_chat.GetChat") requests to check if the bot can use this method. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#setchatstickerset>

        Parameters:
        :   **sticker_set_name** – Name of the sticker set to be set as the group sticker set

        Returns:
        :   instance of method [`aiogram.methods.set_chat_sticker_set.SetChatStickerSet`](../methods/set_chat_sticker_set.html#aiogram.methods.set_chat_sticker_set.SetChatStickerSet "aiogram.methods.set_chat_sticker_set.SetChatStickerSet")

    get_member(*user_id: int*, *\*\*kwargs: Any*) → [GetChatMember](../methods/get_chat_member.html#aiogram.methods.get_chat_member.GetChatMember "aiogram.methods.get_chat_member.GetChatMember")
    :   Shortcut for method [`aiogram.methods.get_chat_member.GetChatMember`](../methods/get_chat_member.html#aiogram.methods.get_chat_member.GetChatMember "aiogram.methods.get_chat_member.GetChatMember")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a [`aiogram.types.chat_member.ChatMember`](chat_member.html#aiogram.types.chat_member.ChatMember "aiogram.types.chat_member.ChatMember") object on success.

        Source: <https://core.telegram.org/bots/api#getchatmember>

        Parameters:
        :   **user_id** – Unique identifier of the target user

        Returns:
        :   instance of method [`aiogram.methods.get_chat_member.GetChatMember`](../methods/get_chat_member.html#aiogram.methods.get_chat_member.GetChatMember "aiogram.methods.get_chat_member.GetChatMember")

    get_member_count(*\*\*kwargs: Any*) → [GetChatMemberCount](../methods/get_chat_member_count.html#aiogram.methods.get_chat_member_count.GetChatMemberCount "aiogram.methods.get_chat_member_count.GetChatMemberCount")
    :   Shortcut for method [`aiogram.methods.get_chat_member_count.GetChatMemberCount`](../methods/get_chat_member_count.html#aiogram.methods.get_chat_member_count.GetChatMemberCount "aiogram.methods.get_chat_member_count.GetChatMemberCount")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to get the number of members in a chat. Returns *Integer* on success.

        Source: <https://core.telegram.org/bots/api#getchatmembercount>

        Returns:
        :   instance of method [`aiogram.methods.get_chat_member_count.GetChatMemberCount`](../methods/get_chat_member_count.html#aiogram.methods.get_chat_member_count.GetChatMemberCount "aiogram.methods.get_chat_member_count.GetChatMemberCount")

    leave(*\*\*kwargs: Any*) → [LeaveChat](../methods/leave_chat.html#aiogram.methods.leave_chat.LeaveChat "aiogram.methods.leave_chat.LeaveChat")
    :   Shortcut for method [`aiogram.methods.leave_chat.LeaveChat`](../methods/leave_chat.html#aiogram.methods.leave_chat.LeaveChat "aiogram.methods.leave_chat.LeaveChat")
        will automatically fill method attributes:

        - `chat_id`

        Use this method for your bot to leave a group, supergroup or channel. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#leavechat>

        Returns:
        :   instance of method [`aiogram.methods.leave_chat.LeaveChat`](../methods/leave_chat.html#aiogram.methods.leave_chat.LeaveChat "aiogram.methods.leave_chat.LeaveChat")

    unpin_all_messages(*\*\*kwargs: Any*) → [UnpinAllChatMessages](../methods/unpin_all_chat_messages.html#aiogram.methods.unpin_all_chat_messages.UnpinAllChatMessages "aiogram.methods.unpin_all_chat_messages.UnpinAllChatMessages")
    :   Shortcut for method [`aiogram.methods.unpin_all_chat_messages.UnpinAllChatMessages`](../methods/unpin_all_chat_messages.html#aiogram.methods.unpin_all_chat_messages.UnpinAllChatMessages "aiogram.methods.unpin_all_chat_messages.UnpinAllChatMessages")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to clear the list of pinned messages in a chat. In private chats and channel direct messages chats, no additional rights are required to unpin all pinned messages. Conversely, the bot must be an administrator with the ‘can_pin_messages’ right or the ‘can_edit_messages’ right to unpin all pinned messages in groups and channels respectively. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#unpinallchatmessages>

        Returns:
        :   instance of method [`aiogram.methods.unpin_all_chat_messages.UnpinAllChatMessages`](../methods/unpin_all_chat_messages.html#aiogram.methods.unpin_all_chat_messages.UnpinAllChatMessages "aiogram.methods.unpin_all_chat_messages.UnpinAllChatMessages")

    unpin_message(*business_connection_id: str | None = None*, *message_id: int | None = None*, *\*\*kwargs: Any*) → [UnpinChatMessage](../methods/unpin_chat_message.html#aiogram.methods.unpin_chat_message.UnpinChatMessage "aiogram.methods.unpin_chat_message.UnpinChatMessage")
    :   Shortcut for method [`aiogram.methods.unpin_chat_message.UnpinChatMessage`](../methods/unpin_chat_message.html#aiogram.methods.unpin_chat_message.UnpinChatMessage "aiogram.methods.unpin_chat_message.UnpinChatMessage")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to remove a message from the list of pinned messages in a chat. In private chats and channel direct messages chats, all messages can be unpinned. Conversely, the bot must be an administrator with the ‘can_pin_messages’ right or the ‘can_edit_messages’ right to unpin messages in groups and channels respectively. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#unpinchatmessage>

        Parameters:
        :   - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be unpinned
            - **message_id** – Identifier of the message to unpin. Required if *business_connection_id* is specified. If not specified, the most recent pinned message (by sending date) will be unpinned

        Returns:
        :   instance of method [`aiogram.methods.unpin_chat_message.UnpinChatMessage`](../methods/unpin_chat_message.html#aiogram.methods.unpin_chat_message.UnpinChatMessage "aiogram.methods.unpin_chat_message.UnpinChatMessage")

    pin_message(*message_id: int*, *business_connection_id: str | None = None*, *disable_notification: bool | None = None*, *\*\*kwargs: Any*) → [PinChatMessage](../methods/pin_chat_message.html#aiogram.methods.pin_chat_message.PinChatMessage "aiogram.methods.pin_chat_message.PinChatMessage")
    :   Shortcut for method [`aiogram.methods.pin_chat_message.PinChatMessage`](../methods/pin_chat_message.html#aiogram.methods.pin_chat_message.PinChatMessage "aiogram.methods.pin_chat_message.PinChatMessage")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to add a message to the list of pinned messages in a chat. In private chats and channel direct messages chats, all non-service messages can be pinned. Conversely, the bot must be an administrator with the ‘can_pin_messages’ right or the ‘can_edit_messages’ right to pin messages in groups and channels respectively. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#pinchatmessage>

        Parameters:
        :   - **message_id** – Identifier of a message to pin
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be pinned
            - **disable_notification** – Pass `True` if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats

        Returns:
        :   instance of method [`aiogram.methods.pin_chat_message.PinChatMessage`](../methods/pin_chat_message.html#aiogram.methods.pin_chat_message.PinChatMessage "aiogram.methods.pin_chat_message.PinChatMessage")

    set_administrator_custom_title(*user_id: int*, *custom_title: str*, *\*\*kwargs: Any*) → [SetChatAdministratorCustomTitle](../methods/set_chat_administrator_custom_title.html#aiogram.methods.set_chat_administrator_custom_title.SetChatAdministratorCustomTitle "aiogram.methods.set_chat_administrator_custom_title.SetChatAdministratorCustomTitle")
    :   Shortcut for method [`aiogram.methods.set_chat_administrator_custom_title.SetChatAdministratorCustomTitle`](../methods/set_chat_administrator_custom_title.html#aiogram.methods.set_chat_administrator_custom_title.SetChatAdministratorCustomTitle "aiogram.methods.set_chat_administrator_custom_title.SetChatAdministratorCustomTitle")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#setchatadministratorcustomtitle>

        Parameters:
        :   - **user_id** – Unique identifier of the target user
            - **custom_title** – New custom title for the administrator; 0-16 characters, emoji are not allowed

        Returns:
        :   instance of method [`aiogram.methods.set_chat_administrator_custom_title.SetChatAdministratorCustomTitle`](../methods/set_chat_administrator_custom_title.html#aiogram.methods.set_chat_administrator_custom_title.SetChatAdministratorCustomTitle "aiogram.methods.set_chat_administrator_custom_title.SetChatAdministratorCustomTitle")

    set_member_tag(*user_id: int*, *tag: str | None = None*, *\*\*kwargs: Any*) → [SetChatMemberTag](../methods/set_chat_member_tag.html#aiogram.methods.set_chat_member_tag.SetChatMemberTag "aiogram.methods.set_chat_member_tag.SetChatMemberTag")
    :   Shortcut for method [`aiogram.methods.set_chat_member_tag.SetChatMemberTag`](../methods/set_chat_member_tag.html#aiogram.methods.set_chat_member_tag.SetChatMemberTag "aiogram.methods.set_chat_member_tag.SetChatMemberTag")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to set a tag for a regular member in a group or a supergroup. The bot must be an administrator in the chat for this to work and must have the *can_manage_tags* administrator right. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#setchatmembertag>

        Parameters:
        :   - **user_id** – Unique identifier of the target user
            - **tag** – New tag for the member; 0-16 characters, emoji are not allowed

        Returns:
        :   instance of method [`aiogram.methods.set_chat_member_tag.SetChatMemberTag`](../methods/set_chat_member_tag.html#aiogram.methods.set_chat_member_tag.SetChatMemberTag "aiogram.methods.set_chat_member_tag.SetChatMemberTag")

    set_permissions(*permissions: [ChatPermissions](chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions")*, *use_independent_chat_permissions: bool | None = None*, *\*\*kwargs: Any*) → [SetChatPermissions](../methods/set_chat_permissions.html#aiogram.methods.set_chat_permissions.SetChatPermissions "aiogram.methods.set_chat_permissions.SetChatPermissions")
    :   Shortcut for method [`aiogram.methods.set_chat_permissions.SetChatPermissions`](../methods/set_chat_permissions.html#aiogram.methods.set_chat_permissions.SetChatPermissions "aiogram.methods.set_chat_permissions.SetChatPermissions")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the *can_restrict_members* administrator rights. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#setchatpermissions>

        Parameters:
        :   - **permissions** – A JSON-serialized object for new default chat permissions
            - **use_independent_chat_permissions** – Pass `True` if chat permissions are set independently. Otherwise, the *can_send_other_messages* and *can_add_web_page_previews* permissions will imply the *can_send_messages*, *can_send_audios*, *can_send_documents*, *can_send_photos*, *can_send_videos*, *can_send_video_notes*, and *can_send_voice_notes* permissions; the *can_send_polls* permission will imply the *can_send_messages* permission

        Returns:
        :   instance of method [`aiogram.methods.set_chat_permissions.SetChatPermissions`](../methods/set_chat_permissions.html#aiogram.methods.set_chat_permissions.SetChatPermissions "aiogram.methods.set_chat_permissions.SetChatPermissions")

    promote(*user_id: int*, *is_anonymous: bool | None = None*, *can_manage_chat: bool | None = None*, *can_delete_messages: bool | None = None*, *can_manage_video_chats: bool | None = None*, *can_restrict_members: bool | None = None*, *can_promote_members: bool | None = None*, *can_change_info: bool | None = None*, *can_invite_users: bool | None = None*, *can_post_stories: bool | None = None*, *can_edit_stories: bool | None = None*, *can_delete_stories: bool | None = None*, *can_post_messages: bool | None = None*, *can_edit_messages: bool | None = None*, *can_pin_messages: bool | None = None*, *can_manage_topics: bool | None = None*, *can_manage_direct_messages: bool | None = None*, *can_manage_tags: bool | None = None*, *\*\*kwargs: Any*) → [PromoteChatMember](../methods/promote_chat_member.html#aiogram.methods.promote_chat_member.PromoteChatMember "aiogram.methods.promote_chat_member.PromoteChatMember")
    :   Shortcut for method [`aiogram.methods.promote_chat_member.PromoteChatMember`](../methods/promote_chat_member.html#aiogram.methods.promote_chat_member.PromoteChatMember "aiogram.methods.promote_chat_member.PromoteChatMember")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass `False` for all boolean parameters to demote a user. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#promotechatmember>

        Parameters:
        :   - **user_id** – Unique identifier of the target user
            - **is_anonymous** – Pass `True` if the administrator’s presence in the chat is hidden
            - **can_manage_chat** – Pass `True` if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages, ignore slow mode, and send messages to the chat without paying Telegram Stars. Implied by any other administrator privilege
            - **can_delete_messages** – Pass `True` if the administrator can delete messages of other users
            - **can_manage_video_chats** – Pass `True` if the administrator can manage video chats
            - **can_restrict_members** – Pass `True` if the administrator can restrict, ban or unban chat members, or access supergroup statistics. For backward compatibility, defaults to `True` for promotions of channel administrators
            - **can_promote_members** – Pass `True` if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by him)
            - **can_change_info** – Pass `True` if the administrator can change chat title, photo and other settings
            - **can_invite_users** – Pass `True` if the administrator can invite new users to the chat
            - **can_post_stories** – Pass `True` if the administrator can post stories to the chat
            - **can_edit_stories** – Pass `True` if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat’s story archive
            - **can_delete_stories** – Pass `True` if the administrator can delete stories posted by other users
            - **can_post_messages** – Pass `True` if the administrator can post messages in the channel, approve suggested posts, or access channel statistics; for channels only
            - **can_edit_messages** – Pass `True` if the administrator can edit messages of other users and can pin messages; for channels only
            - **can_pin_messages** – Pass `True` if the administrator can pin messages; for supergroups only
            - **can_manage_topics** – Pass `True` if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only
            - **can_manage_direct_messages** – Pass `True` if the administrator can manage direct messages within the channel and decline suggested posts; for channels only
            - **can_manage_tags** – Pass `True` if the administrator can edit the tags of regular members; for groups and supergroups only

        Returns:
        :   instance of method [`aiogram.methods.promote_chat_member.PromoteChatMember`](../methods/promote_chat_member.html#aiogram.methods.promote_chat_member.PromoteChatMember "aiogram.methods.promote_chat_member.PromoteChatMember")

    restrict(*user_id: int*, *permissions: [ChatPermissions](chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions")*, *use_independent_chat_permissions: bool | None = None*, *until_date: DateTimeUnion | None = None*, *\*\*kwargs: Any*) → [RestrictChatMember](../methods/restrict_chat_member.html#aiogram.methods.restrict_chat_member.RestrictChatMember "aiogram.methods.restrict_chat_member.RestrictChatMember")
    :   Shortcut for method [`aiogram.methods.restrict_chat_member.RestrictChatMember`](../methods/restrict_chat_member.html#aiogram.methods.restrict_chat_member.RestrictChatMember "aiogram.methods.restrict_chat_member.RestrictChatMember")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass `True` for all permissions to lift restrictions from a user. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#restrictchatmember>

        Parameters:
        :   - **user_id** – Unique identifier of the target user
            - **permissions** – A JSON-serialized object for new user permissions
            - **use_independent_chat_permissions** – Pass `True` if chat permissions are set independently. Otherwise, the *can_send_other_messages* and *can_add_web_page_previews* permissions will imply the *can_send_messages*, *can_send_audios*, *can_send_documents*, *can_send_photos*, *can_send_videos*, *can_send_video_notes*, and *can_send_voice_notes* permissions; the *can_send_polls* permission will imply the *can_send_messages* permission
            - **until_date** – Date when restrictions will be lifted for the user; Unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever

        Returns:
        :   instance of method [`aiogram.methods.restrict_chat_member.RestrictChatMember`](../methods/restrict_chat_member.html#aiogram.methods.restrict_chat_member.RestrictChatMember "aiogram.methods.restrict_chat_member.RestrictChatMember")

    unban(*user_id: int*, *only_if_banned: bool | None = None*, *\*\*kwargs: Any*) → [UnbanChatMember](../methods/unban_chat_member.html#aiogram.methods.unban_chat_member.UnbanChatMember "aiogram.methods.unban_chat_member.UnbanChatMember")
    :   Shortcut for method [`aiogram.methods.unban_chat_member.UnbanChatMember`](../methods/unban_chat_member.html#aiogram.methods.unban_chat_member.UnbanChatMember "aiogram.methods.unban_chat_member.UnbanChatMember")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to unban a previously banned user in a supergroup or channel. The user will **not** return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be **removed** from the chat. If you don’t want this, use the parameter *only_if_banned*. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#unbanchatmember>

        Parameters:
        :   - **user_id** – Unique identifier of the target user
            - **only_if_banned** – Do nothing if the user is not banned

        Returns:
        :   instance of method [`aiogram.methods.unban_chat_member.UnbanChatMember`](../methods/unban_chat_member.html#aiogram.methods.unban_chat_member.UnbanChatMember "aiogram.methods.unban_chat_member.UnbanChatMember")

    ban(*user_id: int*, *until_date: DateTimeUnion | None = None*, *revoke_messages: bool | None = None*, *\*\*kwargs: Any*) → [BanChatMember](../methods/ban_chat_member.html#aiogram.methods.ban_chat_member.BanChatMember "aiogram.methods.ban_chat_member.BanChatMember")
    :   Shortcut for method [`aiogram.methods.ban_chat_member.BanChatMember`](../methods/ban_chat_member.html#aiogram.methods.ban_chat_member.BanChatMember "aiogram.methods.ban_chat_member.BanChatMember")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless [unbanned](https://core.telegram.org/bots/api#unbanchatmember) first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#banchatmember>

        Parameters:
        :   - **user_id** – Unique identifier of the target user
            - **until_date** – Date when the user will be unbanned; Unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only
            - **revoke_messages** – Pass `True` to delete all messages from the chat for the user that is being removed. If `False`, the user will be able to see messages in the group that were sent before the user was removed. Always `True` for supergroups and channels

        Returns:
        :   instance of method [`aiogram.methods.ban_chat_member.BanChatMember`](../methods/ban_chat_member.html#aiogram.methods.ban_chat_member.BanChatMember "aiogram.methods.ban_chat_member.BanChatMember")

    set_description(*description: str | None = None*, *\*\*kwargs: Any*) → [SetChatDescription](../methods/set_chat_description.html#aiogram.methods.set_chat_description.SetChatDescription "aiogram.methods.set_chat_description.SetChatDescription")
    :   Shortcut for method [`aiogram.methods.set_chat_description.SetChatDescription`](../methods/set_chat_description.html#aiogram.methods.set_chat_description.SetChatDescription "aiogram.methods.set_chat_description.SetChatDescription")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#setchatdescription>

        Parameters:
        :   **description** – New chat description, 0-255 characters

        Returns:
        :   instance of method [`aiogram.methods.set_chat_description.SetChatDescription`](../methods/set_chat_description.html#aiogram.methods.set_chat_description.SetChatDescription "aiogram.methods.set_chat_description.SetChatDescription")

    set_title(*title: str*, *\*\*kwargs: Any*) → [SetChatTitle](../methods/set_chat_title.html#aiogram.methods.set_chat_title.SetChatTitle "aiogram.methods.set_chat_title.SetChatTitle")
    :   Shortcut for method [`aiogram.methods.set_chat_title.SetChatTitle`](../methods/set_chat_title.html#aiogram.methods.set_chat_title.SetChatTitle "aiogram.methods.set_chat_title.SetChatTitle")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to change the title of a chat. Titles can’t be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#setchattitle>

        Parameters:
        :   **title** – New chat title, 1-128 characters

        Returns:
        :   instance of method [`aiogram.methods.set_chat_title.SetChatTitle`](../methods/set_chat_title.html#aiogram.methods.set_chat_title.SetChatTitle "aiogram.methods.set_chat_title.SetChatTitle")

    delete_photo(*\*\*kwargs: Any*) → [DeleteChatPhoto](../methods/delete_chat_photo.html#aiogram.methods.delete_chat_photo.DeleteChatPhoto "aiogram.methods.delete_chat_photo.DeleteChatPhoto")
    :   Shortcut for method [`aiogram.methods.delete_chat_photo.DeleteChatPhoto`](../methods/delete_chat_photo.html#aiogram.methods.delete_chat_photo.DeleteChatPhoto "aiogram.methods.delete_chat_photo.DeleteChatPhoto")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to delete a chat photo. Photos can’t be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#deletechatphoto>

        Returns:
        :   instance of method [`aiogram.methods.delete_chat_photo.DeleteChatPhoto`](../methods/delete_chat_photo.html#aiogram.methods.delete_chat_photo.DeleteChatPhoto "aiogram.methods.delete_chat_photo.DeleteChatPhoto")

    set_photo(*photo: [InputFile](input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile")*, *\*\*kwargs: Any*) → [SetChatPhoto](../methods/set_chat_photo.html#aiogram.methods.set_chat_photo.SetChatPhoto "aiogram.methods.set_chat_photo.SetChatPhoto")
    :   Shortcut for method [`aiogram.methods.set_chat_photo.SetChatPhoto`](../methods/set_chat_photo.html#aiogram.methods.set_chat_photo.SetChatPhoto "aiogram.methods.set_chat_photo.SetChatPhoto")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to set a new profile photo for the chat. Photos can’t be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#setchatphoto>

        Parameters:
        :   **photo** – New chat photo, uploaded using multipart/form-data

        Returns:
        :   instance of method [`aiogram.methods.set_chat_photo.SetChatPhoto`](../methods/set_chat_photo.html#aiogram.methods.set_chat_photo.SetChatPhoto "aiogram.methods.set_chat_photo.SetChatPhoto")

    unpin_all_general_forum_topic_messages(*\*\*kwargs: Any*) → [UnpinAllGeneralForumTopicMessages](../methods/unpin_all_general_forum_topic_messages.html#aiogram.methods.unpin_all_general_forum_topic_messages.UnpinAllGeneralForumTopicMessages "aiogram.methods.unpin_all_general_forum_topic_messages.UnpinAllGeneralForumTopicMessages")
    :   Shortcut for method [`aiogram.methods.unpin_all_general_forum_topic_messages.UnpinAllGeneralForumTopicMessages`](../methods/unpin_all_general_forum_topic_messages.html#aiogram.methods.unpin_all_general_forum_topic_messages.UnpinAllGeneralForumTopicMessages "aiogram.methods.unpin_all_general_forum_topic_messages.UnpinAllGeneralForumTopicMessages")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to clear the list of pinned messages in a General forum topic. The bot must be an administrator in the chat for this to work and must have the *can_pin_messages* administrator right in the supergroup. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#unpinallgeneralforumtopicmessages>

        Returns:
        :   instance of method [`aiogram.methods.unpin_all_general_forum_topic_messages.UnpinAllGeneralForumTopicMessages`](../methods/unpin_all_general_forum_topic_messages.html#aiogram.methods.unpin_all_general_forum_topic_messages.UnpinAllGeneralForumTopicMessages "aiogram.methods.unpin_all_general_forum_topic_messages.UnpinAllGeneralForumTopicMessages")
