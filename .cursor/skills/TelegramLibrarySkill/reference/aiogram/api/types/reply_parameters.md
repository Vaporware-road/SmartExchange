# ReplyParameters

> Source: [https://docs.aiogram.dev/en/latest/api/types/reply_parameters.html](https://docs.aiogram.dev/en/latest/api/types/reply_parameters.html)

*class* aiogram.types.reply_parameters.ReplyParameters(*\**, *message_id: int | None = None*, *chat_id: int | str | None = None*, *allow_sending_without_reply: bool | ~aiogram.client.default.Default | None = <Default('allow_sending_without_reply')>*, *quote: str | None = None*, *quote_parse_mode: str | ~aiogram.client.default.Default | None = <Default('parse_mode')>*, *quote_entities: list[~aiogram.types.message_entity.MessageEntity] | None = None*, *quote_position: int | None = None*, *checklist_task_id: int | None = None*, *poll_option_id: str | None = None*, *ephemeral_message_id: int | None = None*, *\*\*extra_data: ~typing.Any*)
:   Describes reply parameters for the message that is being sent.

    Source: <https://core.telegram.org/bots/api#replyparameters>

    message_id*: int | None*
    :   *Optional*. Identifier of the message that will be replied to in the current chat, or in the chat *chat_id* if it is specified. Required if *ephemeral_message_id* isn’t specified

    chat_id*: ChatIdUnion | None*
    :   *Optional*. If the message to be replied to is from a different chat, unique identifier for the chat or username of the bot, supergroup or channel in the format `@username`. Not supported for messages sent on behalf of a business account, messages from channel direct messages chats and ephemeral messages

    allow_sending_without_reply*: bool | Default | None*
    :   *Optional*. Pass `True` if the message should be sent even if the specified message to be replied to is not found. Always `False` for replies in another chat or forum topic, and sent ephemeral messages. Always `True` for messages sent on behalf of a business account

    quote*: str | None*
    :   *Optional*. Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, *custom_emoji*, and *date_time* entities. The message will fail to send if the quote isn’t found in the original message. Ignored for ephemeral messages

    quote_parse_mode*: str | Default | None*
    :   *Optional*. Mode for parsing entities in the quote. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details

    quote_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. A JSON-serialized list of special entities that appear in the quote. It can be specified instead of *quote_parse_mode*

    quote_position*: int | None*
    :   *Optional*. Position of the quote in the original message in UTF-16 code units

    checklist_task_id*: int | None*
    :   *Optional*. Identifier of the specific checklist task to be replied to

    poll_option_id*: str | None*
    :   *Optional*. Persistent identifier of the specific poll option to be replied to

    ephemeral_message_id*: int | None*
    :   *Optional*. Identifier of the incoming ephemeral message that will be replied to in the current chat. A reply to an ephemeral message must itself be an ephemeral message. An ephemeral message may only be replied to within 15 seconds of being sent. Required if *message_id* isn’t specified
