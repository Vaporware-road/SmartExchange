# InaccessibleMessage

> Source: [https://docs.aiogram.dev/en/latest/api/types/inaccessible_message.html](https://docs.aiogram.dev/en/latest/api/types/inaccessible_message.html)

*class* aiogram.types.inaccessible_message.InaccessibleMessage(*\**, *chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*, *message_id: int*, *date: Literal[0] = 0*, *\*\*extra_data: Any*)
:   This object describes a message that was deleted or is otherwise inaccessible to the bot.

    Source: <https://core.telegram.org/bots/api#inaccessiblemessage>

    chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")*
    :   Chat the message belonged to

    message_id*: int*
    :   Unique message identifier inside the chat

    date*: Literal[0]*
    :   Always 0. The field can be used to differentiate regular and inaccessible messages

    answer(*text: str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *entities: list[MessageEntity] | None = None*, *link_preview_options: LinkPreviewOptions | Default | None = <Default('link_preview')>*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *disable_web_page_preview: bool | Default | None = <Default('link_preview_is_disabled')>*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendMessage](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage")
    :   Shortcut for method [`aiogram.methods.send_message.SendMessage`](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send text messages. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendmessage>

        Parameters:
        :   - **text** – Text of the message to be sent, 1-4096 characters after entities parsing
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
            - **parse_mode** – Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details
            - **entities** – A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode*
            - **link_preview_options** – Link preview generation options for the message
            - **disable_notification** – Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound
            - **protect_content** – Protects the contents of the sent message from forwarding and saving
            - **allow_paid_broadcast** – Pass `True` to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance
            - **message_effect_id** – Unique identifier of the message effect to be added to the message; for private chats only
            - **suggested_post_parameters** – A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** – Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** – For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **disable_web_page_preview** – Disables link previews for links in this message
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_message.SendMessage`](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage")

    reply(*text: str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *entities: list[MessageEntity] | None = None*, *link_preview_options: LinkPreviewOptions | Default | None = <Default('link_preview')>*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *disable_web_page_preview: bool | Default | None = <Default('link_preview_is_disabled')>*, *\*\*kwargs: Any*) → [SendMessage](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage")
    :   Shortcut for method [`aiogram.methods.send_message.SendMessage`](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send text messages. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendmessage>

        Parameters:
        :   - **text** – Text of the message to be sent, 1-4096 characters after entities parsing
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **disable_web_page_preview** – Disables link previews for links in this message

        Returns:
        :   instance of method [`aiogram.methods.send_message.SendMessage`](../methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage")

    answer_animation(*animation: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *duration: int | None = None*, *width: int | None = None*, *height: int | None = None*, *thumbnail: InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendAnimation](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation")
    :   Shortcut for method [`aiogram.methods.send_animation.SendAnimation`](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#sendanimation>

        Parameters:
        :   - **animation** – Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_animation.SendAnimation`](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation")

    reply_animation(*animation: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *duration: int | None = None*, *width: int | None = None*, *height: int | None = None*, *thumbnail: InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendAnimation](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation")
    :   Shortcut for method [`aiogram.methods.send_animation.SendAnimation`](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#sendanimation>

        Parameters:
        :   - **animation** – Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_animation.SendAnimation`](../methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation")

    answer_audio(*audio: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *duration: int | None = None*, *performer: str | None = None*, *title: str | None = None*, *thumbnail: InputFile | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendAudio](../methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio")
    :   Shortcut for method [`aiogram.methods.send_audio.SendAudio`](../methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
        For sending voice messages, use the [`aiogram.methods.send_voice.SendVoice`](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice") method instead.

        Source: <https://core.telegram.org/bots/api#sendaudio>

        Parameters:
        :   - **audio** – Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_audio(*audio: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *duration: int | None = None*, *performer: str | None = None*, *title: str | None = None*, *thumbnail: InputFile | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendAudio](../methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio")
    :   Shortcut for method [`aiogram.methods.send_audio.SendAudio`](../methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
        For sending voice messages, use the [`aiogram.methods.send_voice.SendVoice`](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice") method instead.

        Source: <https://core.telegram.org/bots/api#sendaudio>

        Parameters:
        :   - **audio** – Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_audio.SendAudio`](../methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio")

    answer_contact(*phone_number: str*, *first_name: str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *last_name: str | None = None*, *vcard: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendContact](../methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact")
    :   Shortcut for method [`aiogram.methods.send_contact.SendContact`](../methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send phone contacts. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendcontact>

        Parameters:
        :   - **phone_number** – Contact’s phone number
            - **first_name** – Contact’s first name
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_contact(*phone_number: str*, *first_name: str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *last_name: str | None = None*, *vcard: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendContact](../methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact")
    :   Shortcut for method [`aiogram.methods.send_contact.SendContact`](../methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send phone contacts. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendcontact>

        Parameters:
        :   - **phone_number** – Contact’s phone number
            - **first_name** – Contact’s first name
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_contact.SendContact`](../methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact")

    answer_document(*document: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *thumbnail: InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *disable_content_type_detection: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendDocument](../methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument")
    :   Shortcut for method [`aiogram.methods.send_document.SendDocument`](../methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send general files. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#senddocument>

        Parameters:
        :   - **document** – File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_document(*document: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *thumbnail: InputFile | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *disable_content_type_detection: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendDocument](../methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument")
    :   Shortcut for method [`aiogram.methods.send_document.SendDocument`](../methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send general files. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#senddocument>

        Parameters:
        :   - **document** – File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_document.SendDocument`](../methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument")

    answer_game(*game_short_name: str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: InlineKeyboardMarkup | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendGame](../methods/send_game.html#aiogram.methods.send_game.SendGame "aiogram.methods.send_game.SendGame")
    :   Shortcut for method [`aiogram.methods.send_game.SendGame`](../methods/send_game.html#aiogram.methods.send_game.SendGame "aiogram.methods.send_game.SendGame")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send a game. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendgame>

        Parameters:
        :   - **game_short_name** – Short name of the game, serves as the unique identifier for the game. Set up your games via [@BotFather](https://t.me/botfather)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_game(*game_short_name: str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *reply_markup: InlineKeyboardMarkup | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendGame](../methods/send_game.html#aiogram.methods.send_game.SendGame "aiogram.methods.send_game.SendGame")
    :   Shortcut for method [`aiogram.methods.send_game.SendGame`](../methods/send_game.html#aiogram.methods.send_game.SendGame "aiogram.methods.send_game.SendGame")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send a game. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendgame>

        Parameters:
        :   - **game_short_name** –

              Short name of the game, serves as the unique identifier for the game. Set up your games via [@BotFather](https://t.me/botfather)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    answer_invoice(*title: str, description: str, payload: str, currency: str, prices: list[LabeledPrice], message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, provider_token: str | None = None, max_tip_amount: int | None = None, suggested_tip_amounts: list[int] | None = None, start_parameter: str | None = None, provider_data: str | None = None, photo_url: str | None = None, photo_size: int | None = None, photo_width: int | None = None, photo_height: int | None = None, need_name: bool | None = None, need_phone_number: bool | None = None, need_email: bool | None = None, need_shipping_address: bool | None = None, send_phone_number_to_provider: bool | None = None, send_email_to_provider: bool | None = None, is_flexible: bool | None = None, disable_notification: bool | None = None, protect_content: bool | Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: InlineKeyboardMarkup | None = None, allow_sending_without_reply: bool | None = None, reply_to_message_id: int | None = None, \*\*kwargs: Any*) → [SendInvoice](../methods/send_invoice.html#aiogram.methods.send_invoice.SendInvoice "aiogram.methods.send_invoice.SendInvoice")
    :   Shortcut for method [`aiogram.methods.send_invoice.SendInvoice`](../methods/send_invoice.html#aiogram.methods.send_invoice.SendInvoice "aiogram.methods.send_invoice.SendInvoice")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send invoices. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendinvoice>

        Parameters:
        :   - **title** – Product name, 1-32 characters
            - **description** – Product description, 1-255 characters
            - **payload** – Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes
            - **currency** – Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies). Pass ‘XTR’ for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **prices** –

              Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_invoice(*title: str, description: str, payload: str, currency: str, prices: list[LabeledPrice], message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, provider_token: str | None = None, max_tip_amount: int | None = None, suggested_tip_amounts: list[int] | None = None, start_parameter: str | None = None, provider_data: str | None = None, photo_url: str | None = None, photo_size: int | None = None, photo_width: int | None = None, photo_height: int | None = None, need_name: bool | None = None, need_phone_number: bool | None = None, need_email: bool | None = None, need_shipping_address: bool | None = None, send_phone_number_to_provider: bool | None = None, send_email_to_provider: bool | None = None, is_flexible: bool | None = None, disable_notification: bool | None = None, protect_content: bool | Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, suggested_post_parameters: SuggestedPostParameters | None = None, reply_markup: InlineKeyboardMarkup | None = None, allow_sending_without_reply: bool | None = None, \*\*kwargs: Any*) → [SendInvoice](../methods/send_invoice.html#aiogram.methods.send_invoice.SendInvoice "aiogram.methods.send_invoice.SendInvoice")
    :   Shortcut for method [`aiogram.methods.send_invoice.SendInvoice`](../methods/send_invoice.html#aiogram.methods.send_invoice.SendInvoice "aiogram.methods.send_invoice.SendInvoice")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send invoices. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendinvoice>

        Parameters:
        :   - **title** – Product name, 1-32 characters
            - **description** – Product description, 1-255 characters
            - **payload** – Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes
            - **currency** –

              Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies). Pass ‘XTR’ for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **prices** –

              Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in [Telegram Stars](https://t.me/BotNews/90)
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    answer_location(*latitude: float*, *longitude: float*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *horizontal_accuracy: float | None = None*, *live_period: int | None = None*, *heading: int | None = None*, *proximity_alert_radius: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendLocation](../methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation")
    :   Shortcut for method [`aiogram.methods.send_location.SendLocation`](../methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send point on the map. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendlocation>

        Parameters:
        :   - **latitude** – Latitude of the location
            - **longitude** – Longitude of the location
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_location(*latitude: float*, *longitude: float*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *horizontal_accuracy: float | None = None*, *live_period: int | None = None*, *heading: int | None = None*, *proximity_alert_radius: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendLocation](../methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation")
    :   Shortcut for method [`aiogram.methods.send_location.SendLocation`](../methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send point on the map. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendlocation>

        Parameters:
        :   - **latitude** – Latitude of the location
            - **longitude** – Longitude of the location
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_location.SendLocation`](../methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation")

    answer_media_group(*media: list[MediaUnion], business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_parameters: ReplyParameters | None = None, allow_sending_without_reply: bool | None = None, reply_to_message_id: int | None = None, \*\*kwargs: Any*) → [SendMediaGroup](../methods/send_media_group.html#aiogram.methods.send_media_group.SendMediaGroup "aiogram.methods.send_media_group.SendMediaGroup")
    :   Shortcut for method [`aiogram.methods.send_media_group.SendMediaGroup`](../methods/send_media_group.html#aiogram.methods.send_media_group.SendMediaGroup "aiogram.methods.send_media_group.SendMediaGroup")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send a group of photos, live photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an Array of [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") objects that were sent is returned.

        Source: <https://core.telegram.org/bots/api#sendmediagroup>

        Parameters:
        :   - **media** – A JSON-serialized Array describing messages to be sent, must include 2-10 items
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_media_group(*media: list[MediaUnion], business_connection_id: str | None = None, message_thread_id: int | None = None, direct_messages_topic_id: int | None = None, disable_notification: bool | None = None, protect_content: bool | Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, allow_sending_without_reply: bool | None = None, \*\*kwargs: Any*) → [SendMediaGroup](../methods/send_media_group.html#aiogram.methods.send_media_group.SendMediaGroup "aiogram.methods.send_media_group.SendMediaGroup")
    :   Shortcut for method [`aiogram.methods.send_media_group.SendMediaGroup`](../methods/send_media_group.html#aiogram.methods.send_media_group.SendMediaGroup "aiogram.methods.send_media_group.SendMediaGroup")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send a group of photos, live photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an Array of [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") objects that were sent is returned.

        Source: <https://core.telegram.org/bots/api#sendmediagroup>

        Parameters:
        :   - **media** – A JSON-serialized Array describing messages to be sent, must include 2-10 items
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    answer_photo(*photo: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendPhoto](../methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto")
    :   Shortcut for method [`aiogram.methods.send_photo.SendPhoto`](../methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send photos. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendphoto>

        Parameters:
        :   - **photo** – Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo’s width and height must not exceed 10000 in total. Width and height ratio must be at most 20. [More information on Sending Files »](../upload_file.html#sending-files)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_photo(*photo: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendPhoto](../methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto")
    :   Shortcut for method [`aiogram.methods.send_photo.SendPhoto`](../methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send photos. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendphoto>

        Parameters:
        :   - **photo** – Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo’s width and height must not exceed 10000 in total. Width and height ratio must be at most 20. [More information on Sending Files »](../upload_file.html#sending-files)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_photo.SendPhoto`](../methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto")

    answer_poll(*question: str, options: list[InputPollOptionUnion], business_connection_id: str | None = None, message_thread_id: int | None = None, question_parse_mode: str | Default | None = <Default('parse_mode')>, question_entities: list[MessageEntity] | None = None, is_anonymous: bool | None = None, type: str | None = None, allows_multiple_answers: bool | None = None, allows_revoting: bool | None = None, shuffle_options: bool | None = None, allow_adding_options: bool | None = None, hide_results_until_closes: bool | None = None, members_only: bool | None = None, country_codes: list[str] | None = None, correct_option_ids: list[int] | None = None, explanation: str | None = None, explanation_parse_mode: str | Default | None = <Default('parse_mode')>, explanation_entities: list[MessageEntity] | None = None, explanation_media: InputPollMediaUnion | None = None, open_period: int | None = None, close_date: DateTimeUnion | None = None, is_closed: bool | None = None, description: str | None = None, description_parse_mode: str | Default | None = <Default('parse_mode')>, description_entities: list[MessageEntity] | None = None, media: InputPollMediaUnion | None = None, disable_notification: bool | None = None, protect_content: bool | Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_parameters: ReplyParameters | None = None, reply_markup: ReplyMarkupUnion | None = None, allow_sending_without_reply: bool | None = None, correct_option_id: int | None = None, reply_to_message_id: int | None = None, \*\*kwargs: Any*) → [SendPoll](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll")
    :   Shortcut for method [`aiogram.methods.send_poll.SendPoll`](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send a native poll. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendpoll>

        Parameters:
        :   - **question** – Poll question, 1-300 characters
            - **options** – A JSON-serialized list of 1-12 answer options
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **reply_parameters** – Description of the message to reply to
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **correct_option_id** – 0-based identifier of the correct answer option, required for polls in quiz mode
            - **reply_to_message_id** – If the message is a reply, ID of the original message

        Returns:
        :   instance of method [`aiogram.methods.send_poll.SendPoll`](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll")

    reply_poll(*question: str, options: list[InputPollOptionUnion], business_connection_id: str | None = None, message_thread_id: int | None = None, question_parse_mode: str | Default | None = <Default('parse_mode')>, question_entities: list[MessageEntity] | None = None, is_anonymous: bool | None = None, type: str | None = None, allows_multiple_answers: bool | None = None, allows_revoting: bool | None = None, shuffle_options: bool | None = None, allow_adding_options: bool | None = None, hide_results_until_closes: bool | None = None, members_only: bool | None = None, country_codes: list[str] | None = None, correct_option_ids: list[int] | None = None, explanation: str | None = None, explanation_parse_mode: str | Default | None = <Default('parse_mode')>, explanation_entities: list[MessageEntity] | None = None, explanation_media: InputPollMediaUnion | None = None, open_period: int | None = None, close_date: DateTimeUnion | None = None, is_closed: bool | None = None, description: str | None = None, description_parse_mode: str | Default | None = <Default('parse_mode')>, description_entities: list[MessageEntity] | None = None, media: InputPollMediaUnion | None = None, disable_notification: bool | None = None, protect_content: bool | Default | None = <Default('protect_content')>, allow_paid_broadcast: bool | None = None, message_effect_id: str | None = None, reply_markup: ReplyMarkupUnion | None = None, allow_sending_without_reply: bool | None = None, correct_option_id: int | None = None, \*\*kwargs: Any*) → [SendPoll](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll")
    :   Shortcut for method [`aiogram.methods.send_poll.SendPoll`](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send a native poll. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendpoll>

        Parameters:
        :   - **question** – Poll question, 1-300 characters
            - **options** – A JSON-serialized list of 1-12 answer options
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found
            - **correct_option_id** – 0-based identifier of the correct answer option, required for polls in quiz mode

        Returns:
        :   instance of method [`aiogram.methods.send_poll.SendPoll`](../methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll")

    answer_dice(*business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *emoji: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendDice](../methods/send_dice.html#aiogram.methods.send_dice.SendDice "aiogram.methods.send_dice.SendDice")
    :   Shortcut for method [`aiogram.methods.send_dice.SendDice`](../methods/send_dice.html#aiogram.methods.send_dice.SendDice "aiogram.methods.send_dice.SendDice")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send an animated emoji that will display a random value. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#senddice>

        Parameters:
        :   - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
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

    reply_dice(*business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *emoji: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendDice](../methods/send_dice.html#aiogram.methods.send_dice.SendDice "aiogram.methods.send_dice.SendDice")
    :   Shortcut for method [`aiogram.methods.send_dice.SendDice`](../methods/send_dice.html#aiogram.methods.send_dice.SendDice "aiogram.methods.send_dice.SendDice")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send an animated emoji that will display a random value. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#senddice>

        Parameters:
        :   - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
            - **direct_messages_topic_id** – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat
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

    answer_sticker(*sticker: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *emoji: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendSticker](../methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker")
    :   Shortcut for method [`aiogram.methods.send_sticker.SendSticker`](../methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send static .WEBP, [animated](https://telegram.org/blog/animated-stickers) .TGS, or [video](https://telegram.org/blog/video-stickers-better-reactions) .WEBM stickers. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendsticker>

        Parameters:
        :   - **sticker** – Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP sticker from the Internet, or upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files). Video and animated stickers can’t be sent via an HTTP URL
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_sticker(*sticker: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *emoji: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendSticker](../methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker")
    :   Shortcut for method [`aiogram.methods.send_sticker.SendSticker`](../methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send static .WEBP, [animated](https://telegram.org/blog/animated-stickers) .TGS, or [video](https://telegram.org/blog/video-stickers-better-reactions) .WEBM stickers. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendsticker>

        Parameters:
        :   - **sticker** – Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP sticker from the Internet, or upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files). Video and animated stickers can’t be sent via an HTTP URL
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_sticker.SendSticker`](../methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker")

    answer_venue(*latitude: float*, *longitude: float*, *title: str*, *address: str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *foursquare_id: str | None = None*, *foursquare_type: str | None = None*, *google_place_id: str | None = None*, *google_place_type: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendVenue](../methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue")
    :   Shortcut for method [`aiogram.methods.send_venue.SendVenue`](../methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send information about a venue. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendvenue>

        Parameters:
        :   - **latitude** – Latitude of the venue
            - **longitude** – Longitude of the venue
            - **title** – Name of the venue
            - **address** – Address of the venue
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_venue(*latitude: float*, *longitude: float*, *title: str*, *address: str*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *foursquare_id: str | None = None*, *foursquare_type: str | None = None*, *google_place_id: str | None = None*, *google_place_type: str | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendVenue](../methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue")
    :   Shortcut for method [`aiogram.methods.send_venue.SendVenue`](../methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send information about a venue. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendvenue>

        Parameters:
        :   - **latitude** – Latitude of the venue
            - **longitude** – Longitude of the venue
            - **title** – Name of the venue
            - **address** – Address of the venue
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **reply_markup** –

              Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_venue.SendVenue`](../methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue")

    answer_video(*video: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *duration: int | None = None*, *width: int | None = None*, *height: int | None = None*, *thumbnail: InputFile | None = None*, *cover: InputFileUnion | None = None*, *start_timestamp: DateTimeUnion | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *supports_streaming: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendVideo](../methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo")
    :   Shortcut for method [`aiogram.methods.send_video.SendVideo`](../methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as [`aiogram.types.document.Document`](document.html#aiogram.types.document.Document "aiogram.types.document.Document")). On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#sendvideo>

        Parameters:
        :   - **video** – Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_video(*video: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *duration: int | None = None*, *width: int | None = None*, *height: int | None = None*, *thumbnail: InputFile | None = None*, *cover: InputFileUnion | None = None*, *start_timestamp: DateTimeUnion | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *show_caption_above_media: bool | Default | None = <Default('show_caption_above_media')>*, *has_spoiler: bool | None = None*, *supports_streaming: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendVideo](../methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo")
    :   Shortcut for method [`aiogram.methods.send_video.SendVideo`](../methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as [`aiogram.types.document.Document`](document.html#aiogram.types.document.Document "aiogram.types.document.Document")). On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#sendvideo>

        Parameters:
        :   - **video** – Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_video.SendVideo`](../methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo")

    answer_video_note(*video_note: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *duration: int | None = None*, *length: int | None = None*, *thumbnail: InputFile | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendVideoNote](../methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote")
    :   Shortcut for method [`aiogram.methods.send_video_note.SendVideoNote`](../methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote")
        will automatically fill method attributes:

        - `chat_id`

        As of [v.4.0](https://telegram.org/blog/video-messages-and-telescope), Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendvideonote>

        Parameters:
        :   - **video_note** – Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files). Sending video notes by a URL is currently unsupported
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_video_note(*video_note: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *duration: int | None = None*, *length: int | None = None*, *thumbnail: InputFile | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendVideoNote](../methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote")
    :   Shortcut for method [`aiogram.methods.send_video_note.SendVideoNote`](../methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        As of [v.4.0](https://telegram.org/blog/video-messages-and-telescope), Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendvideonote>

        Parameters:
        :   - **video_note** – Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files). Sending video notes by a URL is currently unsupported
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_video_note.SendVideoNote`](../methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote")

    answer_voice(*voice: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *duration: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_parameters: ReplyParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *reply_to_message_id: int | None = None*, *\*\*kwargs: Any*) → [SendVoice](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice")
    :   Shortcut for method [`aiogram.methods.send_voice.SendVoice`](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS, or in .MP3 format, or in .M4A format (other formats may be sent as [`aiogram.types.audio.Audio`](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio") or [`aiogram.types.document.Document`](document.html#aiogram.types.document.Document "aiogram.types.document.Document")). On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#sendvoice>

        Parameters:
        :   - **voice** – Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_voice(*voice: InputFileUnion*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *caption: str | None = None*, *parse_mode: str | Default | None = <Default('parse_mode')>*, *caption_entities: list[MessageEntity] | None = None*, *duration: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | Default | None = <Default('protect_content')>*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: SuggestedPostParameters | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *receiver_user_id: int | None = None*, *callback_query_id: str | None = None*, *allow_sending_without_reply: bool | None = None*, *\*\*kwargs: Any*) → [SendVoice](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice")
    :   Shortcut for method [`aiogram.methods.send_voice.SendVoice`](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS, or in .MP3 format, or in .M4A format (other formats may be sent as [`aiogram.types.audio.Audio`](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio") or [`aiogram.types.document.Document`](document.html#aiogram.types.document.Document "aiogram.types.document.Document")). On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        Source: <https://core.telegram.org/bots/api#sendvoice>

        Parameters:
        :   - **voice** – Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](../upload_file.html#sending-files)
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
            - **receiver_user_id** –

              For outgoing ephemeral messages, unique identifier of the user who will receive the message; for group and supergroup chats only. It is not guaranteed that the user will receive the message, especially if they are offline. See [ephemeral message sending](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details
            - **callback_query_id** – For outgoing ephemeral messages, identifier of the callback query which triggerred the message if any
            - **allow_sending_without_reply** – Pass `True` if the message should be sent even if the specified replied-to message is not found

        Returns:
        :   instance of method [`aiogram.methods.send_voice.SendVoice`](../methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice")

    answer_paid_media(*star_count: int*, *media: list[InputPaidMediaUnion]*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *payload: str | None = None*, *caption: str | None = None*, *parse_mode: str | None = None*, *caption_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *show_caption_above_media: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *allow_paid_broadcast: bool | None = None*, *suggested_post_parameters: [SuggestedPostParameters](suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None = None*, *reply_parameters: [ReplyParameters](reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *\*\*kwargs: Any*) → [SendPaidMedia](../methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia")
    :   Shortcut for method [`aiogram.methods.send_paid_media.SendPaidMedia`](../methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send paid media. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendpaidmedia>

        Parameters:
        :   - **star_count** – The number of Telegram Stars that must be paid to buy access to the media; 1-25000
            - **media** – A JSON-serialized Array describing the media to be sent; up to 10 items
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_paid_media(*star_count: int*, *media: list[InputPaidMediaUnion]*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *payload: str | None = None*, *caption: str | None = None*, *parse_mode: str | None = None*, *caption_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *show_caption_above_media: bool | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *allow_paid_broadcast: bool | None = None*, *suggested_post_parameters: [SuggestedPostParameters](suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *\*\*kwargs: Any*) → [SendPaidMedia](../methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia")
    :   Shortcut for method [`aiogram.methods.send_paid_media.SendPaidMedia`](../methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send paid media. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendpaidmedia>

        Parameters:
        :   - **star_count** – The number of Telegram Stars that must be paid to buy access to the media; 1-25000
            - **media** – A JSON-serialized Array describing the media to be sent; up to 10 items
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    as_reply_parameters(*allow_sending_without_reply: bool | Default | None = <Default('allow_sending_without_reply')>*, *quote: str | None = None*, *quote_parse_mode: str | Default | None = <Default('parse_mode')>*, *quote_entities: list[MessageEntity] | None = None*, *quote_position: int | None = None*) → [ReplyParameters](reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters")

    answer_rich(*rich_message: [InputRichMessage](input_rich_message.html#aiogram.types.input_rich_message.InputRichMessage "aiogram.types.input_rich_message.InputRichMessage")*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: [SuggestedPostParameters](suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None = None*, *reply_parameters: [ReplyParameters](reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *\*\*kwargs: Any*) → [SendRichMessage](../methods/send_rich_message.html#aiogram.methods.send_rich_message.SendRichMessage "aiogram.methods.send_rich_message.SendRichMessage")
    :   Shortcut for method [`aiogram.methods.send_rich_message.SendRichMessage`](../methods/send_rich_message.html#aiogram.methods.send_rich_message.SendRichMessage "aiogram.methods.send_rich_message.SendRichMessage")
        will automatically fill method attributes:

        - `chat_id`

        Use this method to send rich messages. If the message contains a block with a media element, then the bot must have the right to send the media to the chat. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendrichmessage>

        Parameters:
        :   - **rich_message** – The message to be sent
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent. Bot can send rich messages on behalf of a business account only if the corresponding user can send rich messages
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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

    reply_rich(*rich_message: [InputRichMessage](input_rich_message.html#aiogram.types.input_rich_message.InputRichMessage "aiogram.types.input_rich_message.InputRichMessage")*, *business_connection_id: str | None = None*, *message_thread_id: int | None = None*, *direct_messages_topic_id: int | None = None*, *disable_notification: bool | None = None*, *protect_content: bool | None = None*, *allow_paid_broadcast: bool | None = None*, *message_effect_id: str | None = None*, *suggested_post_parameters: [SuggestedPostParameters](suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") | None = None*, *reply_markup: ReplyMarkupUnion | None = None*, *\*\*kwargs: Any*) → [SendRichMessage](../methods/send_rich_message.html#aiogram.methods.send_rich_message.SendRichMessage "aiogram.methods.send_rich_message.SendRichMessage")
    :   Shortcut for method [`aiogram.methods.send_rich_message.SendRichMessage`](../methods/send_rich_message.html#aiogram.methods.send_rich_message.SendRichMessage "aiogram.methods.send_rich_message.SendRichMessage")
        will automatically fill method attributes:

        - `chat_id`
        - `reply_parameters`

        Use this method to send rich messages. If the message contains a block with a media element, then the bot must have the right to send the media to the chat. On success, the sent [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned.

        Source: <https://core.telegram.org/bots/api#sendrichmessage>

        Parameters:
        :   - **rich_message** – The message to be sent
            - **business_connection_id** – Unique identifier of the business connection on behalf of which the message will be sent. Bot can send rich messages on behalf of a business account only if the corresponding user can send rich messages
            - **message_thread_id** – Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only
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
