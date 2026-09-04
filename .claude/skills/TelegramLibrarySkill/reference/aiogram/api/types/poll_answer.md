# PollAnswer

> Source: [https://docs.aiogram.dev/en/latest/api/types/poll_answer.html](https://docs.aiogram.dev/en/latest/api/types/poll_answer.html)

*class* aiogram.types.poll_answer.PollAnswer(*\**, *poll_id: str*, *option_ids: list[int]*, *option_persistent_ids: list[str]*, *voter_chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *user: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None = None*, *\*\*extra_data: Any*)
:   This object represents an answer of a user in a non-anonymous poll.

    Source: <https://core.telegram.org/bots/api#pollanswer>

    poll_id*: str*
    :   Unique poll identifier

    option_ids*: list[int]*
    :   0-based identifiers of chosen answer options. May be empty if the vote was retracted

    option_persistent_ids*: list[str]*
    :   Persistent identifiers of the chosen answer options. May be empty if the vote was retracted

    voter_chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. The chat that changed the answer to the poll, if the voter is anonymous

    user*: [User](user.html#aiogram.types.user.User "aiogram.types.user.User") | None*
    :   *Optional*. The user that changed the answer to the poll, if the voter isn’t anonymous
