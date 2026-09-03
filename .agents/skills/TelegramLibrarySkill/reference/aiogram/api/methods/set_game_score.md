# setGameScore

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_game_score.html](https://docs.aiogram.dev/en/latest/api/methods/set_game_score.html)

Returns: `Message | bool`

*class* aiogram.methods.set_game_score.SetGameScore(*\**, *user_id: int*, *score: int*, *force: bool | None = None*, *disable_edit_message: bool | None = None*, *chat_id: int | None = None*, *message_id: int | None = None*, *inline_message_id: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the [`aiogram.types.message.Message`](../types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") is returned, otherwise `True` is returned. Returns an error, if the new score is not greater than the user’s current score in the chat and *force* is `False`.

    Source: <https://core.telegram.org/bots/api#setgamescore>

    user_id*: int*
    :   User identifier

    score*: int*
    :   New score, must be non-negative

    force*: bool | None*
    :   Pass `True` if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters

    disable_edit_message*: bool | None*
    :   Pass `True` if the game message should not be automatically edited to include the current scoreboard

    chat_id*: int | None*
    :   Required if *inline_message_id* is not specified. Unique identifier for the target chat

    message_id*: int | None*
    :   Required if *inline_message_id* is not specified. Identifier of the sent message

    inline_message_id*: str | None*
    :   Required if *chat_id* and *message_id* are not specified. Identifier of the inline message

## Usage

### As bot method

```
result: Message | bool = await bot.set_game_score(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_game_score import SetGameScore`
- alias: `from aiogram.methods import SetGameScore`

#### With specific bot

```
result: Message | bool = await bot(SetGameScore(...))
```

#### As reply into Webhook in handler

```
return SetGameScore(...)
```
