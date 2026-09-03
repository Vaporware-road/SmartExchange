# sendPoll

> Source: [https://docs.aiogram.dev/en/latest/api/methods/send_poll.html](https://docs.aiogram.dev/en/latest/api/methods/send_poll.html)

Returns: `Message`

*class* aiogram.methods.send_poll.SendPoll(*\*, chat_id: int | str, question: str, options: list[~aiogram.types.input_poll_option.InputPollOption | str], business_connection_id: str | None = None, message_thread_id: int | None = None, question_parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>, question_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None, is_anonymous: bool | None = None, type: str | None = None, allows_multiple_answers: bool | None = None, allows_revoting: bool | None = None, shuffle_options: bool | None = None, allow_adding_options: bool | None = None, hide_results_until_closes: bool | None = None, members_only: bool | None = None, country_codes: list[str] | None = None, correct_option_ids: list[int] | None = None, explanation: str | None = None, explanation_parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>, explanation_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None, explanation_media: ~typing.Annotated[~aiogram.types.input_media_animation.InputMediaAnimation | ~aiogram.types.input_media_audio.InputMediaAudio | ~aiogram.types.input_media_document.InputMediaDocument | ~aiogram.types.input_media_live_photo.InputMediaLivePhoto | ~aiogram.types.input_media_location.InputMediaLocation | ~aiogram.types.input_media_photo.InputMediaPhoto | ~aiogram.types.input_media_venue.InputMediaVenue | ~aiogram.types.input_media_video.InputMediaVideo, FieldInfo(annotation=NoneType, required=True, discriminator='type')] | None = None, open_period: int | None = None, close_date: ~datetime.datetime | ~datetime.timedelta | int | None = None, is_closed: bool | None = None, description: str | None = None, description_parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>, description_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None, media: ~typing.Annotated[~aiogram.types.input_media_animation.InputMediaAnimation | ~aiogram.types.input_media_audio.InputMediaAudio | ~aiogram.types.input_media_document.InputMediaDocument | ~aiogram.types.input_media_live_photo.InputMediaLivePhoto | ~aiogram.types.input_media_location.InputMediaLocation | ~aiogram.types.input_media_photo.InputMediaPhoto | ~aiogram.types.input_media_venue.InputMediaVenue | ~aiogram.types.input_media_video.InputMediaVideo, FieldInfo(annotation=NoneType, required=True, discriminator='type')] | None = None, disable_notification: bool | None = None, protect_content: bool | ~aiogram.client.default.Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_parameters: ~aiogram.types.reply_parameters.ReplyParameters | None = None, reply_markup: ~aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup | ~aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup | ~aiogram.types.reply_keyboard_remove.ReplyKeyboardRemove | ~aiogram.types.force_reply.ForceReply | None = None, allow_sending_without_reply: bool | None = None, correct_option_id: int | None = None, reply_to_message_id: int | None = None, \*\*extra_data: ~typing.Any*)
:   Use this method to send a native poll. On success, the sent [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

    Source: <https://core.telegram.org/bots/api#sendpoll>

    chat_id*: ChatIdUnion*
    :   Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`. Polls can’t be sent to channel direct messages chats

    question*: str*
    :   Poll question, 1-300 characters

    options*: list[InputPollOptionUnion]*
    :   A JSON-serialized list of 1-12 answer options

    business_connection_id*: str | None*
    :   Unique identifier of the business connection on behalf of which the message will be sent

    message_thread_id*: int | None*
    :   Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only

    question_parse_mode*: str | Default | None*
    :   Mode for parsing entities in the question. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. Currently, only custom emoji entities are allowed

    question_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of *question_parse_mode*

    is_anonymous*: bool | None*
    :   `True`, if the poll needs to be anonymous, defaults to `True`

    type*: str | None*
    :   Poll type, ‘quiz’ or ‘regular’, defaults to ‘regular’

    allows_multiple_answers*: bool | None*
    :   Pass `True` if the poll allows multiple answers, defaults to `False`

    allows_revoting*: bool | None*
    :   Pass `True` if the poll allows to change chosen answer options, defaults to `False` for quizzes and to `True` for regular polls

    shuffle_options*: bool | None*
    :   Pass `True` if the poll options must be shown in random order

    allow_adding_options*: bool | None*
    :   Pass `True` if answer options can be added to the poll after creation; not supported for anonymous polls and quizzes

    hide_results_until_closes*: bool | None*
    :   Pass `True` if poll results must be shown only after the poll closes

    members_only*: bool | None*
    :   Pass `True` if voting is limited to users who have been members of the chat where the poll is being sent for more than 24 hours; for channel chats only

    country_codes*: list[str] | None*
    :   A JSON-serialized list of 0-12 two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes indicating the countries from which users can vote in the poll; for channel chats only. Use ‘FT’ as a country code to allow users with anonymous numbers to vote. If omitted or empty, then users from any country can participate in the poll

    correct_option_ids*: list[int] | None*
    :   A JSON-serialized list of monotonically increasing 0-based identifiers of the correct answer options, required for polls in quiz mode

    explanation*: str | None*
    :   Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing

    explanation_parse_mode*: str | Default | None*
    :   Mode for parsing entities in the explanation. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    explanation_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the poll explanation. It can be specified instead of *explanation_parse_mode*

    explanation_media*: InputPollMediaUnion | None*
    :   Media added to the quiz explanation

    open_period*: int | None*
    :   Amount of time in seconds the poll will be active after creation, 5-2628000. Can’t be used together with *close_date*

    close_date*: DateTimeUnion | None*
    :   Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 2628000 seconds in the future. Can’t be used together with *open_period*

    is_closed*: bool | None*
    :   Pass `True` if the poll needs to be immediately closed. This can be useful for poll preview

    description*: str | None*
    :   Description of the poll to be sent, 0-1024 characters after entities parsing

    description_parse_mode*: str | Default | None*
    :   Mode for parsing entities in the poll description. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    description_entities*: list[[MessageEntity](../types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   A JSON-serialized list of special entities that appear in the poll description, which can be specified instead of *description_parse_mode*

    media*: InputPollMediaUnion | None*
    :   Media added to the poll description

    disable_notification*: bool | None*
    :   Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound

    protect_content*: bool | Default | None*
    :   Protects the contents of the sent message from forwarding and saving

    allow_paid_broadcast*: bool | None*
    :   Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance

    message_effect_id*: str | None*
    :   Unique identifier of the message effect to be added to the message; for private chats only

    reply_parameters*: [ReplyParameters](../types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None*
    :   Description of the message to reply to

    reply_markup*: ReplyMarkupUnion | None*
    :   Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user

    allow_sending_without_reply*: bool | None*
    :   Pass `True` if the message should be sent even if the specified replied-to message is not found

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

    correct_option_id*: int | None*
    :   0-based identifier of the correct answer option, required for polls in quiz mode

        Deprecated since version API:9.6: <https://core.telegram.org/bots/api-changelog#april-3-2026>

    reply_to_message_id*: int | None*
    :   If the message is a reply, ID of the original message

        Deprecated since version API:7.0: <https://core.telegram.org/bots/api-changelog#december-29-2023>

## Usage

### As bot method

```
result: Message = await bot.send_poll(...)
```

### Method as object

Imports:

- `from aiogram.methods.send_poll import SendPoll`
- alias: `from aiogram.methods import SendPoll`

#### With specific bot

```
result: Message = await bot(SendPoll(...))
```

#### As reply into Webhook in handler

```
return SendPoll(...)
```

### As shortcut from received object

- [`aiogram.types.message.Message.answer_poll()`](../types/message.html#aiogram.types.message.Message.answer_poll "aiogram.types.message.Message.answer_poll")
- [`aiogram.types.message.Message.reply_poll()`](../types/message.html#aiogram.types.message.Message.reply_poll "aiogram.types.message.Message.reply_poll")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_poll()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_poll "aiogram.types.chat_join_request.ChatJoinRequest.answer_poll")
- [`aiogram.types.chat_join_request.ChatJoinRequest.answer_poll_pm()`](../types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_poll_pm "aiogram.types.chat_join_request.ChatJoinRequest.answer_poll_pm")
- [`aiogram.types.chat_member_updated.ChatMemberUpdated.answer_poll()`](../types/chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated.answer_poll "aiogram.types.chat_member_updated.ChatMemberUpdated.answer_poll")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.answer_poll()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.answer_poll "aiogram.types.inaccessible_message.InaccessibleMessage.answer_poll")
- [`aiogram.types.inaccessible_message.InaccessibleMessage.reply_poll()`](../types/inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage.reply_poll "aiogram.types.inaccessible_message.InaccessibleMessage.reply_poll")
