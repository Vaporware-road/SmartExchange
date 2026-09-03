# Message

> Source: [https://docs.aiogram.dev/en/latest/api/types/message.html](https://docs.aiogram.dev/en/latest/api/types/message.html)

*class* aiogram.types.message.Message(*\**, *message_id: int*, *date: _datetime_serializer, return_type=int, when_used=unless - none)]*, *chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*, *message_thread_id: int | None = None*, *direct_messages_topic: [DirectMessagesTopic](direct_messages_topic.html#aiogram.types.direct_messages_topic.DirectMessagesTopic "aiogram.types.direct_messages_topic.DirectMessagesTopic") | None = None*, *from_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *sender_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *sender_boost_count: int | None = None*, *sender_business_bot: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *sender_tag: str | None = None*, *guest_query_id: str | None = None*, *business_connection_id: str | None = None*, *forward_origin: Annotated[[MessageOriginUser](message_origin_user.html#aiogram.types.message_origin_user.MessageOriginUser "aiogram.types.message_origin_user.MessageOriginUser") | [MessageOriginHiddenUser](message_origin_hidden_user.html#aiogram.types.message_origin_hidden_user.MessageOriginHiddenUser "aiogram.types.message_origin_hidden_user.MessageOriginHiddenUser") | [MessageOriginChat](message_origin_chat.html#aiogram.types.message_origin_chat.MessageOriginChat "aiogram.types.message_origin_chat.MessageOriginChat") | [MessageOriginChannel](message_origin_channel.html#aiogram.types.message_origin_channel.MessageOriginChannel "aiogram.types.message_origin_channel.MessageOriginChannel"), FieldInfo(annotation=NoneType, required=True, discriminator='type')] | None = None*, *is_topic_message: bool | None = None*, *is_automatic_forward: bool | None = None*, *reply_to_message: [Message](#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *external_reply: [ExternalReplyInfo](external_reply_info.html#aiogram.types.external_reply_info.ExternalReplyInfo "aiogram.types.external_reply_info.ExternalReplyInfo") | None = None*, *quote: [TextQuote](text_quote.html#aiogram.types.text_quote.TextQuote "aiogram.types.text_quote.TextQuote") | None = None*, *reply_to_story: [Story](story.html#aiogram.types.story.Story "aiogram.types.story.Story") | None = None*, *reply_to_checklist_task_id: int | None = None*, *reply_to_poll_option_id: str | None = None*, *via_bot: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *guest_bot_caller_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *guest_bot_caller_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *edit_date: int | None = None*, *has_protected_content: bool | None = None*, *is_from_offline: bool | None = None*, *is_paid_post: bool | None = None*, *media_group_id: str | None = None*, *author_signature: str | None = None*, *paid_star_count: int | None = None*, *text: str | None = None*, *entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *link_preview_options: [LinkPreviewOptions](link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | None = None*, *suggested_post_info: [SuggestedPostInfo](suggested_post_info.html#aiogram.types.suggested_post_info.SuggestedPostInfo "aiogram.types.suggested_post_info.SuggestedPostInfo") | None = None*, *effect_id: str | None = None*, *animation: [Animation](animation.html#aiogram.types.animation.Animation "aiogram.types.animation.Animation") | None = None*, *audio: [Audio](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio") | None = None*, *document: [Document](document.html#aiogram.types.document.Document "aiogram.types.document.Document") | None = None*, *live_photo: [LivePhoto](live_photo.html#aiogram.types.live_photo.LivePhoto "aiogram.types.live_photo.LivePhoto") | None = None*, *paid_media: [PaidMediaInfo](paid_media_info.html#aiogram.types.paid_media_info.PaidMediaInfo "aiogram.types.paid_media_info.PaidMediaInfo") | None = None*, *photo: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None = None*, *sticker: [Sticker](sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker") | None = None*, *story: [Story](story.html#aiogram.types.story.Story "aiogram.types.story.Story") | None = None*, *video: [Video](video.html#aiogram.types.video.Video "aiogram.types.video.Video") | None = None*, *video_note: [VideoNote](video_note.html#aiogram.types.video_note.VideoNote "aiogram.types.video_note.VideoNote") | None = None*, *voice: [Voice](voice.html#aiogram.types.voice.Voice "aiogram.types.voice.Voice") | None = None*, *caption: str | None = None*, *caption_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *show_caption_above_media: bool | None = None*, *has_media_spoiler: bool | None = None*, *checklist: [Checklist](checklist.html#aiogram.types.checklist.Checklist "aiogram.types.checklist.Checklist") | None = None*, *contact: [Contact](contact.html#aiogram.types.contact.Contact "aiogram.types.contact.Contact") | None = None*, *dice: [Dice](dice.html#aiogram.types.dice.Dice "aiogram.types.dice.Dice") | None = None*, *game: [Game](game.html#aiogram.types.game.Game "aiogram.types.game.Game") | None = None*, *poll: [Poll](poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") | None = None*, *venue: [Venue](venue.html#aiogram.types.venue.Venue "aiogram.types.venue.Venue") | None = None*, *location: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location") | None = None*, *new_chat_members: list[[User](user.html#aiogram.types.user.User "aiogram.types.user.User")] | None = None*, *left_chat_member: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *chat_owner_left: [ChatOwnerLeft](chat_owner_left.html#aiogram.types.chat_owner_left.ChatOwnerLeft "aiogram.types.chat_owner_left.ChatOwnerLeft") | None = None*, *chat_owner_changed: [ChatOwnerChanged](chat_owner_changed.html#aiogram.types.chat_owner_changed.ChatOwnerChanged "aiogram.types.chat_owner_changed.ChatOwnerChanged") | None = None*, *new_chat_title: str | None = None*, *new_chat_photo: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None = None*, *delete_chat_photo: bool | None = None*, *group_chat_created: bool | None = None*, *supergroup_chat_created: bool | None = None*, *channel_chat_created: bool | None = None*, *message_auto_delete_timer_changed: [MessageAutoDeleteTimerChanged](message_auto_delete_timer_changed.html#aiogram.types.message_auto_delete_timer_changed.MessageAutoDeleteTimerChanged "aiogram.types.message_auto_delete_timer_changed.MessageAutoDeleteTimerChanged") | None = None*, *migrate_to_chat_id: int | None = None*, *migrate_from_chat_id: int | None = None*, *pinned_message: [Message](#aiogram.types.message.Message "aiogram.types.message.Message") | [InaccessibleMessage](inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage "aiogram.types.inaccessible_message.InaccessibleMessage") | None = None*, *invoice: [Invoice](invoice.html#aiogram.types.invoice.Invoice "aiogram.types.invoice.Invoice") | None = None*, *successful_payment: [SuccessfulPayment](successful_payment.html#aiogram.types.successful_payment.SuccessfulPayment "aiogram.types.successful_payment.SuccessfulPayment") | None = None*, *refunded_payment: [RefundedPayment](refunded_payment.html#aiogram.types.refunded_payment.RefundedPayment "aiogram.types.refunded_payment.RefundedPayment") | None = None*, *users_shared: [UsersShared](users_shared.html#aiogram.types.users_shared.UsersShared "aiogram.types.users_shared.UsersShared") | None = None*, *chat_shared: [ChatShared](chat_shared.html#aiogram.types.chat_shared.ChatShared "aiogram.types.chat_shared.ChatShared") | None = None*, *gift: [GiftInfo](gift_info.html#aiogram.types.gift_info.GiftInfo "aiogram.types.gift_info.GiftInfo") | None = None*, *unique_gift: [UniqueGiftInfo](unique_gift_info.html#aiogram.types.unique_gift_info.UniqueGiftInfo "aiogram.types.unique_gift_info.UniqueGiftInfo") | None = None*, *gift_upgrade_sent: [GiftInfo](gift_info.html#aiogram.types.gift_info.GiftInfo "aiogram.types.gift_info.GiftInfo") | None = None*, *connected_website: str | None = None*, *write_access_allowed: [WriteAccessAllowed](write_access_allowed.html#aiogram.types.write_access_allowed.WriteAccessAllowed "aiogram.types.write_access_allowed.WriteAccessAllowed") | None = None*, *passport_data: [PassportData](passport_data.html#aiogram.types.passport_data.PassportData "aiogram.types.passport_data.PassportData") | None = None*, *proximity_alert_triggered: [ProximityAlertTriggered](proximity_alert_triggered.html#aiogram.types.proximity_alert_triggered.ProximityAlertTriggered "aiogram.types.proximity_alert_triggered.ProximityAlertTriggered") | None = None*, *boost_added: [ChatBoostAdded](chat_boost_added.html#aiogram.types.chat_boost_added.ChatBoostAdded "aiogram.types.chat_boost_added.ChatBoostAdded") | None = None*, *chat_background_set: [ChatBackground](chat_background.html#aiogram.types.chat_background.ChatBackground "aiogram.types.chat_background.ChatBackground") | None = None*, *checklist_tasks_done: [ChecklistTasksDone](checklist_tasks_done.html#aiogram.types.checklist_tasks_done.ChecklistTasksDone "aiogram.types.checklist_tasks_done.ChecklistTasksDone") | None = None*, *checklist_tasks_added: [ChecklistTasksAdded](checklist_tasks_added.html#aiogram.types.checklist_tasks_added.ChecklistTasksAdded "aiogram.types.checklist_tasks_added.ChecklistTasksAdded") | None = None*, *direct_message_price_changed: [DirectMessagePriceChanged](direct_message_price_changed.html#aiogram.types.direct_message_price_changed.DirectMessagePriceChanged "aiogram.types.direct_message_price_changed.DirectMessagePriceChanged") | None = None*, *forum_topic_created: [ForumTopicCreated](forum_topic_created.html#aiogram.types.forum_topic_created.ForumTopicCreated "aiogram.types.forum_topic_created.ForumTopicCreated") | None = None*, *forum_topic_edited: [ForumTopicEdited](forum_topic_edited.html#aiogram.types.forum_topic_edited.ForumTopicEdited "aiogram.types.forum_topic_edited.ForumTopicEdited") | None = None*, *forum_topic_closed: [ForumTopicClosed](forum_topic_closed.html#aiogram.types.forum_topic_closed.ForumTopicClosed "aiogram.types.forum_topic_closed.ForumTopicClosed") | None = None*, *forum_topic_reopened: [ForumTopicReopened](forum_topic_reopened.html#aiogram.types.forum_topic_reopened.ForumTopicReopened "aiogram.types.forum_topic_reopened.ForumTopicReopened") | None = None*, *general_forum_topic_hidden: [GeneralForumTopicHidden](general_forum_topic_hidden.html#aiogram.types.general_forum_topic_hidden.GeneralForumTopicHidden "aiogram.types.general_forum_topic_hidden.GeneralForumTopicHidden") | None = None*, *general_forum_topic_unhidden: [GeneralForumTopicUnhidden](general_forum_topic_unhidden.html#aiogram.types.general_forum_topic_unhidden.GeneralForumTopicUnhidden "aiogram.types.general_forum_topic_unhidden.GeneralForumTopicUnhidden") | None = None*, *giveaway_created: [GiveawayCreated](giveaway_created.html#aiogram.types.giveaway_created.GiveawayCreated "aiogram.types.giveaway_created.GiveawayCreated") | None = None*, *giveaway: [Giveaway](giveaway.html#aiogram.types.giveaway.Giveaway "aiogram.types.giveaway.Giveaway") | None = None*, *giveaway_winners: [GiveawayWinners](giveaway_winners.html#aiogram.types.giveaway_winners.GiveawayWinners "aiogram.types.giveaway_winners.GiveawayWinners") | None = None*, *giveaway_completed: [GiveawayCompleted](giveaway_completed.html#aiogram.types.giveaway_completed.GiveawayCompleted "aiogram.types.giveaway_completed.GiveawayCompleted") | None = None*, *managed_bot_created: [ManagedBotCreated](managed_bot_created.html#aiogram.types.managed_bot_created.ManagedBotCreated "aiogram.types.managed_bot_created.ManagedBotCreated") | None = None*, *paid_message_price_changed: [PaidMessagePriceChanged](paid_message_price_changed.html#aiogram.types.paid_message_price_changed.PaidMessagePriceChanged "aiogram.types.paid_message_price_changed.PaidMessagePriceChanged") | None = None*, *poll_option_added: [PollOptionAdded](poll_option_added.html#aiogram.types.poll_option_added.PollOptionAdded "aiogram.types.poll_option_added.PollOptionAdded") | None = None*, *poll_option_deleted: [PollOptionDeleted](poll_option_deleted.html#aiogram.types.poll_option_deleted.PollOptionDeleted "aiogram.types.poll_option_deleted.PollOptionDeleted") | None = None*, *suggested_post_approved: [SuggestedPostApproved](suggested_post_approved.html#aiogram.types.suggested_post_approved.SuggestedPostApproved "aiogram.types.suggested_post_approved.SuggestedPostApproved") | None = None*, *suggested_post_approval_failed: [SuggestedPostApprovalFailed](suggested_post_approval_failed.html#aiogram.types.suggested_post_approval_failed.SuggestedPostApprovalFailed "aiogram.types.suggested_post_approval_failed.SuggestedPostApprovalFailed") | None = None*, *suggested_post_declined: [SuggestedPostDeclined](suggested_post_declined.html#aiogram.types.suggested_post_declined.SuggestedPostDeclined "aiogram.types.suggested_post_declined.SuggestedPostDeclined") | None = None*, *suggested_post_paid: [SuggestedPostPaid](suggested_post_paid.html#aiogram.types.suggested_post_paid.SuggestedPostPaid "aiogram.types.suggested_post_paid.SuggestedPostPaid") | None = None*, *suggested_post_refunded: [SuggestedPostRefunded](suggested_post_refunded.html#aiogram.types.suggested_post_refunded.SuggestedPostRefunded "aiogram.types.suggested_post_refunded.SuggestedPostRefunded") | None = None*, *video_chat_scheduled: [VideoChatScheduled](video_chat_scheduled.html#aiogram.types.video_chat_scheduled.VideoChatScheduled "aiogram.types.video_chat_scheduled.VideoChatScheduled") | None = None*, *video_chat_started: [VideoChatStarted](video_chat_started.html#aiogram.types.video_chat_started.VideoChatStarted "aiogram.types.video_chat_started.VideoChatStarted") | None = None*, *video_chat_ended: [VideoChatEnded](video_chat_ended.html#aiogram.types.video_chat_ended.VideoChatEnded "aiogram.types.video_chat_ended.VideoChatEnded") | None = None*, *video_chat_participants_invited: [VideoChatParticipantsInvited](video_chat_participants_invited.html#aiogram.types.video_chat_participants_invited.VideoChatParticipantsInvited "aiogram.types.video_chat_participants_invited.VideoChatParticipantsInvited") | None = None*, *web_app_data: [WebAppData](web_app_data.html#aiogram.types.web_app_data.WebAppData "aiogram.types.web_app_data.WebAppData") | None = None*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *rich_message: [RichMessage](rich_message.html#aiogram.types.rich_message.RichMessage "aiogram.types.rich_message.RichMessage") | None = None*, *receiver_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *ephemeral_message_id: int | None = None*, *community_chat_added: [CommunityChatAdded](community_chat_added.html#aiogram.types.community_chat_added.CommunityChatAdded "aiogram.types.community_chat_added.CommunityChatAdded") | None = None*, *community_chat_removed: [CommunityChatRemoved](community_chat_removed.html#aiogram.types.community_chat_removed.CommunityChatRemoved "aiogram.types.community_chat_removed.CommunityChatRemoved") | None = None*, *forward_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *forward_from: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *forward_from_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *forward_from_message_id: int | None = None*, *forward_sender_name: str | None = None*, *forward_signature: str | None = None*, *user_shared: [UserShared](user_shared.html#aiogram.types.user_shared.UserShared "aiogram.types.user_shared.UserShared") | None = None*, *\*\*extra_data: Any*)
:   This object represents a message.

    Source: <https://core.telegram.org/bots/api#message>

    message_id*: int*
    :   Unique message identifier inside this chat; 0 for ephemeral messages. In specific instances (e.g., a message containing a video sent to a big chat), the server might automatically schedule a message instead of sending it immediately. In such cases, this field will be 0 and the relevant message will be unusable until it is actually sent

    date*: DateTime*
    :   Date the message was sent in Unix time. It is always a positive number, representing a valid date

    chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*
    :   Chat the message belongs to

    message_thread_id*: int | None*
    :   *Optional*. Unique identifier of a message thread or forum topic to which the message belongs; for supergroups and private chats only

    direct_messages_topic*: [DirectMessagesTopic](direct_messages_topic.html#aiogram.types.direct_messages_topic.DirectMessagesTopic "aiogram.types.direct_messages_topic.DirectMessagesTopic") | None*
    :   *Optional*. Information about the direct messages chat topic that contains the message

    from_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. Sender of the message; may be empty for messages sent to channels. For backward compatibility, if the message was sent on behalf of a chat, the field contains a fake sender user in non-channel chats

    sender_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. Sender of the message when sent on behalf of a chat. For example, the supergroup itself for messages sent by its anonymous administrators or a linked channel for messages automatically forwarded to the channel’s discussion group. For backward compatibility, if the message was sent on behalf of a chat, the field *from* contains a fake sender user in non-channel chats

    sender_boost_count*: int | None*
    :   *Optional*. If the sender of the message boosted the chat, the number of boosts added by the user

    sender_business_bot*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. The bot that actually sent the message on behalf of the business account. Available only for outgoing messages sent on behalf of the connected business account

    sender_tag*: str | None*
    :   *Optional*. Tag or custom title of the sender of the message; for supergroups only

    guest_query_id*: str | None*
    :   *Optional*. The unique identifier for the guest query. Use this identifier with the method [`aiogram.methods.answer_guest_query.AnswerGuestQuery`](../methods/answer_guest_query.html#aiogram.methods.answer_guest_query.AnswerGuestQuery "aiogram.methods.answer_guest_query.AnswerGuestQuery") to send a response message. If non-empty, the message belongs to the chat where the guest bot was summoned, which may not coincide with other existing bot chats sharing the same identifier

    business_connection_id*: str | None*
    :   *Optional*. Unique identifier of the business connection from which the message was received. If non-empty, the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier

    forward_origin*: MessageOriginUnion | None*
    :   *Optional*. Information about the original message for forwarded messages

    is_topic_message*: bool | None*
    :   *Optional*. `True`, if the message is sent to a topic in a forum supergroup or a private chat with the bot

    is_automatic_forward*: bool | None*
    :   *Optional*. `True`, if the message is a channel post that was automatically forwarded to the connected discussion group

    reply_to_message*: [Message](#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. For replies in the same chat and message thread, the original message. Note that the [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") object in this field will not contain further *reply_to_message* fields even if it itself is a reply. If the message is a reply to an ephemeral message, then this field may be omitted

    external_reply*: [ExternalReplyInfo](external_reply_info.html#aiogram.types.external_reply_info.ExternalReplyInfo "aiogram.types.external_reply_info.ExternalReplyInfo") | None*
    :   *Optional*. Information about the message that is being replied to, which may come from another chat or forum topic

    quote*: [TextQuote](text_quote.html#aiogram.types.text_quote.TextQuote "aiogram.types.text_quote.TextQuote") | None*
    :   *Optional*. For replies that quote part of the original message, the quoted part of the message

    reply_to_story*: [Story](story.html#aiogram.types.story.Story "aiogram.types.story.Story") | None*
    :   *Optional*. For replies to a story, the original story

    reply_to_checklist_task_id*: int | None*
    :   *Optional*. Identifier of the specific checklist task that is being replied to

    reply_to_poll_option_id*: str | None*
    :   *Optional*. Persistent identifier of the specific poll option that is being replied to

    via_bot*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. Bot through which the message was sent

    guest_bot_caller_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. For a message sent by a guest bot, this is the user whose original message triggered the bot’s response

    guest_bot_caller_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. For a message sent by a guest bot, this is the chat whose original message triggered the bot’s response

    edit_date*: int | None*
    :   *Optional*. Date the message was last edited in Unix time

    has_protected_content*: bool | None*
    :   *Optional*. `True`, if the message can’t be forwarded

    is_from_offline*: bool | None*
    :   *Optional*. `True`, if the message was sent by an implicit action, for example, as an away or a greeting business message, or as a scheduled message

    is_paid_post*: bool | None*
    :   *Optional*. `True`, if the message is a paid post. Note that such posts must not be deleted for 24 hours to receive the payment and can’t be edited

    media_group_id*: str | None*
    :   *Optional*. The unique identifier inside this chat of a media message group this message belongs to

    author_signature*: str | None*
    :   *Optional*. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator

    paid_star_count*: int | None*
    :   *Optional*. The number of Telegram Stars that were paid by the sender of the message to send it

    text*: str | None*
    :   *Optional*. For text messages, the actual UTF-8 text of the message

    entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text

    link_preview_options*: [LinkPreviewOptions](link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | None*
    :   *Optional*. Options used for link preview generation for the message, if it is a text message and link preview options were changed

    suggested_post_info*: [SuggestedPostInfo](suggested_post_info.html#aiogram.types.suggested_post_info.SuggestedPostInfo "aiogram.types.suggested_post_info.SuggestedPostInfo") | None*
    :   *Optional*. Information about suggested post parameters if the message is a suggested post in a channel direct messages chat. If the message is an approved or declined suggested post, then it can’t be edited

    effect_id*: str | None*
    :   *Optional*. Unique identifier of the message effect added to the message

    animation*: [Animation](animation.html#aiogram.types.animation.Animation "aiogram.types.animation.Animation") | None*
    :   *Optional*. Message is an animation, information about the animation. For backward compatibility, when this field is set, the *document* field will also be set

    audio*: [Audio](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio") | None*
    :   *Optional*. Message is an audio file, information about the file

    document*: [Document](document.html#aiogram.types.document.Document "aiogram.types.document.Document") | None*
    :   *Optional*. Message is a general file, information about the file

    live_photo*: [LivePhoto](live_photo.html#aiogram.types.live_photo.LivePhoto "aiogram.types.live_photo.LivePhoto") | None*
    :   *Optional*. Message is a live photo, information about the live photo. For backward compatibility, when this field is set, the *photo* field will also be set

    paid_media*: [PaidMediaInfo](paid_media_info.html#aiogram.types.paid_media_info.PaidMediaInfo "aiogram.types.paid_media_info.PaidMediaInfo") | None*
    :   *Optional*. Message contains paid media; information about the paid media

    photo*: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None*
    :   *Optional*. Message is a photo, available sizes of the photo

    sticker*: [Sticker](sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker") | None*
    :   *Optional*. Message is a sticker, information about the sticker

    story*: [Story](story.html#aiogram.types.story.Story "aiogram.types.story.Story") | None*
    :   *Optional*. Message is a forwarded story

    video*: [Video](video.html#aiogram.types.video.Video "aiogram.types.video.Video") | None*
    :   *Optional*. Message is a video, information about the video

    video_note*: [VideoNote](video_note.html#aiogram.types.video_note.VideoNote "aiogram.types.video_note.VideoNote") | None*
    :   *Optional*. Message is a [video note](https://telegram.org/blog/video-messages-and-telescope), information about the video message

    voice*: [Voice](voice.html#aiogram.types.voice.Voice "aiogram.types.voice.Voice") | None*
    :   *Optional*. Message is a voice message, information about the file

    caption*: str | None*
    :   *Optional*. Caption for the animation, audio, document, paid media, photo, video or voice

    caption_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption

    show_caption_above_media*: bool | None*
    :   *Optional*. `True`, if the caption must be shown above the message media

    has_media_spoiler*: bool | None*
    :   *Optional*. `True`, if the message media is covered by a spoiler animation

    checklist*: [Checklist](checklist.html#aiogram.types.checklist.Checklist "aiogram.types.checklist.Checklist") | None*
    :   *Optional*. Message is a checklist

    contact*: [Contact](contact.html#aiogram.types.contact.Contact "aiogram.types.contact.Contact") | None*
    :   *Optional*. Message is a shared contact, information about the contact

    dice*: [Dice](dice.html#aiogram.types.dice.Dice "aiogram.types.dice.Dice") | None*
    :   *Optional*. Message is a dice with random value

    game*: [Game](game.html#aiogram.types.game.Game "aiogram.types.game.Game") | None*
    :   *Optional*. Message is a game, information about the game. [More about games »](https://core.telegram.org/bots/api#games)

    poll*: [Poll](poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") | None*
    :   *Optional*. Message is a native poll, information about the poll

    venue*: [Venue](venue.html#aiogram.types.venue.Venue "aiogram.types.venue.Venue") | None*
    :   *Optional*. Message is a venue, information about the venue. For backward compatibility, when this field is set, the *location* field will also be set

    location*: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location") | None*
    :   *Optional*. Message is a shared location, information about the location

    new_chat_members*: list[[User](user.html#aiogram.types.user.User "aiogram.types.user.User")] | None*
    :   *Optional*. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)

    left_chat_member*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. A member was removed from the group, information about them (this member may be the bot itself)

    chat_owner_left*: [ChatOwnerLeft](chat_owner_left.html#aiogram.types.chat_owner_left.ChatOwnerLeft "aiogram.types.chat_owner_left.ChatOwnerLeft") | None*
    :   *Optional*. Service message: chat owner has left

    chat_owner_changed*: [ChatOwnerChanged](chat_owner_changed.html#aiogram.types.chat_owner_changed.ChatOwnerChanged "aiogram.types.chat_owner_changed.ChatOwnerChanged") | None*
    :   *Optional*. Service message: chat owner has changed

    new_chat_title*: str | None*
    :   *Optional*. A chat title was changed to this value

    new_chat_photo*: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None*
    :   *Optional*. A chat photo was change to this value

    delete_chat_photo*: bool | None*
    :   *Optional*. Service message: the chat photo was deleted

    group_chat_created*: bool | None*
    :   *Optional*. Service message: the group has been created

    supergroup_chat_created*: bool | None*
    :   *Optional*. Service message: the supergroup has been created. This field can’t be received in a message coming through updates, because bot can’t be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup

    channel_chat_created*: bool | None*
    :   *Optional*. Service message: the channel has been created. This field can’t be received in a message coming through updates, because bot can’t be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel

    message_auto_delete_timer_changed*: [MessageAutoDeleteTimerChanged](message_auto_delete_timer_changed.html#aiogram.types.message_auto_delete_timer_changed.MessageAutoDeleteTimerChanged "aiogram.types.message_auto_delete_timer_changed.MessageAutoDeleteTimerChanged") | None*
    :   *Optional*. Service message: auto-delete timer settings changed in the chat

    migrate_to_chat_id*: int | None*
    :   *Optional*. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier

    migrate_from_chat_id*: int | None*
    :   *Optional*. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier

    pinned_message*: MaybeInaccessibleMessageUnion | None*
    :   *Optional*. Specified message was pinned. Note that the [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") object in this field will not contain further *reply_to_message* fields even if it itself is a reply

    invoice*: [Invoice](invoice.html#aiogram.types.invoice.Invoice "aiogram.types.invoice.Invoice") | None*
    :   *Optional*. Message is an invoice for a [payment](https://core.telegram.org/bots/api#payments), information about the invoice. [More about payments »](https://core.telegram.org/bots/api#payments)

    successful_payment*: [SuccessfulPayment](successful_payment.html#aiogram.types.successful_payment.SuccessfulPayment "aiogram.types.successful_payment.SuccessfulPayment") | None*
    :   *Optional*. Message is a service message about a successful payment, information about the payment. [More about payments »](https://core.telegram.org/bots/api#payments)

    refunded_payment*: [RefundedPayment](refunded_payment.html#aiogram.types.refunded_payment.RefundedPayment "aiogram.types.refunded_payment.RefundedPayment") | None*
    :   *Optional*. Message is a service message about a refunded payment, information about the payment. [More about payments »](https://core.telegram.org/bots/api#payments)

    users_shared*: [UsersShared](users_shared.html#aiogram.types.users_shared.UsersShared "aiogram.types.users_shared.UsersShared") | None*
    :   *Optional*. Service message: users were shared with the bot

    chat_shared*: [ChatShared](chat_shared.html#aiogram.types.chat_shared.ChatShared "aiogram.types.chat_shared.ChatShared") | None*
    :   *Optional*. Service message: a chat was shared with the bot

    gift*: [GiftInfo](gift_info.html#aiogram.types.gift_info.GiftInfo "aiogram.types.gift_info.GiftInfo") | None*
    :   *Optional*. Service message: a regular gift was sent or received

    unique_gift*: [UniqueGiftInfo](unique_gift_info.html#aiogram.types.unique_gift_info.UniqueGiftInfo "aiogram.types.unique_gift_info.UniqueGiftInfo") | None*
    :   *Optional*. Service message: a unique gift was sent or received

    gift_upgrade_sent*: [GiftInfo](gift_info.html#aiogram.types.gift_info.GiftInfo "aiogram.types.gift_info.GiftInfo") | None*
    :   *Optional*. Service message: upgrade of a gift was purchased after the gift was sent

    connected_website*: str | None*
    :   *Optional*. The domain name of the website on which the user has logged in. [More about Telegram Login »](https://core.telegram.org/widgets/login)

    write_access_allowed*: [WriteAccessAllowed](write_access_allowed.html#aiogram.types.write_access_allowed.WriteAccessAllowed "aiogram.types.write_access_allowed.WriteAccessAllowed") | None*
    :   *Optional*. Service message: the user allowed the bot to write messages after adding it to the attachment or side menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method [requestWriteAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps)

    passport_data*: [PassportData](passport_data.html#aiogram.types.passport_data.PassportData "aiogram.types.passport_data.PassportData") | None*
    :   *Optional*. Telegram Passport data

    proximity_alert_triggered*: [ProximityAlertTriggered](proximity_alert_triggered.html#aiogram.types.proximity_alert_triggered.ProximityAlertTriggered "aiogram.types.proximity_alert_triggered.ProximityAlertTriggered") | None*
    :   *Optional*. Service message. A user in the chat triggered another user’s proximity alert while sharing Live Location

    boost_added*: [ChatBoostAdded](chat_boost_added.html#aiogram.types.chat_boost_added.ChatBoostAdded "aiogram.types.chat_boost_added.ChatBoostAdded") | None*
    :   *Optional*. Service message: user boosted the chat

    chat_background_set*: [ChatBackground](chat_background.html#aiogram.types.chat_background.ChatBackground "aiogram.types.chat_background.ChatBackground") | None*
    :   *Optional*. Service message: chat background set

    checklist_tasks_done*: [ChecklistTasksDone](checklist_tasks_done.html#aiogram.types.checklist_tasks_done.ChecklistTasksDone "aiogram.types.checklist_tasks_done.ChecklistTasksDone") | None*
    :   *Optional*. Service message: some tasks in a checklist were marked as done or not done

    checklist_tasks_added*: [ChecklistTasksAdded](checklist_tasks_added.html#aiogram.types.checklist_tasks_added.ChecklistTasksAdded "aiogram.types.checklist_tasks_added.ChecklistTasksAdded") | None*
    :   *Optional*. Service message: tasks were added to a checklist

    direct_message_price_changed*: [DirectMessagePriceChanged](direct_message_price_changed.html#aiogram.types.direct_message_price_changed.DirectMessagePriceChanged "aiogram.types.direct_message_price_changed.DirectMessagePriceChanged") | None*
    :   *Optional*. Service message: the price for paid messages in the corresponding direct messages chat of a channel has changed

    forum_topic_created*: [ForumTopicCreated](forum_topic_created.html#aiogram.types.forum_topic_created.ForumTopicCreated "aiogram.types.forum_topic_created.ForumTopicCreated") | None*
    :   *Optional*. Service message: forum topic created

    forum_topic_edited*: [ForumTopicEdited](forum_topic_edited.html#aiogram.types.forum_topic_edited.ForumTopicEdited "aiogram.types.forum_topic_edited.ForumTopicEdited") | None*
    :   *Optional*. Service message: forum topic edited

    forum_topic_closed*: [ForumTopicClosed](forum_topic_closed.html#aiogram.types.forum_topic_closed.ForumTopicClosed "aiogram.types.forum_topic_closed.ForumTopicClosed") | None*
    :   *Optional*. Service message: forum topic closed

    forum_topic_reopened*: [ForumTopicReopened](forum_topic_reopened.html#aiogram.types.forum_topic_reopened.ForumTopicReopened "aiogram.types.forum_topic_reopened.ForumTopicReopened") | None*
    :   *Optional*. Service message: forum topic reopened

    general_forum_topic_hidden*: [GeneralForumTopicHidden](general_forum_topic_hidden.html#aiogram.types.general_forum_topic_hidden.GeneralForumTopicHidden "aiogram.types.general_forum_topic_hidden.GeneralForumTopicHidden") | None*
    :   *Optional*. Service message: the ‘General’ forum topic hidden

    general_forum_topic_unhidden*: [GeneralForumTopicUnhidden](general_forum_topic_unhidden.html#aiogram.types.general_forum_topic_unhidden.GeneralForumTopicUnhidden "aiogram.types.general_forum_topic_unhidden.GeneralForumTopicUnhidden") | None*
    :   *Optional*. Service message: the ‘General’ forum topic unhidden

    giveaway_created*: [GiveawayCreated](giveaway_created.html#aiogram.types.giveaway_created.GiveawayCreated "aiogram.types.giveaway_created.GiveawayCreated") | None*
    :   *Optional*. Service message: a scheduled giveaway was created

    giveaway*: [Giveaway](giveaway.html#aiogram.types.giveaway.Giveaway "aiogram.types.giveaway.Giveaway") | None*
    :   *Optional*. The message is a scheduled giveaway message

    giveaway_winners*: [GiveawayWinners](giveaway_winners.html#aiogram.types.giveaway_winners.GiveawayWinners "aiogram.types.giveaway_winners.GiveawayWinners") | None*
    :   *Optional*. A giveaway with public winners was completed

    giveaway_completed*: [GiveawayCompleted](giveaway_completed.html#aiogram.types.giveaway_completed.GiveawayCompleted "aiogram.types.giveaway_completed.GiveawayCompleted") | None*
    :   *Optional*. Service message: a giveaway without public winners was completed

    managed_bot_created*: [ManagedBotCreated](managed_bot_created.html#aiogram.types.managed_bot_created.ManagedBotCreated "aiogram.types.managed_bot_created.ManagedBotCreated") | None*
    :   *Optional*. Service message: user created a bot that will be managed by the current bot

    paid_message_price_changed*: [PaidMessagePriceChanged](paid_message_price_changed.html#aiogram.types.paid_message_price_changed.PaidMessagePriceChanged "aiogram.types.paid_message_price_changed.PaidMessagePriceChanged") | None*
    :   *Optional*. Service message: the price for paid messages has changed in the chat

    poll_option_added*: [PollOptionAdded](poll_option_added.html#aiogram.types.poll_option_added.PollOptionAdded "aiogram.types.poll_option_added.PollOptionAdded") | None*
    :   *Optional*. Service message: answer option was added to a poll

    poll_option_deleted*: [PollOptionDeleted](poll_option_deleted.html#aiogram.types.poll_option_deleted.PollOptionDeleted "aiogram.types.poll_option_deleted.PollOptionDeleted") | None*
    :   *Optional*. Service message: answer option was deleted from a poll

    suggested_post_approved*: [SuggestedPostApproved](suggested_post_approved.html#aiogram.types.suggested_post_approved.SuggestedPostApproved "aiogram.types.suggested_post_approved.SuggestedPostApproved") | None*
    :   *Optional*. Service message: a suggested post was approved

    suggested_post_approval_failed*: [SuggestedPostApprovalFailed](suggested_post_approval_failed.html#aiogram.types.suggested_post_approval_failed.SuggestedPostApprovalFailed "aiogram.types.suggested_post_approval_failed.SuggestedPostApprovalFailed") | None*
    :   *Optional*. Service message: approval of a suggested post has failed

    suggested_post_declined*: [SuggestedPostDeclined](suggested_post_declined.html#aiogram.types.suggested_post_declined.SuggestedPostDeclined "aiogram.types.suggested_post_declined.SuggestedPostDeclined") | None*
    :   *Optional*. Service message: a suggested post was declined

    suggested_post_paid*: [SuggestedPostPaid](suggested_post_paid.html#aiogram.types.suggested_post_paid.SuggestedPostPaid "aiogram.types.suggested_post_paid.SuggestedPostPaid") | None*
    :   *Optional*. Service message: payment for a suggested post was received

    suggested_post_refunded*: [SuggestedPostRefunded](suggested_post_refunded.html#aiogram.types.suggested_post_refunded.SuggestedPostRefunded "aiogram.types.suggested_post_refunded.SuggestedPostRefunded") | None*
    :   *Optional*. Service message: payment for a suggested post was refunded

    video_chat_scheduled*: [VideoChatScheduled](video_chat_scheduled.html#aiogram.types.video_chat_scheduled.VideoChatScheduled "aiogram.types.video_chat_scheduled.VideoChatScheduled") | None*
    :   *Optional*. Service message: video chat scheduled

    video_chat_started*: [VideoChatStarted](video_chat_started.html#aiogram.types.video_chat_started.VideoChatStarted "aiogram.types.video_chat_started.VideoChatStarted") | None*
    :   *Optional*. Service message: video chat started

    video_chat_ended*: [VideoChatEnded](video_chat_ended.html#aiogram.types.video_chat_ended.VideoChatEnded "aiogram.types.video_chat_ended.VideoChatEnded") | None*
    :   *Optional*. Service message: video chat ended

    video_chat_participants_invited*: [VideoChatParticipantsInvited](video_chat_participants_invited.html#aiogram.types.video_chat_participants_invited.VideoChatParticipantsInvited "aiogram.types.video_chat_participants_invited.VideoChatParticipantsInvited") | None*
    :   *Optional*. Service message: new participants invited to a video chat

    web_app_data*: [WebAppData](web_app_data.html#aiogram.types.web_app_data.WebAppData "aiogram.types.web_app_data.WebAppData") | None*
    :   *Optional*. Service message: data sent by a Web App

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message. `login_url` buttons are represented as ordinary `url` buttons

    rich_message*: [RichMessage](rich_message.html#aiogram.types.rich_message.RichMessage "aiogram.types.rich_message.RichMessage") | None*
    :   *Optional*. Message is a rich formatted message

    receiver_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. For ephemeral messages, the user who received the message

    ephemeral_message_id*: int | None*
    :   *Optional*. For ephemeral messages, identifier of the ephemeral message inside this chat. The identifier may be reused for another ephemeral message after the message is deleted or expires

    community_chat_added*: [CommunityChatAdded](community_chat_added.html#aiogram.types.community_chat_added.CommunityChatAdded "aiogram.types.community_chat_added.CommunityChatAdded") | None*
    :   *Optional*. Service message: chat added to a [`aiogram.types.community.Community`](community.html#aiogram.types.community.Community "aiogram.types.community.Community")

    community_chat_removed*: [CommunityChatRemoved](community_chat_removed.html#aiogram.types.community_chat_removed.CommunityChatRemoved "aiogram.types.community_chat_removed.CommunityChatRemoved") | None*
    :   *Optional*. Service message: chat removed from a [`aiogram.types.community.Community`](community.html#aiogram.types.community.Community "aiogram.types.community.Community")

    forward_date*: DateTime | None*
    :   *Optional*. For forwarded messages, date the original message was sent in Unix time

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    forward_from*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. For forwarded messages, sender of the original message

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    forward_from_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. For messages forwarded from channels or from anonymous administrators, information about the original sender chat

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    forward_from_message_id*: int | None*
    :   *Optional*. For messages forwarded from channels, identifier of the original message in the channel

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    forward_sender_name*: str | None*
    :   *Optional*. Sender’s name for messages forwarded from users who disallow adding a link to their account in forwarded messages

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    forward_signature*: str | None*
    :   *Optional*. For forwarded messages that were originally sent in channels or by an anonymous chat administrator, signature of the message sender if present

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    user_shared*: [UserShared](user_shared.html#aiogram.types.user_shared.UserShared "aiogram.types.user_shared.UserShared") | None*
    :   *Optional*. Service message: a user was shared with the bot

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    *property* content_type*: str*

    *property* html_text*: str*

    *property* md_text*: str*

    as_reply_parameters(*allow_sending_without_reply: bool | Default | None = <Default('allow_sending_without_reply')>*, *quote: str | None = None*, *quote_parse_mode: str | Default | None = <Default('parse_mode')>*, *quote_entities: list[MessageEntity] | None = None*, *quote_position: int | None = None*) → [ReplyParameters](reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters")

    reply_animation(*animation: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *duration: int | None = None*, *width: int | None = None*, *height: int | None = None*, *thumbnail: InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendAnimation](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation")
    :   Shortcut for method [`aiogram.methods.send_animation.SendAnimation`](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#sendanimation>

        Parameters:
        :   - **animation** – Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **duration** – Duration of sent animation in seconds
            - **width** – Animation width
            - **height** – Animation height
            - **thumbnail** – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)
            - **caption** – Animation caption (may also be used when resending animation by *file_id*), 0-1024 characters after entities parsing
            - **parse_mode** – Mode for parsing entities in the animation caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **show_caption_above_media** – Pass `True` if the caption must be shown above the message media
            - **has_spoiler** – Pass `True` if the animation needs to be covered with a spoiler animation
            - **disable_notification** – Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** – Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_animation.SendAnimation`](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation")

    answer_animation(*animation: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *duration: int | None = None*, *width: int | None = None*, *height: int | None = None*, *thumbnail: InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendAnimation](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation")
    :   Shortcut for method [`aiogram.methods.send_animation.SendAnimation`](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#sendanimation>

        Parameters:
        :   - **animation** – Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **duration** – Duration of sent animation in seconds
            - **width** – Animation width
            - **height** – Animation height
            - **thumbnail** – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)
            - **caption** – Animation caption (may also be used when resending animation by *file_id*), 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the animation caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **show_caption_above_media** – Pass `True` if the caption must be shown above the message media
            - **has_spoiler** – Pass `True` if the animation needs to be covered with a spoiler animation
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** – For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_animation.SendAnimation`](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation")

    reply_audio(*audio: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *duration: int | None = None*, *performer: str | None = None*, *title: str | None = None*, *thumbnail: InputFile | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendAudio](../methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio")
    :   Shortcut for method [`aiogram.methods.send_audio.SendAudio`](../methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
        For sending voice messages, use the [`aiogram.methods.send_voice.SendVoice`](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice") method instead.

        Source: <https://core.telegram.org/bots/api#sendaudio>

        Parameters:
        :   - **audio** – Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **caption** – Audio caption, 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **duration** – Duration of the audio in seconds
            - **performer** – Performer
            - **title** – Track name
            - **thumbnail** – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_audio.SendAudio`](../methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio")

    answer_audio(*audio: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *duration: int | None = None*, *performer: str | None = None*, *title: str | None = None*, *thumbnail: InputFile | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendAudio](../methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio")
    :   Shortcut for method [`aiogram.methods.send_audio.SendAudio`](../methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
        For sending voice messages, use the [`aiogram.methods.send_voice.SendVoice`](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice") method instead.

        Source: <https://core.telegram.org/bots/api#sendaudio>

        Parameters:
        :   - **audio** – Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **caption** – Audio caption, 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **duration** – Duration of the audio in seconds
            - **performer** – Performer
            - **title** – Track name
            - **thumbnail** – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_audio.SendAudio`](../methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio")

    reply_contact(*phone_number: str*, *first_name: str*, *direct_messages_topic_id: int | None = None*, *last_name: str | None = None*, *vcard: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendContact](../methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact")
    :   Shortcut for method [`aiogram.methods.send_contact.SendContact`](../methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send phone contacts. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendcontact>

        Parameters:
        :   - **phone_number** – Contact’s phone number
            - **first_name** – Contact’s first name
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **last_name** – Contact’s last name
            - **vcard** – Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_contact.SendContact`](../methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact")

    answer_contact(*phone_number: str*, *first_name: str*, *direct_messages_topic_id: int | None = None*, *last_name: str | None = None*, *vcard: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendContact](../methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact")
    :   Shortcut for method [`aiogram.methods.send_contact.SendContact`](../methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send phone contacts. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendcontact>

        Parameters:
        :   - **phone_number** – Contact’s phone number
            - **first_name** – Contact’s first name
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **last_name** – Contact’s last name
            - **vcard** –

              Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_contact.SendContact`](../methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact")

    reply_document(*document: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *thumbnail: InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *disable_content_type_detection: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendDocument](../methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument")
    :   Shortcut for method [`aiogram.methods.send_document.SendDocument`](../methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send general files. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#senddocument>

        Parameters:
        :   - **document** – File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **thumbnail** – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)
            - **caption** – Document caption (may also be used when resending documents by *file_id*), 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **disable_content_type_detection** – Disables automatic server-side content type detection for files uploaded using multipart/form-data
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_document.SendDocument`](../methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument")

    answer_document(*document: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *thumbnail: InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *disable_content_type_detection: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendDocument](../methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument")
    :   Shortcut for method [`aiogram.methods.send_document.SendDocument`](../methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send general files. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#senddocument>

        Parameters:
        :   - **document** – File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **thumbnail** – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)
            - **caption** – Document caption (may also be used when resending documents by *file_id*), 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **disable_content_type_detection** – Disables automatic server-side content type detection for files uploaded using multipart/form-data
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_document.SendDocument`](../methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument")

    reply_game(*game_short_name: str*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *reply_markup: InlineKeyboardMarkup | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendGame](../methods/send_game.html#aiogram.methods.send_game.SendGame "aiogram.methods.send_game.SendGame")
    :   Shortcut for method [`aiogram.methods.send_game.SendGame`](../methods/send_game.html#aiogram.methods.send_game.SendGame "aiogram.methods.send_game.SendGame")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send a game. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendgame>

        Parameters:
        :   - **game_short_name** – Short name of the game, serves as the unique identifier for the game. Set up your games via [@BotFather](https://t.me/botfather)
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **reply_markup** –

              A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards). If empty, one ‘Play game_title’ button will be shown. If not empty, the first button must launch the game
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_game.SendGame`](../methods/send_game.html#aiogram.methods.send_game.SendGame "aiogram.methods.send_game.SendGame")

    answer_game(*game_short_name: str*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: InlineKeyboardMarkup | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendGame](../methods/send_game.html#aiogram.methods.send_game.SendGame "aiogram.methods.send_game.SendGame")
    :   Shortcut for method [`aiogram.methods.send_game.SendGame`](../methods/send_game.html#aiogram.methods.send_game.SendGame "aiogram.methods.send_game.SendGame")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send a game. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendgame>

        Parameters:
        :   - **game_short_name** –

              Short name of the game, serves as the unique identifier for the game. Set up your games via [@BotFather](https://t.me/botfather)
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards). If empty, one ‘Play game_title’ button will be shown. If not empty, the first button must launch the game
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_game.SendGame`](../methods/send_game.html#aiogram.methods.send_game.SendGame "aiogram.methods.send_game.SendGame")

    reply_invoice(*title: str, description: str, payload: str, currency: str, prices: list[LabeledPrice], direct_messages_topic_id: int | None = None, provider_token: str | None = None, max_tip_amount: int | None = None, suggested_tip_amounts: list[int] | None = None, start_parameter: str | None = None, provider_data: str | None = None, photo_url: str | None = None, photo_size: int | None = None, photo_width: int | None = None, photo_height: int | None = None, need_name: bool | None = None, need_phone_number: bool | None = None, need_email: bool | None = None, need_shipping_address: bool | None = None, send_phone_number_to_provider: bool | None = None, send_email_to_provider: bool | None = None, is_flexible: bool | None = None, disable_notification: bool | None = None, protect_content: bool | Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_markup: InlineKeyboardMarkup | None = None, allow_sending_without_reply: bool | None = None, \*\*kwargs: Any*) → [SendInvoice](../methods/send_invoice.html#aiogram.methods.send_invoice.SendInvoice "aiogram.methods.send_invoice.SendInvoice")
    :   Shortcut for method [`aiogram.methods.send_invoice.SendInvoice`](../methods/send_invoice.html#aiogram.methods.send_invoice.SendInvoice "aiogram.methods.send_invoice.SendInvoice")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send invoices. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendinvoice>

        Parameters:
        :   - **title** – Product name, 1-32 characters
            - **description** – Product description, 1-255 characters
            - **payload** – Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes
            - **currency** – Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies). Pass ‘XTR’ for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **prices** –

              Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **provider_token** –

              Payment provider token, obtained via [@BotFather](https://t.me/botfather). Pass an empty string for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **max_tip_amount** –

              The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of `US$ 1.45` pass `max_tip_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **suggested_tip_amounts** – A JSON-serialized Array of suggested amounts of tips in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*
            - **start_parameter** – Unique deep-linking parameter. If left empty, **forwarded copies** of the sent message will have a *Pay* button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a *URL* button with a deep link to the bot (instead of a *Pay* button), with the value used as the start parameter
            - **provider_data** – JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider
            - **photo_url** – URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for
            - **photo_size** – Photo size in bytes
            - **photo_width** – Photo width
            - **photo_height** – Photo height
            - **need_name** –

              Pass `True` if you require the user’s full name to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **need_phone_number** –

              Pass `True` if you require the user’s phone number to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **need_email** –

              Pass `True` if you require the user’s email address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **need_shipping_address** –

              Pass `True` if you require the user’s shipping address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **send_phone_number_to_provider** –

              Pass `True` if the user’s phone number should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **send_email_to_provider** –

              Pass `True` if the user’s email address should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **is_flexible** –

              Pass `True` if the final price depends on the shipping method. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards). If empty, one ‘Pay `total price`’ button will be shown. If not empty, the first button must be a Pay button
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_invoice.SendInvoice`](../methods/send_invoice.html#aiogram.methods.send_invoice.SendInvoice "aiogram.methods.send_invoice.SendInvoice")

    answer_invoice(*title: str, description: str, payload: str, currency: str, prices: list[LabeledPrice], direct_messages_topic_id: int | None = None, provider_token: str | None = None, max_tip_amount: int | None = None, suggested_tip_amounts: list[int] | None = None, start_parameter: str | None = None, provider_data: str | None = None, photo_url: str | None = None, photo_size: int | None = None, photo_width: int | None = None, photo_height: int | None = None, need_name: bool | None = None, need_phone_number: bool | None = None, need_email: bool | None = None, need_shipping_address: bool | None = None, send_phone_number_to_provider: bool | None = None, send_email_to_provider: bool | None = None, is_flexible: bool | None = None, disable_notification: bool | None = None, protect_content: bool | Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: InlineKeyboardMarkup | None = None, allow_sending_without_reply: bool | None = None, reply_to_message_id: int | None = None, \*\*kwargs: Any*) → [SendInvoice](../methods/send_invoice.html#aiogram.methods.send_invoice.SendInvoice "aiogram.methods.send_invoice.SendInvoice")
    :   Shortcut for method [`aiogram.methods.send_invoice.SendInvoice`](../methods/send_invoice.html#aiogram.methods.send_invoice.SendInvoice "aiogram.methods.send_invoice.SendInvoice")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send invoices. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendinvoice>

        Parameters:
        :   - **title** – Product name, 1-32 characters
            - **description** – Product description, 1-255 characters
            - **payload** – Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes
            - **currency** –

              Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies). Pass ‘XTR’ for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **prices** –

              Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **provider_token** –

              Payment provider token, obtained via [@BotFather](https://t.me/botfather). Pass an empty string for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **max_tip_amount** –

              The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of `US$ 1.45` pass `max_tip_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **suggested_tip_amounts** – A JSON-serialized Array of suggested amounts of tips in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*
            - **start_parameter** – Unique deep-linking parameter. If left empty, **forwarded copies** of the sent message will have a *Pay* button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a *URL* button with a deep link to the bot (instead of a *Pay* button), with the value used as the start parameter
            - **provider_data** – JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider
            - **photo_url** – URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for
            - **photo_size** – Photo size in bytes
            - **photo_width** – Photo width
            - **photo_height** – Photo height
            - **need_name** –

              Pass `True` if you require the user’s full name to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **need_phone_number** –

              Pass `True` if you require the user’s phone number to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **need_email** –

              Pass `True` if you require the user’s email address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **need_shipping_address** –

              Pass `True` if you require the user’s shipping address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **send_phone_number_to_provider** –

              Pass `True` if the user’s phone number should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **send_email_to_provider** –

              Pass `True` if the user’s email address should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **is_flexible** –

              Pass `True` if the final price depends on the shipping method. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards). If empty, one ‘Pay `total price`’ button will be shown. If not empty, the first button must be a Pay button
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_invoice.SendInvoice`](../methods/send_invoice.html#aiogram.methods.send_invoice.SendInvoice "aiogram.methods.send_invoice.SendInvoice")

    reply_location(*latitude: float*, *longitude: float*, *direct_messages_topic_id: int | None = None*, *horizontal_accuracy: float | None = None*, *live_period: int | None = None*, *heading: int | None = None*, *proximity_alert_radius: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendLocation](../methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation")
    :   Shortcut for method [`aiogram.methods.send_location.SendLocation`](../methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send point on the map. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendlocation>

        Parameters:
        :   - **latitude** – Latitude of the location
            - **longitude** – Longitude of the location
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **horizontal_accuracy** – The radius of uncertainty for the location, measured in meters; 0-1500
            - **live_period** – Period in seconds during which the location will be updated (see [Live Locations](https://telegram.org/blog/live-locations)), must be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely. Must be 0 for ephemeral messages
            - **heading** – For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified
            - **proximity_alert_radius** – For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_location.SendLocation`](../methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation")

    answer_location(*latitude: float*, *longitude: float*, *direct_messages_topic_id: int | None = None*, *horizontal_accuracy: float | None = None*, *live_period: int | None = None*, *heading: int | None = None*, *proximity_alert_radius: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendLocation](../methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation")
    :   Shortcut for method [`aiogram.methods.send_location.SendLocation`](../methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send point on the map. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendlocation>

        Parameters:
        :   - **latitude** – Latitude of the location
            - **longitude** – Longitude of the location
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **horizontal_accuracy** – The radius of uncertainty for the location, measured in meters; 0-1500
            - **live_period** –

              Period in seconds during which the location will be updated (see [Live Locations](https://telegram.org/blog/live-locations)), must be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely. Must be 0 for ephemeral messages
            - **heading** – For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified
            - **proximity_alert_radius** – For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_location.SendLocation`](../methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation")

    reply_media_group(*media: list[MediaUnion], direct_messages_topic_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, allow_sending_without_reply: bool | None = None, \*\*kwargs: Any*) → [SendMediaGroup](../methods/send_media_group.html#aiogram.methods.send_media_group.SendMediaGroup "aiogram.methods.send_media_group.SendMediaGroup")
    :   Shortcut for method [`aiogram.methods.send_media_group.SendMediaGroup`](../methods/send_media_group.html#aiogram.methods.send_media_group.SendMediaGroup "aiogram.methods.send_media_group.SendMediaGroup")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send a group of photos, live photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an Array of [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") objects that were sent is returned.

        Source: <https://core.telegram.org/bots/api#sendmediagroup>

        Parameters:
        :   - **media** – A JSON-serialized Array describing messages to be sent, must include 2-10 items
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat
            - **disable_notification** –

              Sends messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent messages from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_media_group.SendMediaGroup`](../methods/send_media_group.html#aiogram.methods.send_media_group.SendMediaGroup "aiogram.methods.send_media_group.SendMediaGroup")

    answer_media_group(*media: list[MediaUnion], direct_messages_topic_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_parameters: ReplyParameters | None = None, allow_sending_without_reply: bool | None = None, reply_to_message_id: int | None = None, \*\*kwargs: Any*) → [SendMediaGroup](../methods/send_media_group.html#aiogram.methods.send_media_group.SendMediaGroup "aiogram.methods.send_media_group.SendMediaGroup")
    :   Shortcut for method [`aiogram.methods.send_media_group.SendMediaGroup`](../methods/send_media_group.html#aiogram.methods.send_media_group.SendMediaGroup "aiogram.methods.send_media_group.SendMediaGroup")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send a group of photos, live photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an Array of [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") objects that were sent is returned.

        Source: <https://core.telegram.org/bots/api#sendmediagroup>

        Parameters:
        :   - **media** – A JSON-serialized Array describing messages to be sent, must include 2-10 items
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat
            - **disable_notification** –

              Sends messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent messages from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **reply_parameters** – Description of the message to reply to
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the messages are a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_media_group.SendMediaGroup`](../methods/send_media_group.html#aiogram.methods.send_media_group.SendMediaGroup "aiogram.methods.send_media_group.SendMediaGroup")

    reply(*text: str*, *direct_messages_topic_id: int | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *entities: list[MessageEntity] | None = None*, *link_preview_options: LinkPreviewOptions | Default | None = <Default('link_preview')>*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *disable_web_page_preview: bool | Default | None = <Default('link_preview_is_disabled')>*, *\*\*kwargs: Any*) → [SendMessage](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage")
    :   Shortcut for method [`aiogram.methods.send_message.SendMessage`](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send text messages. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendmessage>

        Parameters:
        :   - **text** – Text of the message to be sent, 1-4096 characters after entities parsing
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **parse_mode** –

              Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **entities** – A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*
            - **link_preview_options** – Link preview generation options for the message
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **disable_web_page_preview** – Disables link previews for links in this message

        Returns:
        :   instance of method [`aiogram.methods.send_message.SendMessage`](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage")

    answer(*text: str*, *direct_messages_topic_id: int | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *entities: list[MessageEntity] | None = None*, *link_preview_options: LinkPreviewOptions | Default | None = <Default('link_preview')>*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *disable_web_page_preview: bool | Default | None = <Default('link_preview_is_disabled')>*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendMessage](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage")
    :   Shortcut for method [`aiogram.methods.send_message.SendMessage`](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send text messages. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendmessage>

        Parameters:
        :   - **text** – Text of the message to be sent, 1-4096 characters after entities parsing
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **parse_mode** –

              Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **entities** – A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*
            - **link_preview_options** – Link preview generation options for the message
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **disable_web_page_preview** – Disables link previews for links in this message
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_message.SendMessage`](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage")

    reply_photo(*photo: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendPhoto](../methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto")
    :   Shortcut for method [`aiogram.methods.send_photo.SendPhoto`](../methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send photos. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendphoto>

        Parameters:
        :   - **photo** – Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo’s width and height must not exceed 10000 in total. Width and height ratio must be at most 20. [More information on Sending Files »](../upload_file.html#sending-files)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **caption** – Photo caption (may also be used when resending photos by *file_id*), 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **show_caption_above_media** – Pass `True` if the caption must be shown above the message media
            - **has_spoiler** – Pass `True` if the photo needs to be covered with a spoiler animation
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_photo.SendPhoto`](../methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto")

    answer_photo(*photo: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendPhoto](../methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto")
    :   Shortcut for method [`aiogram.methods.send_photo.SendPhoto`](../methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send photos. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendphoto>

        Parameters:
        :   - **photo** – Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo’s width and height must not exceed 10000 in total. Width and height ratio must be at most 20. [More information on Sending Files »](../upload_file.html#sending-files)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **caption** – Photo caption (may also be used when resending photos by *file_id*), 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **show_caption_above_media** – Pass `True` if the caption must be shown above the message media
            - **has_spoiler** – Pass `True` if the photo needs to be covered with a spoiler animation
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_photo.SendPhoto`](../methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto")

    reply_poll(*question: str, options: list[InputPollOptionUnion], question_parse_mode: str | Default | None = <Default('parse_mode')>, question_entities: list[MessageEntity] | None = None, is_anonymous: bool | None = None, type: str | None = None, allows_multiple_answers: bool | None = None, allows_revoting: bool | None = None, shuffle_options: bool | None = None, allow_adding_options: bool | None = None, hide_results_until_closes: bool | None = None, members_only: bool | None = None, country_codes: list[str] | None = None, correct_option_ids: list[int] | None = None, explanation: str | None = None, explanation_parse_mode: str | Default | None = <Default('parse_mode')>, explanation_entities: list[MessageEntity] | None = None, explanation_media: InputPollMediaUnion | None = None, open_period: int | None = None, close_date: DateTimeUnion | None = None, is_closed: bool | None = None, description: str | None = None, description_parse_mode: str | Default | None = <Default('parse_mode')>, description_entities: list[MessageEntity] | None = None, media: InputPollMediaUnion | None = None, disable_notification: bool | None = None, protect_content: bool | Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_markup: ReplyMarkupUnion | None = None, allow_sending_without_reply: bool | None = None, correct_option_id: int | None = None, \*\*kwargs: Any*) → [SendPoll](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll")
    :   Shortcut for method [`aiogram.methods.send_poll.SendPoll`](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send a native poll. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendpoll>

        Parameters:
        :   - **question** – Poll question, 1-300 characters
            - **options** – A JSON-serialized list of 1-12 answer options
            - **question_parse_mode** –

              Mode for parsing entities in the question. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. Currently, only custom emoji entities are allowed
            - **question_entities** – A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of *question_parse_mode*
            - **is_anonymous** – `True`, if the poll needs to be anonymous, defaults to `True`
            - **type** – Poll type, ‘quiz’ or ‘regular’, defaults to ‘regular’
            - **allows_multiple_answers** – Pass `True` if the poll allows multiple answers, defaults to `False`
            - **allows_revoting** – Pass `True` if the poll allows to change chosen answer options, defaults to `False` for quizzes and to `True` for regular polls
            - **shuffle_options** – Pass `True` if the poll options must be shown in random order
            - **allow_adding_options** – Pass `True` if answer options can be added to the poll after creation; not supported for anonymous polls and quizzes
            - **hide_results_until_closes** – Pass `True` if poll results must be shown only after the poll closes
            - **members_only** – Pass `True` if voting is limited to users who have been members of the chat where the poll is being sent for more than 24 hours; for channel chats only
            - **country_codes** – A JSON-serialized list of 0-12 two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes indicating the countries from which users can vote in the poll; for channel chats only. Use ‘FT’ as a country code to allow users with anonymous numbers to vote. If omitted or empty, then users from any country can participate in the poll
            - **correct_option_ids** – A JSON-serialized list of monotonically increasing 0-based identifiers of the correct answer options, required for polls in quiz mode
            - **explanation** – Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing
            - **explanation_parse_mode** –

              Mode for parsing entities in the explanation. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **explanation_entities** – A JSON-serialized list of special entities that appear in the poll explanation. It can be specified instead of *explanation_parse_mode*
            - **explanation_media** – Media added to the quiz explanation
            - **open_period** – Amount of time in seconds the poll will be active after creation, 5-2628000. Can’t be used together with *close_date*
            - **close_date** – Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 2628000 seconds in the future. Can’t be used together with *open_period*
            - **is_closed** – Pass `True` if the poll needs to be immediately closed. This can be useful for poll preview
            - **description** – Description of the poll to be sent, 0-1024 characters after entities parsing
            - **description_parse_mode** –

              Mode for parsing entities in the poll description. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **description_entities** – A JSON-serialized list of special entities that appear in the poll description, which can be specified instead of *description_parse_mode*
            - **media** – Media added to the poll description
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **correct_option_id** – 0-based identifier of the correct answer option, required for polls in quiz mode

        Returns:
        :   instance of method [`aiogram.methods.send_poll.SendPoll`](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll")

    answer_poll(*question: str, options: list[InputPollOptionUnion], question_parse_mode: str | Default | None = <Default('parse_mode')>, question_entities: list[MessageEntity] | None = None, is_anonymous: bool | None = None, type: str | None = None, allows_multiple_answers: bool | None = None, allows_revoting: bool | None = None, shuffle_options: bool | None = None, allow_adding_options: bool | None = None, hide_results_until_closes: bool | None = None, members_only: bool | None = None, country_codes: list[str] | None = None, correct_option_ids: list[int] | None = None, explanation: str | None = None, explanation_parse_mode: str | Default | None = <Default('parse_mode')>, explanation_entities: list[MessageEntity] | None = None, explanation_media: InputPollMediaUnion | None = None, open_period: int | None = None, close_date: DateTimeUnion | None = None, is_closed: bool | None = None, description: str | None = None, description_parse_mode: str | Default | None = <Default('parse_mode')>, description_entities: list[MessageEntity] | None = None, media: InputPollMediaUnion | None = None, disable_notification: bool | None = None, protect_content: bool | Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyMarkupUnion | None = None, allow_sending_without_reply: bool | None = None, correct_option_id: int | None = None, reply_to_message_id: int | None = None, \*\*kwargs: Any*) → [SendPoll](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll")
    :   Shortcut for method [`aiogram.methods.send_poll.SendPoll`](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send a native poll. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendpoll>

        Parameters:
        :   - **question** – Poll question, 1-300 characters
            - **options** – A JSON-serialized list of 1-12 answer options
            - **question_parse_mode** –

              Mode for parsing entities in the question. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. Currently, only custom emoji entities are allowed
            - **question_entities** – A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of *question_parse_mode*
            - **is_anonymous** – `True`, if the poll needs to be anonymous, defaults to `True`
            - **type** – Poll type, ‘quiz’ or ‘regular’, defaults to ‘regular’
            - **allows_multiple_answers** – Pass `True` if the poll allows multiple answers, defaults to `False`
            - **allows_revoting** – Pass `True` if the poll allows to change chosen answer options, defaults to `False` for quizzes and to `True` for regular polls
            - **shuffle_options** – Pass `True` if the poll options must be shown in random order
            - **allow_adding_options** – Pass `True` if answer options can be added to the poll after creation; not supported for anonymous polls and quizzes
            - **hide_results_until_closes** – Pass `True` if poll results must be shown only after the poll closes
            - **members_only** – Pass `True` if voting is limited to users who have been members of the chat where the poll is being sent for more than 24 hours; for channel chats only
            - **country_codes** –

              A JSON-serialized list of 0-12 two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes indicating the countries from which users can vote in the poll; for channel chats only. Use ‘FT’ as a country code to allow users with anonymous numbers to vote. If omitted or empty, then users from any country can participate in the poll
            - **correct_option_ids** – A JSON-serialized list of monotonically increasing 0-based identifiers of the correct answer options, required for polls in quiz mode
            - **explanation** – Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing
            - **explanation_parse_mode** –

              Mode for parsing entities in the explanation. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **explanation_entities** – A JSON-serialized list of special entities that appear in the poll explanation. It can be specified instead of *explanation_parse_mode*
            - **explanation_media** – Media added to the quiz explanation
            - **open_period** – Amount of time in seconds the poll will be active after creation, 5-2628000. Can’t be used together with *close_date*
            - **close_date** – Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 2628000 seconds in the future. Can’t be used together with *open_period*
            - **is_closed** – Pass `True` if the poll needs to be immediately closed. This can be useful for poll preview
            - **description** – Description of the poll to be sent, 0-1024 characters after entities parsing
            - **description_parse_mode** –

              Mode for parsing entities in the poll description. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **description_entities** – A JSON-serialized list of special entities that appear in the poll description, which can be specified instead of *description_parse_mode*
            - **media** – Media added to the poll description
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **correct_option_id** – 0-based identifier of the correct answer option, required for polls in quiz mode
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_poll.SendPoll`](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll")

    reply_dice(*direct_messages_topic_id: int | None = None*, *emoji: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendDice](../methods/send_dice.html#aiogram.methods.send_dice.SendDice "aiogram.methods.send_dice.SendDice")
    :   Shortcut for method [`aiogram.methods.send_dice.SendDice`](../methods/send_dice.html#aiogram.methods.send_dice.SendDice "aiogram.methods.send_dice.SendDice")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send an animated emoji that will display a random value. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#senddice>

        Parameters:
        :   - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **emoji** – Emoji on which the dice throw animation is based. Currently, must be one of ‘🎲’, ‘🎯’, ‘🏀’, ‘⚽’, ‘🎳’, or ‘🎰’. Dice can have values 1-6 for ‘🎲’, ‘🎯’ and ‘🎳’, values 1-5 for ‘🏀’ and ‘⚽’, and values 1-64 for ‘🎰’. Defaults to ‘🎲’
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_dice.SendDice`](../methods/send_dice.html#aiogram.methods.send_dice.SendDice "aiogram.methods.send_dice.SendDice")

    answer_dice(*direct_messages_topic_id: int | None = None*, *emoji: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendDice](../methods/send_dice.html#aiogram.methods.send_dice.SendDice "aiogram.methods.send_dice.SendDice")
    :   Shortcut for method [`aiogram.methods.send_dice.SendDice`](../methods/send_dice.html#aiogram.methods.send_dice.SendDice "aiogram.methods.send_dice.SendDice")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send an animated emoji that will display a random value. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#senddice>

        Parameters:
        :   - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **emoji** – Emoji on which the dice throw animation is based. Currently, must be one of ‘🎲’, ‘🎯’, ‘🏀’, ‘⚽’, ‘🎳’, or ‘🎰’. Dice can have values 1-6 for ‘🎲’, ‘🎯’ and ‘🎳’, values 1-5 for ‘🏀’ and ‘⚽’, and values 1-64 for ‘🎰’. Defaults to ‘🎲’
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_dice.SendDice`](../methods/send_dice.html#aiogram.methods.send_dice.SendDice "aiogram.methods.send_dice.SendDice")

    reply_sticker(*sticker: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *emoji: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendSticker](../methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker")
    :   Shortcut for method [`aiogram.methods.send_sticker.SendSticker`](../methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send static .WEBP, [animated](https://telegram.org/blog/animated-stickers) .TGS, or [video](https://telegram.org/blog/video-stickers-better-reactions) .WEBM stickers. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendsticker>

        Parameters:
        :   - **sticker** – Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP sticker from the Internet, or upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files). Video and animated stickers can’t be sent via an HTTP URL
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **emoji** – Emoji associated with the sticker; only for just uploaded stickers
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_sticker.SendSticker`](../methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker")

    answer_sticker(*sticker: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *emoji: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendSticker](../methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker")
    :   Shortcut for method [`aiogram.methods.send_sticker.SendSticker`](../methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send static .WEBP, [animated](https://telegram.org/blog/animated-stickers) .TGS, or [video](https://telegram.org/blog/video-stickers-better-reactions) .WEBM stickers. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendsticker>

        Parameters:
        :   - **sticker** – Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP sticker from the Internet, or upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files). Video and animated stickers can’t be sent via an HTTP URL
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **emoji** – Emoji associated with the sticker; only for just uploaded stickers
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_sticker.SendSticker`](../methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker")

    reply_venue(*latitude: float*, *longitude: float*, *title: str*, *address: str*, *direct_messages_topic_id: int | None = None*, *foursquare_id: str | None = None*, *foursquare_type: str | None = None*, *google_place_id: str | None = None*, *google_place_type: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendVenue](../methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue")
    :   Shortcut for method [`aiogram.methods.send_venue.SendVenue`](../methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send information about a venue. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendvenue>

        Parameters:
        :   - **latitude** – Latitude of the venue
            - **longitude** – Longitude of the venue
            - **title** – Name of the venue
            - **address** – Address of the venue
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **foursquare_id** – Foursquare identifier of the venue
            - **foursquare_type** – Foursquare type of the venue, if known. (For example, ‘arts_entertainment/default’, ‘arts_entertainment/aquarium’ or ‘food/icecream’.)
            - **google_place_id** – Google Places identifier of the venue
            - **google_place_type** – Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_venue.SendVenue`](../methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue")

    answer_venue(*latitude: float*, *longitude: float*, *title: str*, *address: str*, *direct_messages_topic_id: int | None = None*, *foursquare_id: str | None = None*, *foursquare_type: str | None = None*, *google_place_id: str | None = None*, *google_place_type: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendVenue](../methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue")
    :   Shortcut for method [`aiogram.methods.send_venue.SendVenue`](../methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send information about a venue. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendvenue>

        Parameters:
        :   - **latitude** – Latitude of the venue
            - **longitude** – Longitude of the venue
            - **title** – Name of the venue
            - **address** – Address of the venue
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **foursquare_id** – Foursquare identifier of the venue
            - **foursquare_type** – Foursquare type of the venue, if known. (For example, ‘arts_entertainment/default’, ‘arts_entertainment/aquarium’ or ‘food/icecream’.)
            - **google_place_id** – Google Places identifier of the venue
            - **google_place_type** –

              Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_venue.SendVenue`](../methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue")

    reply_video(*video: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *duration: int | None = None*, *width: int | None = None*, *height: int | None = None*, *thumbnail: InputFile | None = None*, *cover: InputFileUnion | None = None*, *start_timestamp: DateTimeUnion | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *supports_streaming: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendVideo](../methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo")
    :   Shortcut for method [`aiogram.methods.send_video.SendVideo`](../methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as [`aiogram.types.document.Document`](document.html#aiogram.types.document.Document "aiogram.types.document.Document")). On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#sendvideo>

        Parameters:
        :   - **video** – Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **duration** – Duration of sent video in seconds
            - **width** – Video width
            - **height** – Video height
            - **thumbnail** – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)
            - **cover** – Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files)
            - **start_timestamp** – Start timestamp for the video in the message
            - **caption** – Video caption (may also be used when resending videos by *file_id*), 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **show_caption_above_media** – Pass `True` if the caption must be shown above the message media
            - **has_spoiler** – Pass `True` if the video needs to be covered with a spoiler animation
            - **supports_streaming** – Pass `True` if the uploaded video is suitable for streaming
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_video.SendVideo`](../methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo")

    answer_video(*video: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *duration: int | None = None*, *width: int | None = None*, *height: int | None = None*, *thumbnail: InputFile | None = None*, *cover: InputFileUnion | None = None*, *start_timestamp: DateTimeUnion | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *supports_streaming: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendVideo](../methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo")
    :   Shortcut for method [`aiogram.methods.send_video.SendVideo`](../methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as [`aiogram.types.document.Document`](document.html#aiogram.types.document.Document "aiogram.types.document.Document")). On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#sendvideo>

        Parameters:
        :   - **video** – Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **duration** – Duration of sent video in seconds
            - **width** – Video width
            - **height** – Video height
            - **thumbnail** – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)
            - **cover** – Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass ‘attach://<file_attach_name>’ to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](../upload_file.html#sending-files)
            - **start_timestamp** – Start timestamp for the video in the message
            - **caption** – Video caption (may also be used when resending videos by *file_id*), 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **show_caption_above_media** – Pass `True` if the caption must be shown above the message media
            - **has_spoiler** – Pass `True` if the video needs to be covered with a spoiler animation
            - **supports_streaming** – Pass `True` if the uploaded video is suitable for streaming
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_video.SendVideo`](../methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo")

    reply_video_note(*video_note: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *duration: int | None = None*, *length: int | None = None*, *thumbnail: InputFile | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendVideoNote](../methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote")
    :   Shortcut for method [`aiogram.methods.send_video_note.SendVideoNote`](../methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        As of [v.4.0](https://telegram.org/blog/video-messages-and-telescope), Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendvideonote>

        Parameters:
        :   - **video_note** – Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files). Sending video notes by a URL is currently unsupported
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **duration** – Duration of sent video in seconds
            - **length** – Video width and height, i.e. diameter of the video message
            - **thumbnail** – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_video_note.SendVideoNote`](../methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote")

    answer_video_note(*video_note: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *duration: int | None = None*, *length: int | None = None*, *thumbnail: InputFile | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendVideoNote](../methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote")
    :   Shortcut for method [`aiogram.methods.send_video_note.SendVideoNote`](../methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        As of [v.4.0](https://telegram.org/blog/video-messages-and-telescope), Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendvideonote>

        Parameters:
        :   - **video_note** – Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files). Sending video notes by a URL is currently unsupported
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **duration** – Duration of sent video in seconds
            - **length** – Video width and height, i.e. diameter of the video message
            - **thumbnail** – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass ‘attach://<file_attach_name>’ if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](../upload_file.html#sending-files)
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_video_note.SendVideoNote`](../methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote")

    reply_voice(*voice: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *duration: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendVoice](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice")
    :   Shortcut for method [`aiogram.methods.send_voice.SendVoice`](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS, or in .MP3 format, or in .M4A format (other formats may be sent as [`aiogram.types.audio.Audio`](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio") or [`aiogram.types.document.Document`](document.html#aiogram.types.document.Document "aiogram.types.document.Document")). On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#sendvoice>

        Parameters:
        :   - **voice** – Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **caption** – Voice message caption, 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the voice message caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **duration** – Duration of the voice message in seconds
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_voice.SendVoice`](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice")

    answer_voice(*voice: InputFileUnion*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *duration: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendVoice](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice")
    :   Shortcut for method [`aiogram.methods.send_voice.SendVoice`](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS, or in .MP3 format, or in .M4A format (other formats may be sent as [`aiogram.types.audio.Audio`](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio") or [`aiogram.types.document.Document`](document.html#aiogram.types.document.Document "aiogram.types.document.Document")). On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#sendvoice>

        Parameters:
        :   - **voice** – Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **caption** – Voice message caption, 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the voice message caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **duration** – Duration of the voice message in seconds
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_voice.SendVoice`](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice")

    send_copy(*chat_id: ChatIdUnion*, *disable_notification: bool | None = None*, *reply_to_message_id: int | None = None*, *reply_parameters: [ReplyParameters](reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None = None*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | [ReplyKeyboardMarkup](reply_keyboard_markup.html#aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup "aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup") | None = None*, *allow_sending_without_reply: bool | None = None*, *message_thread_id: int | None = None*, *business_connection_id: str | None = None*, *parse_mode: str | None = None*, *message_effect_id: str | None = None*, *link_preview_options: [LinkPreviewOptions](link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | None = None*) → [ForwardMessage](../methods/forward_message.html#aiogram.methods.forward_message.ForwardMessage "aiogram.methods.forward_message.ForwardMessage") | [SendAnimation](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation") | [SendAudio](../methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio") | [SendContact](../methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact") | [SendDocument](../methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument") | [SendLocation](../methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation") | [SendMessage](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage") | [SendPhoto](../methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto") | [SendPoll](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll") | [SendDice](../methods/send_dice.html#aiogram.methods.send_dice.SendDice "aiogram.methods.send_dice.SendDice") | [SendSticker](../methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker") | [SendVenue](../methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue") | [SendVideo](../methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo") | [SendVideoNote](../methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote") | [SendVoice](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice")
    :   Send copy of a message.

        Is similar to `aiogram.client.bot.Bot.copy_message()`
        but returning the sent message instead of [`aiogram.types.message_id.MessageId`](message_id.html#aiogram.types.message_id.MessageId "aiogram.types.message_id.MessageId")

        Note

        This method doesn’t use the API method named copyMessage and
        historically implemented before the similar method is added to API

        Parameters:
        :   - **chat_id**
            - **disable_notification**
            - **reply_to_message_id**
            - **reply_parameters**
            - **reply_markup**
            - **allow_sending_without_reply**
            - **message_thread_id**
            - **business_connection_id**
            - **parse_mode**
            - **message_effect_id**
            - **link_preview_options** – Link preview generation options for the copied message.
              Only applied when the source message is a text message; falls back to
              the original message’s `link_preview_options` when not provided.

        Returns:

    copy_to(*chat_id: ChatIdUnion*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *video_start_timestamp: DateTimeUnion | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [CopyMessage](../methods/copy_message.html#aiogram.methods.copy_message.CopyMessage "aiogram.methods.copy_message.CopyMessage")
    :   Shortcut for method [`aiogram.methods.copy_message.CopyMessage`](../methods/copy_message.html#aiogram.methods.copy_message.CopyMessage "aiogram.methods.copy_message.CopyMessage")
        will automatically fill method attributes:

        - `from_chat_id`
        - `message_id`

        Use this method to copy messages of any kind. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can’t be copied. A quiz `aiogram.methods.poll.Poll` can be copied only if the value of the field *correct_option_id* is known to the bot. The method is analogous to the method [`aiogram.methods.forward_message.ForwardMessage`](../methods/forward_message.html#aiogram.methods.forward_message.ForwardMessage "aiogram.methods.forward_message.ForwardMessage"), but the copied message doesn’t have a link to the original message. Returns the [`aiogram.types.message_id.MessageId`](message_id.html#aiogram.types.message_id.MessageId "aiogram.types.message_id.MessageId") of the sent message on success.

        Source: <https://core.telegram.org/bots/api#copymessage>

        Parameters:
        :   - **chat_id** – Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **video_start_timestamp** – New start timestamp for the copied video in the message
            - **caption** – New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept
            - **parse_mode** –

              Mode for parsing entities in the new caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of *parse_mode*
            - **show_caption_above_media** – Pass `True` if the caption must be shown above the message media. Ignored if a new caption isn’t specified
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; only available when copying to private chats
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.copy_message.CopyMessage`](../methods/copy_message.html#aiogram.methods.copy_message.CopyMessage "aiogram.methods.copy_message.CopyMessage")

    edit_text(*text: str | None = None*, *inline_message_id: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *entities: list[MessageEntity] | None = None*, *link_preview_options: LinkPreviewOptions | Default | None = <Default('link_preview')>*, *reply_markup: InlineKeyboardMarkup | None = None*, *rich_message: InputRichMessage | None = None*, *disable_web_page_preview: bool | Default | None = <Default('link_preview_is_disabled')>*, *\*\*kwargs: Any*) → [EditMessageText](../methods/edit_message_text.html#aiogram.methods.edit_message_text.EditMessageText "aiogram.methods.edit_message_text.EditMessageText")
    :   Shortcut for method [`aiogram.methods.edit_message_text.EditMessageText`](../methods/edit_message_text.html#aiogram.methods.edit_message_text.EditMessageText "aiogram.methods.edit_message_text.EditMessageText")
        will automatically fill method attributes:

        - `chat_id`
        - `message_id`
        - `business_connection_id`

        Use this method to edit text, rich and [game](https://core.telegram.org/bots/api#games) messages. On success, if the edited message is not an inline message, the edited [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

        Source: <https://core.telegram.org/bots/api#editmessagetext>

        Parameters:
        :   - **text** – New text of the message, 1-4096 characters after entity parsing; required if *rich_message* isn’t specified
            - **inline_message_id** – Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
            - **parse_mode** –

              Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **entities** – A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*
            - **link_preview_options** – Link preview generation options for the message
            - **reply_markup** –

              A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)
            - **rich_message** – New rich content of the message; required if *text* isn’t specified. Direct upload of new files isn’t supported when an inline message is edited
            - **disable_web_page_preview** – Disables link previews for links in this message

        Returns:
        :   instance of method [`aiogram.methods.edit_message_text.EditMessageText`](../methods/edit_message_text.html#aiogram.methods.edit_message_text.EditMessageText "aiogram.methods.edit_message_text.EditMessageText")

    forward(*chat_id: ChatIdUnion*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *video_start_timestamp: DateTimeUnion | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *\*\*kwargs: Any*) → [ForwardMessage](../methods/forward_message.html#aiogram.methods.forward_message.ForwardMessage "aiogram.methods.forward_message.ForwardMessage")
    :   Shortcut for method [`aiogram.methods.forward_message.ForwardMessage`](../methods/forward_message.html#aiogram.methods.forward_message.ForwardMessage "aiogram.methods.forward_message.ForwardMessage")
        will automatically fill method attributes:

        - `from_chat_id`
        - `message_id`

        Use this method to forward messages of any kind. Service messages and messages with protected content can’t be forwarded. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#forwardmessage>

        Parameters:
        :   - **chat_id** – Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be forwarded; required if the message is forwarded to a direct messages chat
            - **video_start_timestamp** – New start timestamp for the forwarded video in the message
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the forwarded message from forwarding and saving
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; only available when forwarding to private chats
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only

        Returns:
        :   instance of method [`aiogram.methods.forward_message.ForwardMessage`](../methods/forward_message.html#aiogram.methods.forward_message.ForwardMessage "aiogram.methods.forward_message.ForwardMessage")

    edit_media(*media: InputMediaUnion*, *inline_message_id: str | None = None*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*kwargs: Any*) → [EditMessageMedia](../methods/edit_message_media.html#aiogram.methods.edit_message_media.EditMessageMedia "aiogram.methods.edit_message_media.EditMessageMedia")
    :   Shortcut for method [`aiogram.methods.edit_message_media.EditMessageMedia`](../methods/edit_message_media.html#aiogram.methods.edit_message_media.EditMessageMedia "aiogram.methods.edit_message_media.EditMessageMedia")
        will automatically fill method attributes:

        - `chat_id`
        - `message_id`
        - `business_connection_id`

        Use this method to edit animation, audio, document, live photo, photo, or video messages, or to replace a text or a rich message with a media. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo, a live photo, or a video otherwise. When an inline message is edited, a new file can’t be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

        Source: <https://core.telegram.org/bots/api#editmessagemedia>

        Parameters:
        :   - **media** – A JSON-serialized object for the new media content of the message
            - **inline_message_id** – Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
            - **reply_markup** –

              A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

        Returns:
        :   instance of method [`aiogram.methods.edit_message_media.EditMessageMedia`](../methods/edit_message_media.html#aiogram.methods.edit_message_media.EditMessageMedia "aiogram.methods.edit_message_media.EditMessageMedia")

    edit_reply_markup(*inline_message_id: str | None = None*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*kwargs: Any*) → [EditMessageReplyMarkup](../methods/edit_message_reply_markup.html#aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup "aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup")
    :   Shortcut for method [`aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup`](../methods/edit_message_reply_markup.html#aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup "aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup")
        will automatically fill method attributes:

        - `chat_id`
        - `message_id`
        - `business_connection_id`

        Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

        Source: <https://core.telegram.org/bots/api#editmessagereplymarkup>

        Parameters:
        :   - **inline_message_id** – Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
            - **reply_markup** –

              A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

        Returns:
        :   instance of method [`aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup`](../methods/edit_message_reply_markup.html#aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup "aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup")

    delete_reply_markup(*inline_message_id: str | None = None*, *\*\*kwargs: Any*) → [EditMessageReplyMarkup](../methods/edit_message_reply_markup.html#aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup "aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup")
    :   Shortcut for method [`aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup`](../methods/edit_message_reply_markup.html#aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup "aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup")
        will automatically fill method attributes:

        - `chat_id`
        - `message_id`
        - `business_connection_id`
        - `reply_markup`

        Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

        Source: <https://core.telegram.org/bots/api#editmessagereplymarkup>

        Parameters:
        :   **inline_message_id** – Required if *chat_id* and *message_id* are not specified. Identifier of the inline message

        Returns:
        :   instance of method [`aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup`](../methods/edit_message_reply_markup.html#aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup "aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup")

    edit_live_location(*latitude: float*, *longitude: float*, *inline_message_id: str | None = None*, *live_period: int | None = None*, *horizontal_accuracy: float | None = None*, *heading: int | None = None*, *proximity_alert_radius: int | None = None*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*kwargs: Any*) → [EditMessageLiveLocation](../methods/edit_message_live_location.html#aiogram.methods.edit_message_live_location.EditMessageLiveLocation "aiogram.methods.edit_message_live_location.EditMessageLiveLocation")
    :   Shortcut for method [`aiogram.methods.edit_message_live_location.EditMessageLiveLocation`](../methods/edit_message_live_location.html#aiogram.methods.edit_message_live_location.EditMessageLiveLocation "aiogram.methods.edit_message_live_location.EditMessageLiveLocation")
        will automatically fill method attributes:

        - `chat_id`
        - `message_id`
        - `business_connection_id`

        Use this method to edit live location messages. A location can be edited until its *live_period* expires or editing is explicitly disabled by a call to [`aiogram.methods.stop_message_live_location.StopMessageLiveLocation`](../methods/stop_message_live_location.html#aiogram.methods.stop_message_live_location.StopMessageLiveLocation "aiogram.methods.stop_message_live_location.StopMessageLiveLocation"). On success, if the edited message is not an inline message, the edited [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned.

        Source: <https://core.telegram.org/bots/api#editmessagelivelocation>

        Parameters:
        :   - **latitude** – Latitude of new location
            - **longitude** – Longitude of new location
            - **inline_message_id** – Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
            - **live_period** – New period in seconds during which the location can be updated, starting from the message send date. If 0x7FFFFFFF is specified, then the location can be updated forever. Otherwise, the new value must not exceed the current *live_period* by more than a day, and the live location expiration date must remain within the next 90 days. If not specified, then *live_period* remains unchanged
            - **horizontal_accuracy** – The radius of uncertainty for the location, measured in meters; 0-1500
            - **heading** – Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified
            - **proximity_alert_radius** – The maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified
            - **reply_markup** –

              A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

        Returns:
        :   instance of method [`aiogram.methods.edit_message_live_location.EditMessageLiveLocation`](../methods/edit_message_live_location.html#aiogram.methods.edit_message_live_location.EditMessageLiveLocation "aiogram.methods.edit_message_live_location.EditMessageLiveLocation")

    stop_live_location(*inline_message_id: str | None = None*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*kwargs: Any*) → [StopMessageLiveLocation](../methods/stop_message_live_location.html#aiogram.methods.stop_message_live_location.StopMessageLiveLocation "aiogram.methods.stop_message_live_location.StopMessageLiveLocation")
    :   Shortcut for method [`aiogram.methods.stop_message_live_location.StopMessageLiveLocation`](../methods/stop_message_live_location.html#aiogram.methods.stop_message_live_location.StopMessageLiveLocation "aiogram.methods.stop_message_live_location.StopMessageLiveLocation")
        will automatically fill method attributes:

        - `chat_id`
        - `message_id`
        - `business_connection_id`

        Use this method to stop updating a live location message before *live_period* expires. On success, if the message is not an inline message, the edited [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned.

        Source: <https://core.telegram.org/bots/api#stopmessagelivelocation>

        Parameters:
        :   - **inline_message_id** – Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
            - **reply_markup** –

              A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

        Returns:
        :   instance of method [`aiogram.methods.stop_message_live_location.StopMessageLiveLocation`](../methods/stop_message_live_location.html#aiogram.methods.stop_message_live_location.StopMessageLiveLocation "aiogram.methods.stop_message_live_location.StopMessageLiveLocation")

    edit_caption(*inline_message_id: str | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *reply_markup: InlineKeyboardMarkup | None = None*, *\*\*kwargs: Any*) → [EditMessageCaption](../methods/edit_message_caption.html#aiogram.methods.edit_message_caption.EditMessageCaption "aiogram.methods.edit_message_caption.EditMessageCaption")
    :   Shortcut for method [`aiogram.methods.edit_message_caption.EditMessageCaption`](../methods/edit_message_caption.html#aiogram.methods.edit_message_caption.EditMessageCaption "aiogram.methods.edit_message_caption.EditMessageCaption")
        will automatically fill method attributes:

        - `chat_id`
        - `message_id`
        - `business_connection_id`

        Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

        Source: <https://core.telegram.org/bots/api#editmessagecaption>

        Parameters:
        :   - **inline_message_id** – Required if *chat_id* and *message_id* are not specified. Identifier of the inline message
            - **caption** – New caption of the message, 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the message caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **show_caption_above_media** – Pass `True` if the caption must be shown above the message media. Supported only for animation, photo and video messages
            - **reply_markup** –

              A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

        Returns:
        :   instance of method [`aiogram.methods.edit_message_caption.EditMessageCaption`](../methods/edit_message_caption.html#aiogram.methods.edit_message_caption.EditMessageCaption "aiogram.methods.edit_message_caption.EditMessageCaption")

    delete(*\*\*kwargs: Any*) → [DeleteMessage](../methods/delete_message.html#aiogram.methods.delete_message.DeleteMessage "aiogram.methods.delete_message.DeleteMessage")
    :   Shortcut for method [`aiogram.methods.delete_message.DeleteMessage`](../methods/delete_message.html#aiogram.methods.delete_message.DeleteMessage "aiogram.methods.delete_message.DeleteMessage")
        will automatically fill method attributes:

        - `chat_id`
        - `message_id`
        - `business_connection_id`

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

        Returns:
        :   instance of method [`aiogram.methods.delete_message.DeleteMessage`](../methods/delete_message.html#aiogram.methods.delete_message.DeleteMessage "aiogram.methods.delete_message.DeleteMessage")

    edit_ephemeral_text(*text: str*, *parse_mode: str | None = None*, *entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *link_preview_options: [LinkPreviewOptions](link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | None = None*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*kwargs: Any*) → [EditEphemeralMessageText](../methods/edit_ephemeral_message_text.html#aiogram.methods.edit_ephemeral_message_text.EditEphemeralMessageText "aiogram.methods.edit_ephemeral_message_text.EditEphemeralMessageText")
    :   Shortcut for method [`aiogram.methods.edit_ephemeral_message_text.EditEphemeralMessageText`](../methods/edit_ephemeral_message_text.html#aiogram.methods.edit_ephemeral_message_text.EditEphemeralMessageText "aiogram.methods.edit_ephemeral_message_text.EditEphemeralMessageText")
        will automatically fill method attributes:

        - `chat_id`
        - `receiver_user_id`
        - `ephemeral_message_id`

        Use this method to edit an ephemeral text message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, `True` is returned.

        Source: <https://core.telegram.org/bots/api#editephemeralmessagetext>

        Parameters:
        :   - **text** – New text of the message, 1-4096 characters after entity parsing
            - **parse_mode** –

              Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **entities** – A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*
            - **link_preview_options** – Link preview generation options for the message
            - **reply_markup** –

              A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

        Returns:
        :   instance of method [`aiogram.methods.edit_ephemeral_message_text.EditEphemeralMessageText`](../methods/edit_ephemeral_message_text.html#aiogram.methods.edit_ephemeral_message_text.EditEphemeralMessageText "aiogram.methods.edit_ephemeral_message_text.EditEphemeralMessageText")

    edit_ephemeral_caption(*caption: str | None = None*, *parse_mode: str | None = None*, *caption_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*kwargs: Any*) → [EditEphemeralMessageCaption](../methods/edit_ephemeral_message_caption.html#aiogram.methods.edit_ephemeral_message_caption.EditEphemeralMessageCaption "aiogram.methods.edit_ephemeral_message_caption.EditEphemeralMessageCaption")
    :   Shortcut for method [`aiogram.methods.edit_ephemeral_message_caption.EditEphemeralMessageCaption`](../methods/edit_ephemeral_message_caption.html#aiogram.methods.edit_ephemeral_message_caption.EditEphemeralMessageCaption "aiogram.methods.edit_ephemeral_message_caption.EditEphemeralMessageCaption")
        will automatically fill method attributes:

        - `chat_id`
        - `receiver_user_id`
        - `ephemeral_message_id`

        Use this method to edit the caption of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, `True` is returned.

        Source: <https://core.telegram.org/bots/api#editephemeralmessagecaption>

        Parameters:
        :   - **caption** – New caption of the message, 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the message caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **reply_markup** –

              A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

        Returns:
        :   instance of method [`aiogram.methods.edit_ephemeral_message_caption.EditEphemeralMessageCaption`](../methods/edit_ephemeral_message_caption.html#aiogram.methods.edit_ephemeral_message_caption.EditEphemeralMessageCaption "aiogram.methods.edit_ephemeral_message_caption.EditEphemeralMessageCaption")

    edit_ephemeral_media(*media: InputMediaUnion*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*kwargs: Any*) → [EditEphemeralMessageMedia](../methods/edit_ephemeral_message_media.html#aiogram.methods.edit_ephemeral_message_media.EditEphemeralMessageMedia "aiogram.methods.edit_ephemeral_message_media.EditEphemeralMessageMedia")
    :   Shortcut for method [`aiogram.methods.edit_ephemeral_message_media.EditEphemeralMessageMedia`](../methods/edit_ephemeral_message_media.html#aiogram.methods.edit_ephemeral_message_media.EditEphemeralMessageMedia "aiogram.methods.edit_ephemeral_message_media.EditEphemeralMessageMedia")
        will automatically fill method attributes:

        - `chat_id`
        - `receiver_user_id`
        - `ephemeral_message_id`

        Use this method to edit the media of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, `True` is returned.

        Source: <https://core.telegram.org/bots/api#editephemeralmessagemedia>

        Parameters:
        :   - **media** – A JSON-serialized object for the new media content of the message. A new file can’t be uploaded; use a previously uploaded file via its file_id or specify a URL
            - **reply_markup** –

              A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

        Returns:
        :   instance of method [`aiogram.methods.edit_ephemeral_message_media.EditEphemeralMessageMedia`](../methods/edit_ephemeral_message_media.html#aiogram.methods.edit_ephemeral_message_media.EditEphemeralMessageMedia "aiogram.methods.edit_ephemeral_message_media.EditEphemeralMessageMedia")

    edit_ephemeral_reply_markup(*reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*kwargs: Any*) → [EditEphemeralMessageReplyMarkup](../methods/edit_ephemeral_message_reply_markup.html#aiogram.methods.edit_ephemeral_message_reply_markup.EditEphemeralMessageReplyMarkup "aiogram.methods.edit_ephemeral_message_reply_markup.EditEphemeralMessageReplyMarkup")
    :   Shortcut for method [`aiogram.methods.edit_ephemeral_message_reply_markup.EditEphemeralMessageReplyMarkup`](../methods/edit_ephemeral_message_reply_markup.html#aiogram.methods.edit_ephemeral_message_reply_markup.EditEphemeralMessageReplyMarkup "aiogram.methods.edit_ephemeral_message_reply_markup.EditEphemeralMessageReplyMarkup")
        will automatically fill method attributes:

        - `chat_id`
        - `receiver_user_id`
        - `ephemeral_message_id`

        Use this method to edit only the reply markup of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, `True` is returned.

        Source: <https://core.telegram.org/bots/api#editephemeralmessagereplymarkup>

        Parameters:
        :   **reply_markup** –

            A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards)

        Returns:
        :   instance of method [`aiogram.methods.edit_ephemeral_message_reply_markup.EditEphemeralMessageReplyMarkup`](../methods/edit_ephemeral_message_reply_markup.html#aiogram.methods.edit_ephemeral_message_reply_markup.EditEphemeralMessageReplyMarkup "aiogram.methods.edit_ephemeral_message_reply_markup.EditEphemeralMessageReplyMarkup")

    delete_ephemeral(*\*\*kwargs: Any*) → [DeleteEphemeralMessage](../methods/delete_ephemeral_message.html#aiogram.methods.delete_ephemeral_message.DeleteEphemeralMessage "aiogram.methods.delete_ephemeral_message.DeleteEphemeralMessage")
    :   Shortcut for method [`aiogram.methods.delete_ephemeral_message.DeleteEphemeralMessage`](../methods/delete_ephemeral_message.html#aiogram.methods.delete_ephemeral_message.DeleteEphemeralMessage "aiogram.methods.delete_ephemeral_message.DeleteEphemeralMessage")
        will automatically fill method attributes:

        - `chat_id`
        - `receiver_user_id`
        - `ephemeral_message_id`

        Use this method to delete an ephemeral message. Note that it is not guaranteed that the user will receive the message deletion event, especially if they are offline. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#deleteephemeralmessage>

        Returns:
        :   instance of method [`aiogram.methods.delete_ephemeral_message.DeleteEphemeralMessage`](../methods/delete_ephemeral_message.html#aiogram.methods.delete_ephemeral_message.DeleteEphemeralMessage "aiogram.methods.delete_ephemeral_message.DeleteEphemeralMessage")

    pin(*disable_notification: bool | None = None*, *\*\*kwargs: Any*) → [PinChatMessage](../methods/pin_chat_message.html#aiogram.methods.pin_chat_message.PinChatMessage "aiogram.methods.pin_chat_message.PinChatMessage")
    :   Shortcut for method [`aiogram.methods.pin_chat_message.PinChatMessage`](../methods/pin_chat_message.html#aiogram.methods.pin_chat_message.PinChatMessage "aiogram.methods.pin_chat_message.PinChatMessage")
        will automatically fill method attributes:

        - `chat_id`
        - `message_id`
        - `business_connection_id`

        Use this method to add a message to the list of pinned messages in a chat. In private chats and channel direct messages chats, all non-service messages can be pinned. Conversely, the bot must be an administrator with the ‘can_pin_messages’ right or the ‘can_edit_messages’ right to pin messages in groups and channels respectively. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#pinchatmessage>

        Parameters:
        :   **disable_notification** – Pass `True` if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats

        Returns:
        :   instance of method [`aiogram.methods.pin_chat_message.PinChatMessage`](../methods/pin_chat_message.html#aiogram.methods.pin_chat_message.PinChatMessage "aiogram.methods.pin_chat_message.PinChatMessage")

    unpin(*\*\*kwargs: Any*) → [UnpinChatMessage](../methods/unpin_chat_message.html#aiogram.methods.unpin_chat_message.UnpinChatMessage "aiogram.methods.unpin_chat_message.UnpinChatMessage")
    :   Shortcut for method [`aiogram.methods.unpin_chat_message.UnpinChatMessage`](../methods/unpin_chat_message.html#aiogram.methods.unpin_chat_message.UnpinChatMessage "aiogram.methods.unpin_chat_message.UnpinChatMessage")
        will automatically fill method attributes:

        - `chat_id`
        - `message_id`
        - `business_connection_id`

        Use this method to remove a message from the list of pinned messages in a chat. In private chats and channel direct messages chats, all messages can be unpinned. Conversely, the bot must be an administrator with the ‘can_pin_messages’ right or the ‘can_edit_messages’ right to unpin messages in groups and channels respectively. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#unpinchatmessage>

        Returns:
        :   instance of method [`aiogram.methods.unpin_chat_message.UnpinChatMessage`](../methods/unpin_chat_message.html#aiogram.methods.unpin_chat_message.UnpinChatMessage "aiogram.methods.unpin_chat_message.UnpinChatMessage")

    get_url(*force_private: bool = False*, *include_thread_id: bool = False*) → str | None
    :   Returns message URL. Cannot be used in private (one-to-one) chats.
        If chat has a username, returns URL like <https://t.me/username/message_id>
        Otherwise (or if {force_private} flag is set), returns <https://t.me/c/shifted_chat_id/message_id>

        Parameters:
        :   - **force_private** – if set, a private URL is returned even for a public chat
            - **include_thread_id** – if set, adds chat thread id to URL and returns like <https://t.me/username/thread_id/message_id>

        Returns:
        :   string with full message URL

    react(*reaction: list[ReactionTypeUnion] | None = None*, *is_big: bool | None = None*, *\*\*kwargs: Any*) → [SetMessageReaction](../methods/set_message_reaction.html#aiogram.methods.set_message_reaction.SetMessageReaction "aiogram.methods.set_message_reaction.SetMessageReaction")
    :   Shortcut for method [`aiogram.methods.set_message_reaction.SetMessageReaction`](../methods/set_message_reaction.html#aiogram.methods.set_message_reaction.SetMessageReaction "aiogram.methods.set_message_reaction.SetMessageReaction")
        will automatically fill method attributes:

        - `chat_id`
        - `message_id`
        - `business_connection_id`

        Use this method to change the chosen reactions on a message. Service messages of some types can’t be reacted to. Automatically forwarded messages from a channel to its discussion group have the same available reactions as messages in the channel. Bots can’t use paid reactions. Returns `True` on success.

        Source: <https://core.telegram.org/bots/api#setmessagereaction>

        Parameters:
        :   - **reaction** – A JSON-serialized list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message. A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators. Paid reactions can’t be used by bots
            - **is_big** – Pass `True` to set the reaction with a big animation

        Returns:
        :   instance of method [`aiogram.methods.set_message_reaction.SetMessageReaction`](../methods/set_message_reaction.html#aiogram.methods.set_message_reaction.SetMessageReaction "aiogram.methods.set_message_reaction.SetMessageReaction")

    answer_paid_media(*star_count: int*, *media: list[InputPaidMediaUnion]*, *direct_messages_topic_id: int | None = None*, *payload: str | None = None*, *caption: str | None = None*, *parse_mode: str | None = None*, *caption_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *show_caption_above_media: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *allow_paid_broadcast: bool | None = None*, *suggested_post_parameters: [SuggestedPostParameters](suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None = None*, *reply_parameters: [ReplyParameters](reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *\*\*kwargs: Any*) → [SendPaidMedia](../methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia")
    :   Shortcut for method [`aiogram.methods.send_paid_media.SendPaidMedia`](../methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send paid media. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendpaidmedia>

        Parameters:
        :   - **star_count** – The number of Telegram Stars that must be paid to buy access to the media; 1-25000
            - **media** – A JSON-serialized Array describing the media to be sent; up to 10 items
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **payload** – Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes
            - **caption** – Media caption, 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the media caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **show_caption_above_media** – Pass `True` if the caption must be shown above the message media
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user

        Returns:
        :   instance of method [`aiogram.methods.send_paid_media.SendPaidMedia`](../methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia")

    reply_paid_media(*star_count: int*, *media: list[InputPaidMediaUnion]*, *direct_messages_topic_id: int | None = None*, *payload: str | None = None*, *caption: str | None = None*, *parse_mode: str | None = None*, *caption_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *show_caption_above_media: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *allow_paid_broadcast: bool | None = None*, *suggested_post_parameters: [SuggestedPostParameters](suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *\*\*kwargs: Any*) → [SendPaidMedia](../methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia")
    :   Shortcut for method [`aiogram.methods.send_paid_media.SendPaidMedia`](../methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send paid media. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendpaidmedia>

        Parameters:
        :   - **star_count** – The number of Telegram Stars that must be paid to buy access to the media; 1-25000
            - **media** – A JSON-serialized Array describing the media to be sent; up to 10 items
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **payload** – Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes
            - **caption** – Media caption, 0-1024 characters after entities parsing
            - **parse_mode** –

              Mode for parsing entities in the media caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **caption_entities** – A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode*
            - **show_caption_above_media** – Pass `True` if the caption must be shown above the message media
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user

        Returns:
        :   instance of method [`aiogram.methods.send_paid_media.SendPaidMedia`](../methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia")

    answer_guest_query(*result: InlineQueryResultUnion*, *\*\*kwargs: Any*) → [AnswerGuestQuery](../methods/answer_guest_query.html#aiogram.methods.answer_guest_query.AnswerGuestQuery "aiogram.methods.answer_guest_query.AnswerGuestQuery")
    :   Shortcut for method [`aiogram.methods.answer_guest_query.AnswerGuestQuery`](../methods/answer_guest_query.html#aiogram.methods.answer_guest_query.AnswerGuestQuery "aiogram.methods.answer_guest_query.AnswerGuestQuery")
        will automatically fill method attributes:

        - `guest_query_id`

        Use this method to reply to a received guest message. On success, a [`aiogram.types.sent_guest_message.SentGuestMessage`](sent_guest_message.html#aiogram.types.sent_guest_message.SentGuestMessage "aiogram.types.sent_guest_message.SentGuestMessage") object is returned.

        Source: <https://core.telegram.org/bots/api#answerguestquery>

        Parameters:
        :   **result** – A JSON-serialized object describing the message to be sent

        Returns:
        :   instance of method [`aiogram.methods.answer_guest_query.AnswerGuestQuery`](../methods/answer_guest_query.html#aiogram.methods.answer_guest_query.AnswerGuestQuery "aiogram.methods.answer_guest_query.AnswerGuestQuery")

    answer_rich(*rich_message: [InputRichMessage](input_rich_message.html#aiogram.types.input_rich_message.InputRichMessage "aiogram.types.input_rich_message.InputRichMessage")*, *direct_messages_topic_id: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: [SuggestedPostParameters](suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None = None*, *reply_parameters: [ReplyParameters](reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *\*\*kwargs: Any*) → [SendRichMessage](../methods/send_rich_message.html#aiogram.methods.send_rich_message.SendRichMessage "aiogram.methods.send_rich_message.SendRichMessage")
    :   Shortcut for method [`aiogram.methods.send_rich_message.SendRichMessage`](../methods/send_rich_message.html#aiogram.methods.send_rich_message.SendRichMessage "aiogram.methods.send_rich_message.SendRichMessage")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`

        Use this method to send rich messages. If the message contains a block with a media element, then the bot must have the right to send the media to the chat. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendrichmessage>

        Parameters:
        :   - **rich_message** – The message to be sent
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user

        Returns:
        :   instance of method [`aiogram.methods.send_rich_message.SendRichMessage`](../methods/send_rich_message.html#aiogram.methods.send_rich_message.SendRichMessage "aiogram.methods.send_rich_message.SendRichMessage")

    reply_rich(*rich_message: [InputRichMessage](input_rich_message.html#aiogram.types.input_rich_message.InputRichMessage "aiogram.types.input_rich_message.InputRichMessage")*, *direct_messages_topic_id: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: [SuggestedPostParameters](suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *\*\*kwargs: Any*) → [SendRichMessage](../methods/send_rich_message.html#aiogram.methods.send_rich_message.SendRichMessage "aiogram.methods.send_rich_message.SendRichMessage")
    :   Shortcut for method [`aiogram.methods.send_rich_message.SendRichMessage`](../methods/send_rich_message.html#aiogram.methods.send_rich_message.SendRichMessage "aiogram.methods.send_rich_message.SendRichMessage")
        will automatically fill method attributes:

        - `chat_id`
        - `message_thread_id`
        - `business_connection_id`
        - `reply_parameters`
        - `receiver_user_id`

        Use this method to send rich messages. If the message contains a block with a media element, then the bot must have the right to send the media to the chat. On success, the sent [`aiogram.types.message.Message`](#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendrichmessage>

        Parameters:
        :   - **rich_message** – The message to be sent
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **disable_notification** –

              Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** –

              Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user

        Returns:
        :   instance of method [`aiogram.methods.send_rich_message.SendRichMessage`](../methods/send_rich_message.html#aiogram.methods.send_rich_message.SendRichMessage "aiogram.methods.send_rich_message.SendRichMessage")
