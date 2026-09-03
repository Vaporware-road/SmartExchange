# getGameHighScores

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_game_high_scores.html](https://docs.aiogram.dev/en/latest/api/methods/get_game_high_scores.html)

Returns: `list[GameHighScore]`

*class* aiogram.methods.get_game_high_scores.GetGameHighScores(*\**, *user_id: int*, *chat_id: int | None = None*, *message_id: int | None = None*, *inline_message_id: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. Returns an Array of [`aiogram.types.game_high_score.GameHighScore`](../types/game_high_score.html#aiogram.types.game_high_score.GameHighScore "aiogram.types.game_high_score.GameHighScore") objects.

    > This method will currently return scores for the target user, plus two of their closest neighbors on each side. Will also return the top three users if the user and their neighbors are not among them. Please note that this behavior is subject to change.

    Source: <https://core.telegram.org/bots/api#getgamehighscores>

    user_id*: int*
    :   Target user id

    chat_id*: int | None*
    :   Required if *inline_message_id* is not specified. Unique identifier for the target chat

    message_id*: int | None*
    :   Required if *inline_message_id* is not specified. Identifier of the sent message

    inline_message_id*: str | None*
    :   Required if *chat_id* and *message_id* are not specified. Identifier of the inline message

## Usage

### As bot method

```
result: list[GameHighScore] = await bot.get_game_high_scores(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_game_high_scores import GetGameHighScores`
- alias: `from aiogram.methods import GetGameHighScores`

#### With specific bot

```
result: list[GameHighScore] = await bot(GetGameHighScores(...))
```
