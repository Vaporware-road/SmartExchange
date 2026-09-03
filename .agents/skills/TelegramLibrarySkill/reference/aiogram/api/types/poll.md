# Poll

> Source: [https://docs.aiogram.dev/en/latest/api/types/poll.html](https://docs.aiogram.dev/en/latest/api/types/poll.html)

*class* aiogram.types.poll.Poll(*\**, *id: str*, *question: str*, *options: list[[PollOption](poll_option.html#aiogram.types.poll_option.PollOption "aiogram.types.poll_option.PollOption")]*, *total_voter_count: int*, *is_closed: bool*, *is_anonymous: bool*, *type: str*, *allows_multiple_answers: bool*, *allows_revoting: bool*, *members_only: bool*, *question_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *country_codes: list[str] | None = None*, *correct_option_ids: list[int] | None = None*, *explanation: str | None = None*, *explanation_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *explanation_media: [PollMedia](poll_media.html#aiogram.types.poll_media.PollMedia "aiogram.types.poll_media.PollMedia") | None = None*, *open_period: int | None = None*, *close_date: _datetime_serializer, return_type=int, when_used=unless - none)] | None = None*, *description: str | None = None*, *description_entities: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None = None*, *media: [PollMedia](poll_media.html#aiogram.types.poll_media.PollMedia "aiogram.types.poll_media.PollMedia") | None = None*, *correct_option_id: int | None = None*, *\*\*extra_data: Any*)
:   This object contains information about a poll.

    Source: <https://core.telegram.org/bots/api#poll>

    id*: str*
    :   Unique poll identifier

    question*: str*
    :   Poll question, 1-300 characters

    options*: list[[PollOption](poll_option.html#aiogram.types.poll_option.PollOption "aiogram.types.poll_option.PollOption")]*
    :   List of poll options

    total_voter_count*: int*
    :   Total number of users that voted in the poll

    is_closed*: bool*
    :   `True`, if the poll is closed

    is_anonymous*: bool*
    :   `True`, if the poll is anonymous

    type*: str*
    :   Poll type, currently can be ‘regular’ or ‘quiz’

    allows_multiple_answers*: bool*
    :   `True`, if the poll allows multiple answers

    allows_revoting*: bool*
    :   `True`, if the poll allows to change the chosen answer options

    members_only*: bool*
    :   `True` if voting is limited to users who have been members of the chat where the poll was originally sent for more than 24 hours

    question_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. Special entities that appear in the *question*. Currently, only custom emoji entities are allowed in poll questions

    country_codes*: list[str] | None*
    :   *Optional*. A list of two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes indicating the countries from which users can vote in the poll. The country code ‘FT’ is used for users with anonymous numbers. If omitted, then users from any country can participate in the poll

    correct_option_ids*: list[int] | None*
    :   *Optional*. Array of 0-based identifiers of the correct answer options. Available only for polls in quiz mode which are closed or were sent (not forwarded) by the bot or to the private chat with the bot

    explanation*: str | None*
    :   *Optional*. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters

    explanation_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. Special entities like usernames, URLs, bot commands, etc. that appear in the *explanation*

    explanation_media*: [PollMedia](poll_media.html#aiogram.types.poll_media.PollMedia "aiogram.types.poll_media.PollMedia") | None*
    :   *Optional*. Media added to the quiz explanation

    open_period*: int | None*
    :   *Optional*. Amount of time in seconds the poll will be active after creation

    close_date*: DateTime | None*
    :   *Optional*. Point in time (Unix timestamp) when the poll will be automatically closed

    description*: str | None*
    :   *Optional*. Description of the poll; for polls inside the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object only

    description_entities*: list[[MessageEntity](message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")] | None*
    :   *Optional*. Special entities like usernames, URLs, bot commands, etc. that appear in the description

    media*: [PollMedia](poll_media.html#aiogram.types.poll_media.PollMedia "aiogram.types.poll_media.PollMedia") | None*
    :   *Optional*. Media added to the poll description; for polls inside the [`aiogram.types.message.Message`](message.html#aiogram.types.message.Message "aiogram.types.message.Message") object only

    correct_option_id*: int | None*
    :   *Optional*. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot

        Deprecated since version API:9.6: <https://core.telegram.org/bots/api-changelog#april-3-2026>
