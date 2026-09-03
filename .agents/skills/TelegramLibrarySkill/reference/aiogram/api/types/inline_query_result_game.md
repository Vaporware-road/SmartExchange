# InlineQueryResultGame

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result_game.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result_game.html)

*class* aiogram.types.inline_query_result_game.InlineQueryResultGame(*\**, *type: Literal[InlineQueryResultType.GAME] = InlineQueryResultType.GAME*, *id: str*, *game_short_name: str*, *reply_markup: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None = None*, *\*\*extra_data: Any*)
:   Represents a [Game](https://core.telegram.org/bots/api#games).

    Source: <https://core.telegram.org/bots/api#inlinequeryresultgame>

    type*: Literal[InlineQueryResultType.GAME]*
    :   Type of the result, must be *game*

    id*: str*
    :   Unique identifier for this result, 1-64 bytes

    game_short_name*: str*
    :   Short name of the game

    reply_markup*: [InlineKeyboardMarkup](inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup") | None*
    :   *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message
