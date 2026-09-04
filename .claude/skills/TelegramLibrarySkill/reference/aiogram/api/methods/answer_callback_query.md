# answerCallbackQuery

> Source: [https://docs.aiogram.dev/en/latest/api/methods/answer_callback_query.html](https://docs.aiogram.dev/en/latest/api/methods/answer_callback_query.html)

Returns: `bool`

*class* aiogram.methods.answer_callback_query.AnswerCallbackQuery(*\**, *callback_query_id: str*, *text: str | None = None*, *show_alert: bool | None = None*, *url: str | None = None*, *cache_time: int | None = None*, *\*\*extra_data: Any*)
:   Use this method to send answers to callback queries sent from [inline keyboards](https://core.telegram.org/bots/features#inline-keyboards). The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, `True` is returned.

    > Alternatively, the user can be redirected to the specified Game URL. For this option to work, you must first create a game for your bot via [@BotFather](https://t.me/botfather) and accept the terms. Otherwise, you may use links like `t.me/your_bot?start=XXXX` that open your bot with a parameter.

    Source: <https://core.telegram.org/bots/api#answercallbackquery>

    callback_query_id*: str*
    :   Unique identifier for the query to be answered

    text*: str | None*
    :   Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters

    show_alert*: bool | None*
    :   If `True`, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to `False`

    url*: str | None*
    :   URL that will be opened by the user’s client. If you have created a [`aiogram.types.game.Game`](../types/game.html#aiogram.types.game.Game "aiogram.types.game.Game") and accepted the conditions via [@BotFather](https://t.me/botfather), specify the URL that opens your game - note that this will only work if the query comes from a <https://core.telegram.org/bots/api#inlinekeyboardbutton> *callback_game* button

    cache_time*: int | None*
    :   The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0

## Usage

### As bot method

```
result: bool = await bot.answer_callback_query(...)
```

### Method as object

Imports:

- `from aiogram.methods.answer_callback_query import AnswerCallbackQuery`
- alias: `from aiogram.methods import AnswerCallbackQuery`

#### With specific bot

```
result: bool = await bot(AnswerCallbackQuery(...))
```

#### As reply into Webhook in handler

```
return AnswerCallbackQuery(...)
```

### As shortcut from received object

- [`aiogram.types.callback_query.CallbackQuery.answer()`](../types/callback_query.html#aiogram.types.callback_query.CallbackQuery.answer "aiogram.types.callback_query.CallbackQuery.answer")
