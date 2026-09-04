# InlineQuery

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query.html](https://docs.aiogram.dev/en/latest/api/types/inline_query.html)

*class* aiogram.types.inline_query.InlineQuery(*\**, *id: str*, *from_user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*, *query: str*, *offset: str*, *chat_type: str | None = None*, *location: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location") | None = None*, *\*\*extra_data: Any*)
:   This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    Source: <https://core.telegram.org/bots/api#inlinequery>

    id*: str*
    :   Unique identifier for this query

    from_user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Sender

    query*: str*
    :   Text of the query (up to 256 characters)

    offset*: str*
    :   Offset of the results to be returned, can be controlled by the bot

    chat_type*: str | None*
    :   *Optional*. Type of the chat from which the inline query was sent. Can be either ‘sender’ for a private chat with the inline query sender, ‘private’, ‘group’, ‘supergroup’, or ‘channel’. The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat

    location*: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location") | None*
    :   *Optional*. Sender location, only for bots that request user location

    answer(*results: list[InlineQueryResultUnion]*, *cache_time: int | None = None*, *is_personal: bool | None = None*, *next_offset: str | None = None*, *button: [InlineQueryResultsButton](inline_query_results_button.html#aiogram.types.inline_query_results_button.InlineQueryResultsButton "aiogram.types.inline_query_results_button.InlineQueryResultsButton") | None = None*, *switch_pm_parameter: str | None = None*, *switch_pm_text: str | None = None*, *\*\*kwargs: Any*) → [AnswerInlineQuery](../methods/answer_inline_query.html#aiogram.methods.answer_inline_query.AnswerInlineQuery "aiogram.methods.answer_inline_query.AnswerInlineQuery")
    :   Shortcut for method [`aiogram.methods.answer_inline_query.AnswerInlineQuery`](../methods/answer_inline_query.html#aiogram.methods.answer_inline_query.AnswerInlineQuery "aiogram.methods.answer_inline_query.AnswerInlineQuery")
        will automatically fill method attributes:

        - `inline_query_id`

        Use this method to send answers to an inline query. On success, `True` is returned.

        No more than **50** results per query are allowed.

        Source: <https://core.telegram.org/bots/api#answerinlinequery>

        Parameters:
        :   - **results** – A JSON-serialized Array of results for the inline query
            - **cache_time** – The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300
            - **is_personal** – Pass `True` if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query
            - **next_offset** – Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don’t support pagination. Offset length can’t exceed 64 bytes
            - **button** – A JSON-serialized object describing a button to be shown above inline query results
            - **switch_pm_parameter** – [Deep-linking](https://core.telegram.org/bots/features#deep-linking) parameter for the /start message sent to the bot when user presses the switch button. 1-64 characters, only `A-Z`, `a-z`, `0-9`, `_` and `-` are allowed
            - **switch_pm_text** – If passed, clients will display a button with specified text that switches the user to a private chat with the bot and sends the bot a start message with the parameter *switch_pm_parameter*

        Returns:
        :   instance of method [`aiogram.methods.answer_inline_query.AnswerInlineQuery`](../methods/answer_inline_query.html#aiogram.methods.answer_inline_query.AnswerInlineQuery "aiogram.methods.answer_inline_query.AnswerInlineQuery")
