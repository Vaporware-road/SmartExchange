# ChatFullInfo

> Source: [https://docs.aiogram.dev/en/latest/api/types/chat_full_info.html](https://docs.aiogram.dev/en/latest/api/types/chat_full_info.html)

*class* aiogram.types.chat_full_info.ChatFullInfo(*\**, *id: int*, *type: str*, *title: str | None = None*, *username: str | None = None*, *first_name: str | None = None*, *last_name: str | None = None*, *is_forum: bool | None = None*, *is_direct_messages: bool | None = None*, *accent_color_id: int*, *active_usernames: list[str] | None = None*, *available_reactions: list[Annotated[[ReactionTypeEmoji](reaction_type_emoji.html#aiogram.types.reaction_type_emoji.ReactionTypeEmoji "aiogram.types.reaction_type_emoji.ReactionTypeEmoji") | [ReactionTypeCustomEmoji](reaction_type_custom_emoji.html#aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji "aiogram.types.reaction_type_custom_emoji.ReactionTypeCustomEmoji") | [ReactionTypePaid](reaction_type_paid.html#aiogram.types.reaction_type_paid.ReactionTypePaid "aiogram.types.reaction_type_paid.ReactionTypePaid"), FieldInfo(annotation=NoneType, required=True, discriminator='type')]] | None = None*, *background_custom_emoji_id: str | None = None*, *bio: str | None = None*, *birthdate: [Birthdate](birthdate.html#aiogram.types.birthdate.Birthdate "aiogram.types.birthdate.Birthdate") | None = None*, *business_intro: [BusinessIntro](business_intro.html#aiogram.types.business_intro.BusinessIntro "aiogram.types.business_intro.BusinessIntro") | None = None*, *business_location: [BusinessLocation](business_location.html#aiogram.types.business_location.BusinessLocation "aiogram.types.business_location.BusinessLocation") | None = None*, *business_opening_hours: [BusinessOpeningHours](business_opening_hours.html#aiogram.types.business_opening_hours.BusinessOpeningHours "aiogram.types.business_opening_hours.BusinessOpeningHours") | None = None*, *can_set_sticker_set: bool | None = None*, *custom_emoji_sticker_set_name: str | None = None*, *description: str | None = None*, *emoji_status_custom_emoji_id: str | None = None*, *emoji_status_expiration_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *has_aggressive_anti_spam_enabled: bool | None = None*, *has_hidden_members: bool | None = None*, *has_private_forwards: bool | None = None*, *has_protected_content: bool | None = None*, *has_restricted_voice_and_video_messages: bool | None = None*, *has_visible_history: bool | None = None*, *invite_link: str | None = None*, *join_by_request: bool | None = None*, *join_to_send_messages: bool | None = None*, *linked_chat_id: int | None = None*, *location: [ChatLocation](chat_location.html#aiogram.types.chat_location.ChatLocation "aiogram.types.chat_location.ChatLocation") | None = None*, *message_auto_delete_time: int | None = None*, *permissions: [ChatPermissions](chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions") | None = None*, *personal_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *photo: [ChatPhoto](chat_photo.html#aiogram.types.chat_photo.ChatPhoto "aiogram.types.chat_photo.ChatPhoto") | None = None*, *pinned_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *profile_accent_color_id: int | None = None*, *profile_background_custom_emoji_id: str | None = None*, *slow_mode_delay: int | None = None*, *sticker_set_name: str | None = None*, *unrestrict_boost_count: int | None = None*, *max_reaction_count: int*, *accepted_gift_types: [AcceptedGiftTypes](accepted_gift_types.html#aiogram.types.accepted_gift_types.AcceptedGiftTypes "aiogram.types.accepted_gift_types.AcceptedGiftTypes")*, *parent_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *can_send_paid_media: bool | None = None*, *rating: [UserRating](user_rating.html#aiogram.types.user_rating.UserRating "aiogram.types.user_rating.UserRating") | None = None*, *first_profile_audio: [Audio](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio") | None = None*, *unique_gift_colors: [UniqueGiftColors](unique_gift_colors.html#aiogram.types.unique_gift_colors.UniqueGiftColors "aiogram.types.unique_gift_colors.UniqueGiftColors") | None = None*, *paid_message_star_count: int | None = None*, *guard_bot: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *community: [Community](community.html#aiogram.types.community.Community "aiogram.types.community.Community") | None = None*, *can_send_gift: bool | None = None*, *\*\*extra_data: Any*)
:   This object contains full information about a chat.

    Source: <https://core.telegram.org/bots/api#chatfullinfo>

    id*: int*
    :   Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier

    type*: str*
    :   Type of the chat, can be either ‘private’, ‘group’, ‘supergroup’ or ‘channel’

    accent_color_id*: int*
    :   Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See [accent colors](https://core.telegram.org/bots/api#accent-colors) for more details

    max_reaction_count*: int*
    :   The maximum number of reactions that can be set on a message in the chat

    accepted_gift_types*: [AcceptedGiftTypes](accepted_gift_types.html#aiogram.types.accepted_gift_types.AcceptedGiftTypes "aiogram.types.accepted_gift_types.AcceptedGiftTypes")*
    :   Information about types of gifts that are accepted by the chat or by the corresponding user for private chats

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

    photo*: [ChatPhoto](chat_photo.html#aiogram.types.chat_photo.ChatPhoto "aiogram.types.chat_photo.ChatPhoto") | None*
    :   *Optional*. Chat photo

    active_usernames*: list[str] | None*
    :   *Optional*. If non-empty, the list of all [active chat usernames](https://telegram.org/blog/topics-in-groups-collectible-usernames#collectible-usernames); for private chats, supergroups and channels

    birthdate*: [Birthdate](birthdate.html#aiogram.types.birthdate.Birthdate "aiogram.types.birthdate.Birthdate") | None*
    :   *Optional*. For private chats, the date of birth of the user

    business_intro*: [BusinessIntro](business_intro.html#aiogram.types.business_intro.BusinessIntro "aiogram.types.business_intro.BusinessIntro") | None*
    :   *Optional*. For private chats with business accounts, the intro of the business

    business_location*: [BusinessLocation](business_location.html#aiogram.types.business_location.BusinessLocation "aiogram.types.business_location.BusinessLocation") | None*
    :   *Optional*. For private chats with business accounts, the location of the business

    business_opening_hours*: [BusinessOpeningHours](business_opening_hours.html#aiogram.types.business_opening_hours.BusinessOpeningHours "aiogram.types.business_opening_hours.BusinessOpeningHours") | None*
    :   *Optional*. For private chats with business accounts, the opening hours of the business

    personal_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. For private chats, the personal channel of the user

    parent_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. Information about the corresponding channel chat; for direct messages chats only

    available_reactions*: list[ReactionTypeUnion] | None*
    :   *Optional*. List of available reactions allowed in the chat. If omitted, then all [emoji reactions](https://core.telegram.org/bots/api#reactiontypeemoji) are allowed

    background_custom_emoji_id*: str | None*
    :   *Optional*. Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background

    profile_accent_color_id*: int | None*
    :   *Optional*. Identifier of the accent color for the chat’s profile background. See [profile accent colors](https://core.telegram.org/bots/api#profile-accent-colors) for more details

    profile_background_custom_emoji_id*: str | None*
    :   *Optional*. Custom emoji identifier of the emoji chosen by the chat for its profile background

    emoji_status_custom_emoji_id*: str | None*
    :   *Optional*. Custom emoji identifier of the emoji status of the chat or the other party in a private chat

    emoji_status_expiration_date*: DateTime | None*
    :   *Optional*. Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any

    bio*: str | None*
    :   *Optional*. Bio of the other party in a private chat

    has_private_forwards*: bool | None*
    :   *Optional*. `True`, if privacy settings of the other party in the private chat allows to use `tg://user?id=<user_id>` links only in chats with the user

    has_restricted_voice_and_video_messages*: bool | None*
    :   *Optional*. `True`, if the privacy settings of the other party restrict sending voice and video note messages in the private chat

    join_to_send_messages*: bool | None*
    :   *Optional*. `True`, if users need to join the supergroup before they can send messages

    join_by_request*: bool | None*
    :   *Optional*. `True`, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators

    description*: str | None*
    :   *Optional*. Description, for groups, supergroups and channel chats

    invite_link*: str | None*
    :   *Optional*. Primary invite link, for groups, supergroups and channel chats

    pinned_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. The most recent pinned message (by sending date)

    permissions*: [ChatPermissions](chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions") | None*
    :   *Optional*. Default chat member permissions, for groups and supergroups

    can_send_paid_media*: bool | None*
    :   *Optional*. `True`, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats

    slow_mode_delay*: int | None*
    :   *Optional*. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds

    unrestrict_boost_count*: int | None*
    :   *Optional*. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions

    message_auto_delete_time*: int | None*
    :   *Optional*. The time after which all messages sent to the chat will be automatically deleted; in seconds

    has_aggressive_anti_spam_enabled*: bool | None*
    :   *Optional*. `True`, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators

    has_hidden_members*: bool | None*
    :   *Optional*. `True`, if non-administrators can only get the list of bots and administrators in the chat

    has_protected_content*: bool | None*
    :   *Optional*. `True`, if messages from the chat can’t be forwarded to other chats

    has_visible_history*: bool | None*
    :   *Optional*. `True`, if new chat members will have access to old messages; available only to chat administrators

    sticker_set_name*: str | None*
    :   *Optional*. For supergroups, name of the group sticker set

    can_set_sticker_set*: bool | None*
    :   *Optional*. `True`, if the bot can change the group sticker set

    custom_emoji_sticker_set_name*: str | None*
    :   *Optional*. For supergroups, the name of the group’s custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group

    linked_chat_id*: int | None*
    :   *Optional*. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier

    location*: [ChatLocation](chat_location.html#aiogram.types.chat_location.ChatLocation "aiogram.types.chat_location.ChatLocation") | None*
    :   *Optional*. For supergroups, the location to which the supergroup is connected

    rating*: [UserRating](user_rating.html#aiogram.types.user_rating.UserRating "aiogram.types.user_rating.UserRating") | None*
    :   *Optional*. For private chats, the rating of the user if any

    first_profile_audio*: [Audio](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio") | None*
    :   *Optional*. For private chats, the first audio added to the profile of the user

    unique_gift_colors*: [UniqueGiftColors](unique_gift_colors.html#aiogram.types.unique_gift_colors.UniqueGiftColors "aiogram.types.unique_gift_colors.UniqueGiftColors") | None*
    :   *Optional*. The color scheme based on a unique gift that must be used for the chat’s name, message replies and link previews

    paid_message_star_count*: int | None*
    :   *Optional*. The number of Telegram Stars a general user has to pay to send a message to the chat

    guard_bot*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. The bot that processes join request queries in the chat. The field is only available to chat administrators

    community*: [Community](community.html#aiogram.types.community.Community "aiogram.types.community.Community") | None*
    :   *Optional*. The [`aiogram.types.community.Community`](community.html#aiogram.types.community.Community "aiogram.types.community.Community") to which the chat belongs

    can_send_gift*: bool | None*
    :   *Optional*. `True`, if gifts can be sent to the chat

        Deprecated since version API:9.0: <https://core.telegram.org/bots/api-changelog#april-11-2025>
