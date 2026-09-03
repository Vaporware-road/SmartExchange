# Update

> Source: [https://docs.aiogram.dev/en/latest/api/types/update.html](https://docs.aiogram.dev/en/latest/api/types/update.html)

*class* aiogram.types.update.Update(*\**, *update_id: int*, *message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *edited_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *channel_post: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *edited_channel_post: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *business_connection: [BusinessConnection](business_connection.html#aiogram.types.business_connection.BusinessConnection "aiogram.types.business_connection.BusinessConnection") | None = None*, *business_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *edited_business_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *deleted_business_messages: [BusinessMessagesDeleted](business_messages_deleted.html#aiogram.types.business_messages_deleted.BusinessMessagesDeleted "aiogram.types.business_messages_deleted.BusinessMessagesDeleted") | None = None*, *guest_message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None = None*, *message_reaction: [MessageReactionUpdated](message_reaction_updated.html#aiogram.types.message_reaction_updated.MessageReactionUpdated "aiogram.types.message_reaction_updated.MessageReactionUpdated") | None = None*, *message_reaction_count: [MessageReactionCountUpdated](message_reaction_count_updated.html#aiogram.types.message_reaction_count_updated.MessageReactionCountUpdated "aiogram.types.message_reaction_count_updated.MessageReactionCountUpdated") | None = None*, *inline_query: [InlineQuery](inline_query.html#aiogram.types.inline_query.InlineQuery "aiogram.types.inline_query.InlineQuery") | None = None*, *chosen_inline_result: [ChosenInlineResult](chosen_inline_result.html#aiogram.types.chosen_inline_result.ChosenInlineResult "aiogram.types.chosen_inline_result.ChosenInlineResult") | None = None*, *callback_query: [CallbackQuery](callback_query.html#aiogram.types.callback_query.CallbackQuery "aiogram.types.callback_query.CallbackQuery") | None = None*, *shipping_query: [ShippingQuery](shipping_query.html#aiogram.types.shipping_query.ShippingQuery "aiogram.types.shipping_query.ShippingQuery") | None = None*, *pre_checkout_query: [PreCheckoutQuery](pre_checkout_query.html#aiogram.types.pre_checkout_query.PreCheckoutQuery "aiogram.types.pre_checkout_query.PreCheckoutQuery") | None = None*, *purchased_paid_media: [PaidMediaPurchased](paid_media_purchased.html#aiogram.types.paid_media_purchased.PaidMediaPurchased "aiogram.types.paid_media_purchased.PaidMediaPurchased") | None = None*, *poll: [Poll](poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") | None = None*, *poll_answer: [PollAnswer](poll_answer.html#aiogram.types.poll_answer.PollAnswer "aiogram.types.poll_answer.PollAnswer") | None = None*, *my_chat_member: [ChatMemberUpdated](chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated "aiogram.types.chat_member_updated.ChatMemberUpdated") | None = None*, *chat_member: [ChatMemberUpdated](chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated "aiogram.types.chat_member_updated.ChatMemberUpdated") | None = None*, *chat_join_request: [ChatJoinRequest](chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest "aiogram.types.chat_join_request.ChatJoinRequest") | None = None*, *chat_boost: [ChatBoostUpdated](chat_boost_updated.html#aiogram.types.chat_boost_updated.ChatBoostUpdated "aiogram.types.chat_boost_updated.ChatBoostUpdated") | None = None*, *removed_chat_boost: [ChatBoostRemoved](chat_boost_removed.html#aiogram.types.chat_boost_removed.ChatBoostRemoved "aiogram.types.chat_boost_removed.ChatBoostRemoved") | None = None*, *managed_bot: [ManagedBotUpdated](managed_bot_updated.html#aiogram.types.managed_bot_updated.ManagedBotUpdated "aiogram.types.managed_bot_updated.ManagedBotUpdated") | None = None*, *subscription: [BotSubscriptionUpdated](bot_subscription_updated.html#aiogram.types.bot_subscription_updated.BotSubscriptionUpdated "aiogram.types.bot_subscription_updated.BotSubscriptionUpdated") | None = None*, *\*\*extra_data: Any*)
:   This [object](https://core.telegram.org/bots/api#available-types) represents an incoming update.

    At most **one** of the optional fields can be present in any given update.

    Source: <https://core.telegram.org/bots/api#update>

    update_id*: int*
    :   The update’s unique identifier. Update identifiers start from a certain positive number and increase sequentially. This identifier becomes especially handy if you’re using [webhooks](https://core.telegram.org/bots/api#setwebhook), since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially

    message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. New incoming message of any kind - text, photo, sticker, etc

    edited_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. New version of a message that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot

    channel_post*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. New incoming channel post of any kind - text, photo, sticker, etc

    edited_channel_post*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. New version of a channel post that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot

    business_connection*: [BusinessConnection](business_connection.html#aiogram.types.business_connection.BusinessConnection "aiogram.types.business_connection.BusinessConnection") | None*
    :   *Optional*. The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot

    business_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. New message from a connected business account

    edited_business_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. New version of a message from a connected business account

    deleted_business_messages*: [BusinessMessagesDeleted](business_messages_deleted.html#aiogram.types.business_messages_deleted.BusinessMessagesDeleted "aiogram.types.business_messages_deleted.BusinessMessagesDeleted") | None*
    :   *Optional*. Messages were deleted from a connected business account

    guest_message*: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | None*
    :   *Optional*. New guest message. The bot can use the field *Message.guest_query_id* and the method [`aiogram.methods.answer_guest_query.AnswerGuestQuery`](../methods/answer_guest_query.html#aiogram.methods.answer_guest_query.AnswerGuestQuery "aiogram.methods.answer_guest_query.AnswerGuestQuery") to send a message in response

    message_reaction*: [MessageReactionUpdated](message_reaction_updated.html#aiogram.types.message_reaction_updated.MessageReactionUpdated "aiogram.types.message_reaction_updated.MessageReactionUpdated") | None*
    :   *Optional*. A reaction to a message was changed by a user. The bot must be an administrator in the chat and must explicitly specify `"message_reaction"` in the list of *allowed_updates* to receive these updates. The update isn’t received for reactions set by bots

    message_reaction_count*: [MessageReactionCountUpdated](message_reaction_count_updated.html#aiogram.types.message_reaction_count_updated.MessageReactionCountUpdated "aiogram.types.message_reaction_count_updated.MessageReactionCountUpdated") | None*
    :   *Optional*. Reactions to a message with anonymous reactions were changed. The bot must be an administrator in the chat and must explicitly specify `"message_reaction_count"` in the list of *allowed_updates* to receive these updates. The updates are grouped and can be sent with delay up to a few minutes

    inline_query*: [InlineQuery](inline_query.html#aiogram.types.inline_query.InlineQuery "aiogram.types.inline_query.InlineQuery") | None*
    :   *Optional*. New incoming [inline](https://core.telegram.org/bots/api#inline-mode) query

    chosen_inline_result*: [ChosenInlineResult](chosen_inline_result.html#aiogram.types.chosen_inline_result.ChosenInlineResult "aiogram.types.chosen_inline_result.ChosenInlineResult") | None*
    :   *Optional*. The result of an [inline](https://core.telegram.org/bots/api#inline-mode) query that was chosen by a user and sent to their chat partner. Please see our documentation on the [feedback collecting](https://core.telegram.org/bots/inline#collecting-feedback) for details on how to enable these updates for your bot

    callback_query*: [CallbackQuery](callback_query.html#aiogram.types.callback_query.CallbackQuery "aiogram.types.callback_query.CallbackQuery") | None*
    :   *Optional*. New incoming callback query

    shipping_query*: [ShippingQuery](shipping_query.html#aiogram.types.shipping_query.ShippingQuery "aiogram.types.shipping_query.ShippingQuery") | None*
    :   *Optional*. New incoming shipping query. Only for invoices with flexible price

    pre_checkout_query*: [PreCheckoutQuery](pre_checkout_query.html#aiogram.types.pre_checkout_query.PreCheckoutQuery "aiogram.types.pre_checkout_query.PreCheckoutQuery") | None*
    :   *Optional*. New incoming pre-checkout query. Contains full information about checkout

    purchased_paid_media*: [PaidMediaPurchased](paid_media_purchased.html#aiogram.types.paid_media_purchased.PaidMediaPurchased "aiogram.types.paid_media_purchased.PaidMediaPurchased") | None*
    :   *Optional*. A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat

    poll*: [Poll](poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") | None*
    :   *Optional*. New poll state. Bots receive only updates about manually stopped polls and polls, which are sent by the bot

    poll_answer*: [PollAnswer](poll_answer.html#aiogram.types.poll_answer.PollAnswer "aiogram.types.poll_answer.PollAnswer") | None*
    :   *Optional*. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself

    my_chat_member*: [ChatMemberUpdated](chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated "aiogram.types.chat_member_updated.ChatMemberUpdated") | None*
    :   *Optional*. The bot’s chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user

    chat_member*: [ChatMemberUpdated](chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated "aiogram.types.chat_member_updated.ChatMemberUpdated") | None*
    :   *Optional*. A chat member’s status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify `"chat_member"` in the list of *allowed_updates* to receive these updates

    chat_join_request*: [ChatJoinRequest](chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest "aiogram.types.chat_join_request.ChatJoinRequest") | None*
    :   *Optional*. A request to join the chat has been sent. The bot must have the *can_invite_users* administrator right in the chat to receive these updates

    chat_boost*: [ChatBoostUpdated](chat_boost_updated.html#aiogram.types.chat_boost_updated.ChatBoostUpdated "aiogram.types.chat_boost_updated.ChatBoostUpdated") | None*
    :   *Optional*. A chat boost was added or changed. The bot must be an administrator in the chat to receive these updates

    removed_chat_boost*: [ChatBoostRemoved](chat_boost_removed.html#aiogram.types.chat_boost_removed.ChatBoostRemoved "aiogram.types.chat_boost_removed.ChatBoostRemoved") | None*
    :   *Optional*. A boost was removed from a chat. The bot must be an administrator in the chat to receive these updates

    managed_bot*: [ManagedBotUpdated](managed_bot_updated.html#aiogram.types.managed_bot_updated.ManagedBotUpdated "aiogram.types.managed_bot_updated.ManagedBotUpdated") | None*
    :   *Optional*. A new bot was created to be managed by the bot, or token or owner of a managed bot was changed

    subscription*: [BotSubscriptionUpdated](bot_subscription_updated.html#aiogram.types.bot_subscription_updated.BotSubscriptionUpdated "aiogram.types.bot_subscription_updated.BotSubscriptionUpdated") | None*
    :   *Optional*. User payment subscription has changed

    *property* event_type*: str*
    :   Detect update type
        If update type is unknown, raise UpdateTypeLookupError

        Returns:

    *property* event*: TelegramObject*

*exception* aiogram.types.update.UpdateTypeLookupError
:   Update does not contain any known event type.
