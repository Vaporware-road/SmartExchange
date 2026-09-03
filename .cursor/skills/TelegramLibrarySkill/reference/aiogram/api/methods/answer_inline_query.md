# answerInlineQuery

> Source: [https://docs.aiogram.dev/en/latest/api/methods/answer_inline_query.html](https://docs.aiogram.dev/en/latest/api/methods/answer_inline_query.html)

Returns: `bool`

*class* aiogram.methods.answer_inline_query.AnswerInlineQuery(*\**, *inline_query_id: str*, *results: list[[InlineQueryResultCachedAudio](../types/inline_query_result_cached_audio.html#aiogram.types.inline_query_result_cached_audio.InlineQueryResultCachedAudio "aiogram.types.inline_query_result_cached_audio.InlineQueryResultCachedAudio") | [InlineQueryResultCachedDocument](../types/inline_query_result_cached_document.html#aiogram.types.inline_query_result_cached_document.InlineQueryResultCachedDocument "aiogram.types.inline_query_result_cached_document.InlineQueryResultCachedDocument") | [InlineQueryResultCachedGif](../types/inline_query_result_cached_gif.html#aiogram.types.inline_query_result_cached_gif.InlineQueryResultCachedGif "aiogram.types.inline_query_result_cached_gif.InlineQueryResultCachedGif") | [InlineQueryResultCachedMpeg4Gif](../types/inline_query_result_cached_mpeg4_gif.html#aiogram.types.inline_query_result_cached_mpeg4_gif.InlineQueryResultCachedMpeg4Gif "aiogram.types.inline_query_result_cached_mpeg4_gif.InlineQueryResultCachedMpeg4Gif") | [InlineQueryResultCachedPhoto](../types/inline_query_result_cached_photo.html#aiogram.types.inline_query_result_cached_photo.InlineQueryResultCachedPhoto "aiogram.types.inline_query_result_cached_photo.InlineQueryResultCachedPhoto") | [InlineQueryResultCachedSticker](../types/inline_query_result_cached_sticker.html#aiogram.types.inline_query_result_cached_sticker.InlineQueryResultCachedSticker "aiogram.types.inline_query_result_cached_sticker.InlineQueryResultCachedSticker") | [InlineQueryResultCachedVideo](../types/inline_query_result_cached_video.html#aiogram.types.inline_query_result_cached_video.InlineQueryResultCachedVideo "aiogram.types.inline_query_result_cached_video.InlineQueryResultCachedVideo") | [InlineQueryResultCachedVoice](../types/inline_query_result_cached_voice.html#aiogram.types.inline_query_result_cached_voice.InlineQueryResultCachedVoice "aiogram.types.inline_query_result_cached_voice.InlineQueryResultCachedVoice") | [InlineQueryResultArticle](../types/inline_query_result_article.html#aiogram.types.inline_query_result_article.InlineQueryResultArticle "aiogram.types.inline_query_result_article.InlineQueryResultArticle") | [InlineQueryResultAudio](../types/inline_query_result_audio.html#aiogram.types.inline_query_result_audio.InlineQueryResultAudio "aiogram.types.inline_query_result_audio.InlineQueryResultAudio") | [InlineQueryResultContact](../types/inline_query_result_contact.html#aiogram.types.inline_query_result_contact.InlineQueryResultContact "aiogram.types.inline_query_result_contact.InlineQueryResultContact") | [InlineQueryResultGame](../types/inline_query_result_game.html#aiogram.types.inline_query_result_game.InlineQueryResultGame "aiogram.types.inline_query_result_game.InlineQueryResultGame") | [InlineQueryResultDocument](../types/inline_query_result_document.html#aiogram.types.inline_query_result_document.InlineQueryResultDocument "aiogram.types.inline_query_result_document.InlineQueryResultDocument") | [InlineQueryResultGif](../types/inline_query_result_gif.html#aiogram.types.inline_query_result_gif.InlineQueryResultGif "aiogram.types.inline_query_result_gif.InlineQueryResultGif") | [InlineQueryResultLocation](../types/inline_query_result_location.html#aiogram.types.inline_query_result_location.InlineQueryResultLocation "aiogram.types.inline_query_result_location.InlineQueryResultLocation") | [InlineQueryResultMpeg4Gif](../types/inline_query_result_mpeg4_gif.html#aiogram.types.inline_query_result_mpeg4_gif.InlineQueryResultMpeg4Gif "aiogram.types.inline_query_result_mpeg4_gif.InlineQueryResultMpeg4Gif") | [InlineQueryResultPhoto](../types/inline_query_result_photo.html#aiogram.types.inline_query_result_photo.InlineQueryResultPhoto "aiogram.types.inline_query_result_photo.InlineQueryResultPhoto") | [InlineQueryResultVenue](../types/inline_query_result_venue.html#aiogram.types.inline_query_result_venue.InlineQueryResultVenue "aiogram.types.inline_query_result_venue.InlineQueryResultVenue") | [InlineQueryResultVideo](../types/inline_query_result_video.html#aiogram.types.inline_query_result_video.InlineQueryResultVideo "aiogram.types.inline_query_result_video.InlineQueryResultVideo") | [InlineQueryResultVoice](../types/inline_query_result_voice.html#aiogram.types.inline_query_result_voice.InlineQueryResultVoice "aiogram.types.inline_query_result_voice.InlineQueryResultVoice")]*, *cache_time: int | None = None*, *is_personal: bool | None = None*, *next_offset: str | None = None*, *button: [InlineQueryResultsButton](../types/inline_query_results_button.html#aiogram.types.inline_query_results_button.InlineQueryResultsButton "aiogram.types.inline_query_results_button.InlineQueryResultsButton") | None = None*, *switch_pm_parameter: str | None = None*, *switch_pm_text: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to send answers to an inline query. On success, `True` is returned.

    No more than **50** results per query are allowed.

    Source: <https://core.telegram.org/bots/api#answerinlinequery>

    inline_query_id*: str*
    :   Unique identifier for the answered query

    results*: list[InlineQueryResultUnion]*
    :   A JSON-serialized Array of results for the inline query

    cache_time*: int | None*
    :   The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300

    is_personal*: bool | None*
    :   Pass `True` if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query

    next_offset*: str | None*
    :   Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don’t support pagination. Offset length can’t exceed 64 bytes

    button*: [InlineQueryResultsButton](../types/inline_query_results_button.html#aiogram.types.inline_query_results_button.InlineQueryResultsButton "aiogram.types.inline_query_results_button.InlineQueryResultsButton") | None*
    :   A JSON-serialized object describing a button to be shown above inline query results

    switch_pm_parameter*: str | None*
    :   [Deep-linking](https://core.telegram.org/bots/features#deep-linking) parameter for the /start message sent to the bot when user presses the switch button. 1-64 characters, only `A-Z`, `a-z`, `0-9`, `_` and `-` are allowed

        Deprecated since version API:6.7: <https://core.telegram.org/bots/api-changelog#april-21-2023>

    switch_pm_text*: str | None*
    :   If passed, clients will display a button with specified text that switches the user to a private chat with the bot and sends the bot a start message with the parameter *switch_pm_parameter*

        Deprecated since version API:6.7: <https://core.telegram.org/bots/api-changelog#april-21-2023>

## Usage

### As bot method

```
result: bool = await bot.answer_inline_query(...)
```

### Method as object

Imports:

- `from aiogram.methods.answer_inline_query import AnswerInlineQuery`
- alias: `from aiogram.methods import AnswerInlineQuery`

#### With specific bot

```
result: bool = await bot(AnswerInlineQuery(...))
```

#### As reply into Webhook in handler

```
return AnswerInlineQuery(...)
```

### As shortcut from received object

- [`aiogram.types.inline_query.InlineQuery.answer()`](../types/inline_query.html#aiogram.types.inline_query.InlineQuery.answer "aiogram.types.inline_query.InlineQuery.answer")
