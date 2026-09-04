# answerWebAppQuery

> Source: [https://docs.aiogram.dev/en/latest/api/methods/answer_web_app_query.html](https://docs.aiogram.dev/en/latest/api/methods/answer_web_app_query.html)

Returns: `SentWebAppMessage`

*class* aiogram.methods.answer_web_app_query.AnswerWebAppQuery(*\**, *web_app_query_id: str*, *result: [InlineQueryResultCachedAudio](../types/inline_query_result_cached_audio.html#aiogram.types.inline_query_result_cached_audio.InlineQueryResultCachedAudio "aiogram.types.inline_query_result_cached_audio.InlineQueryResultCachedAudio") | [InlineQueryResultCachedDocument](../types/inline_query_result_cached_document.html#aiogram.types.inline_query_result_cached_document.InlineQueryResultCachedDocument "aiogram.types.inline_query_result_cached_document.InlineQueryResultCachedDocument") | [InlineQueryResultCachedGif](../types/inline_query_result_cached_gif.html#aiogram.types.inline_query_result_cached_gif.InlineQueryResultCachedGif "aiogram.types.inline_query_result_cached_gif.InlineQueryResultCachedGif") | [InlineQueryResultCachedMpeg4Gif](../types/inline_query_result_cached_mpeg4_gif.html#aiogram.types.inline_query_result_cached_mpeg4_gif.InlineQueryResultCachedMpeg4Gif "aiogram.types.inline_query_result_cached_mpeg4_gif.InlineQueryResultCachedMpeg4Gif") | [InlineQueryResultCachedPhoto](../types/inline_query_result_cached_photo.html#aiogram.types.inline_query_result_cached_photo.InlineQueryResultCachedPhoto "aiogram.types.inline_query_result_cached_photo.InlineQueryResultCachedPhoto") | [InlineQueryResultCachedSticker](../types/inline_query_result_cached_sticker.html#aiogram.types.inline_query_result_cached_sticker.InlineQueryResultCachedSticker "aiogram.types.inline_query_result_cached_sticker.InlineQueryResultCachedSticker") | [InlineQueryResultCachedVideo](../types/inline_query_result_cached_video.html#aiogram.types.inline_query_result_cached_video.InlineQueryResultCachedVideo "aiogram.types.inline_query_result_cached_video.InlineQueryResultCachedVideo") | [InlineQueryResultCachedVoice](../types/inline_query_result_cached_voice.html#aiogram.types.inline_query_result_cached_voice.InlineQueryResultCachedVoice "aiogram.types.inline_query_result_cached_voice.InlineQueryResultCachedVoice") | [InlineQueryResultArticle](../types/inline_query_result_article.html#aiogram.types.inline_query_result_article.InlineQueryResultArticle "aiogram.types.inline_query_result_article.InlineQueryResultArticle") | [InlineQueryResultAudio](../types/inline_query_result_audio.html#aiogram.types.inline_query_result_audio.InlineQueryResultAudio "aiogram.types.inline_query_result_audio.InlineQueryResultAudio") | [InlineQueryResultContact](../types/inline_query_result_contact.html#aiogram.types.inline_query_result_contact.InlineQueryResultContact "aiogram.types.inline_query_result_contact.InlineQueryResultContact") | [InlineQueryResultGame](../types/inline_query_result_game.html#aiogram.types.inline_query_result_game.InlineQueryResultGame "aiogram.types.inline_query_result_game.InlineQueryResultGame") | [InlineQueryResultDocument](../types/inline_query_result_document.html#aiogram.types.inline_query_result_document.InlineQueryResultDocument "aiogram.types.inline_query_result_document.InlineQueryResultDocument") | [InlineQueryResultGif](../types/inline_query_result_gif.html#aiogram.types.inline_query_result_gif.InlineQueryResultGif "aiogram.types.inline_query_result_gif.InlineQueryResultGif") | [InlineQueryResultLocation](../types/inline_query_result_location.html#aiogram.types.inline_query_result_location.InlineQueryResultLocation "aiogram.types.inline_query_result_location.InlineQueryResultLocation") | [InlineQueryResultMpeg4Gif](../types/inline_query_result_mpeg4_gif.html#aiogram.types.inline_query_result_mpeg4_gif.InlineQueryResultMpeg4Gif "aiogram.types.inline_query_result_mpeg4_gif.InlineQueryResultMpeg4Gif") | [InlineQueryResultPhoto](../types/inline_query_result_photo.html#aiogram.types.inline_query_result_photo.InlineQueryResultPhoto "aiogram.types.inline_query_result_photo.InlineQueryResultPhoto") | [InlineQueryResultVenue](../types/inline_query_result_venue.html#aiogram.types.inline_query_result_venue.InlineQueryResultVenue "aiogram.types.inline_query_result_venue.InlineQueryResultVenue") | [InlineQueryResultVideo](../types/inline_query_result_video.html#aiogram.types.inline_query_result_video.InlineQueryResultVideo "aiogram.types.inline_query_result_video.InlineQueryResultVideo") | [InlineQueryResultVoice](../types/inline_query_result_voice.html#aiogram.types.inline_query_result_voice.InlineQueryResultVoice "aiogram.types.inline_query_result_voice.InlineQueryResultVoice")*, *\*\*extra_data: Any*)
:   Use this method to set the result of an interaction with a [Web App](https://core.telegram.org/bots/webapps) and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a [`aiogram.types.sent_web_app_message.SentWebAppMessage`](../types/sent_web_app_message.html#aiogram.types.sent_web_app_message.SentWebAppMessage "aiogram.types.sent_web_app_message.SentWebAppMessage") object is returned.

    Source: <https://core.telegram.org/bots/api#answerwebappquery>

    web_app_query_id*: str*
    :   Unique identifier for the query to be answered

    result*: InlineQueryResultUnion*
    :   A JSON-serialized object describing the message to be sent

## Usage

### As bot method

```
result: SentWebAppMessage = await bot.answer_web_app_query(...)
```

### Method as object

Imports:

- `from aiogram.methods.answer_web_app_query import AnswerWebAppQuery`
- alias: `from aiogram.methods import AnswerWebAppQuery`

#### With specific bot

```
result: SentWebAppMessage = await bot(AnswerWebAppQuery(...))
```

#### As reply into Webhook in handler

```
return AnswerWebAppQuery(...)
```
