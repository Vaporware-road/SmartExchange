# CallbackQuery

> Source: [https://docs.aiogram.dev/en/latest/api/types/callback_query.html](https://docs.aiogram.dev/en/latest/api/types/callback_query.html)

*class* aiogram.types.callback_query.CallbackQuery(*\**, *id: str*, *from_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *chat_instance: str*, *message: [Message](message.html#aiogram.types.message.Message "aiogram.types.message.Message") | [InaccessibleMessage](inaccessible_message.html#aiogram.types.inaccessible_message.InaccessibleMessage "aiogram.types.inaccessible_message.InaccessibleMessage") | None = None*, *inline_message_id: str | None = None*, *data: str | None = None*, *game_short_name: str | None = None*, *\*\*extra_data: Any*)
:   This object represents an incoming callback query from a callback button in an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards). If the button that originated the query was attached to a message sent by the bot, the field *message* will be present. If the button was attached to a message sent via the bot (in [inline mode](https://core.telegram.org/bots/api#inline-mode)), the field *inline_message_id* will be present. Exactly one of the fields *data* or *game_short_name* will be present.

    > **NOTE:** After the user presses a callback button, Telegram clients will display a progress bar until you call [`aiogram.methods.answer_callback_query.AnswerCallbackQuery`](../methods/answer_callback_query.html#aiogram.methods.answer_callback_query.AnswerCallbackQuery "aiogram.methods.answer_callback_query.AnswerCallbackQuery"). It is, therefore, necessary to react by calling [`aiogram.methods.answer_callback_query.AnswerCallbackQuery`](../methods/answer_callback_query.html#aiogram.methods.answer_callback_query.AnswerCallbackQuery "aiogram.methods.answer_callback_query.AnswerCallbackQuery") even if no notification to the user is needed (e.g., without specifying any of the optional parameters).

    Source: <https://core.telegram.org/bots/api#callbackquery>

    id*: str*
    :   Unique identifier for this query

    from_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Sender

    chat_instance*: str*
    :   Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in `aiogram.methods.games.Games`

    message*: MaybeInaccessibleMessageUnion | None*
    :   *Optional*. Message sent by the bot with the callback button that originated the query

    inline_message_id*: str | None*
    :   *Optional*. Identifier of the message sent via the bot in inline mode, that originated the query

    data*: str | None*
    :   *Optional*. Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data

    game_short_name*: str | None*
    :   *Optional*. Short name of a [Game](https://core.telegram.org/bots/api#games) to be returned, serves as the unique identifier for the game

    answer(*text: str | None = None*, *show_alert: bool | None = None*, *url: str | None = None*, *cache_time: int | None = None*, *\*\*kwargs: Any*) → [AnswerCallbackQuery](../methods/answer_callback_query.html#aiogram.methods.answer_callback_query.AnswerCallbackQuery "aiogram.methods.answer_callback_query.AnswerCallbackQuery")
    :   Shortcut for method [`aiogram.methods.answer_callback_query.AnswerCallbackQuery`](../methods/answer_callback_query.html#aiogram.methods.answer_callback_query.AnswerCallbackQuery "aiogram.methods.answer_callback_query.AnswerCallbackQuery")
        will automatically fill method attributes:

        - `callback_query_id`

        Use this method to send answers to callback queries sent from [inline keyboards](https://core.telegram.org/bots/features#inline-keyboards). The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, `True` is returned.

        > Alternatively, the user can be redirected to the specified Game URL. For this option to work, you must first create a game for your bot via [@BotFather](https://t.me/botfather) and accept the terms. Otherwise, you may use links like `t.me/your_bot?start=XXXX` that open your bot with a parameter.

        Source: <https://core.telegram.org/bots/api#answercallbackquery>

        Parameters:
        :   - **text** – Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters
            - **show_alert** – If `True`, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to `False`
            - **url** –

              URL that will be opened by the user’s client. If you have created a [`aiogram.types.game.Game`](game.html#aiogram.types.game.Game "aiogram.types.game.Game") and accepted the conditions via [@BotFather](https://t.me/botfather), specify the URL that opens your game - note that this will only work if the query comes from a <https://core.telegram.org/bots/api#inlinekeyboardbutton> *callback_game* button
            - **cache_time** – The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0

        Returns:
        :   instance of method [`aiogram.methods.answer_callback_query.AnswerCallbackQuery`](../methods/answer_callback_query.html#aiogram.methods.answer_callback_query.AnswerCallbackQuery "aiogram.methods.answer_callback_query.AnswerCallbackQuery")
