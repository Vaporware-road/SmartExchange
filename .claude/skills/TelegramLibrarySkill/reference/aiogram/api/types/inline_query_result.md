# InlineQueryResult

> Source: [https://docs.aiogram.dev/en/latest/api/types/inline_query_result.html](https://docs.aiogram.dev/en/latest/api/types/inline_query_result.html)

*class* aiogram.types.inline_query_result.InlineQueryResult(*\*\*extra_data: Any*)
:   This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:

    > - [`aiogram.types.inline_query_result_cached_audio.InlineQueryResultCachedAudio`](inline_query_result_cached_audio.html#aiogram.types.inline_query_result_cached_audio.InlineQueryResultCachedAudio "aiogram.types.inline_query_result_cached_audio.InlineQueryResultCachedAudio")
    > - [`aiogram.types.inline_query_result_cached_document.InlineQueryResultCachedDocument`](inline_query_result_cached_document.html#aiogram.types.inline_query_result_cached_document.InlineQueryResultCachedDocument "aiogram.types.inline_query_result_cached_document.InlineQueryResultCachedDocument")
    > - [`aiogram.types.inline_query_result_cached_gif.InlineQueryResultCachedGif`](inline_query_result_cached_gif.html#aiogram.types.inline_query_result_cached_gif.InlineQueryResultCachedGif "aiogram.types.inline_query_result_cached_gif.InlineQueryResultCachedGif")
    > - [`aiogram.types.inline_query_result_cached_mpeg4_gif.InlineQueryResultCachedMpeg4Gif`](inline_query_result_cached_mpeg4_gif.html#aiogram.types.inline_query_result_cached_mpeg4_gif.InlineQueryResultCachedMpeg4Gif "aiogram.types.inline_query_result_cached_mpeg4_gif.InlineQueryResultCachedMpeg4Gif")
    > - [`aiogram.types.inline_query_result_cached_photo.InlineQueryResultCachedPhoto`](inline_query_result_cached_photo.html#aiogram.types.inline_query_result_cached_photo.InlineQueryResultCachedPhoto "aiogram.types.inline_query_result_cached_photo.InlineQueryResultCachedPhoto")
    > - [`aiogram.types.inline_query_result_cached_sticker.InlineQueryResultCachedSticker`](inline_query_result_cached_sticker.html#aiogram.types.inline_query_result_cached_sticker.InlineQueryResultCachedSticker "aiogram.types.inline_query_result_cached_sticker.InlineQueryResultCachedSticker")
    > - [`aiogram.types.inline_query_result_cached_video.InlineQueryResultCachedVideo`](inline_query_result_cached_video.html#aiogram.types.inline_query_result_cached_video.InlineQueryResultCachedVideo "aiogram.types.inline_query_result_cached_video.InlineQueryResultCachedVideo")
    > - [`aiogram.types.inline_query_result_cached_voice.InlineQueryResultCachedVoice`](inline_query_result_cached_voice.html#aiogram.types.inline_query_result_cached_voice.InlineQueryResultCachedVoice "aiogram.types.inline_query_result_cached_voice.InlineQueryResultCachedVoice")
    > - [`aiogram.types.inline_query_result_article.InlineQueryResultArticle`](inline_query_result_article.html#aiogram.types.inline_query_result_article.InlineQueryResultArticle "aiogram.types.inline_query_result_article.InlineQueryResultArticle")
    > - [`aiogram.types.inline_query_result_audio.InlineQueryResultAudio`](inline_query_result_audio.html#aiogram.types.inline_query_result_audio.InlineQueryResultAudio "aiogram.types.inline_query_result_audio.InlineQueryResultAudio")
    > - [`aiogram.types.inline_query_result_contact.InlineQueryResultContact`](inline_query_result_contact.html#aiogram.types.inline_query_result_contact.InlineQueryResultContact "aiogram.types.inline_query_result_contact.InlineQueryResultContact")
    > - [`aiogram.types.inline_query_result_game.InlineQueryResultGame`](inline_query_result_game.html#aiogram.types.inline_query_result_game.InlineQueryResultGame "aiogram.types.inline_query_result_game.InlineQueryResultGame")
    > - [`aiogram.types.inline_query_result_document.InlineQueryResultDocument`](inline_query_result_document.html#aiogram.types.inline_query_result_document.InlineQueryResultDocument "aiogram.types.inline_query_result_document.InlineQueryResultDocument")
    > - [`aiogram.types.inline_query_result_gif.InlineQueryResultGif`](inline_query_result_gif.html#aiogram.types.inline_query_result_gif.InlineQueryResultGif "aiogram.types.inline_query_result_gif.InlineQueryResultGif")
    > - [`aiogram.types.inline_query_result_location.InlineQueryResultLocation`](inline_query_result_location.html#aiogram.types.inline_query_result_location.InlineQueryResultLocation "aiogram.types.inline_query_result_location.InlineQueryResultLocation")
    > - [`aiogram.types.inline_query_result_mpeg4_gif.InlineQueryResultMpeg4Gif`](inline_query_result_mpeg4_gif.html#aiogram.types.inline_query_result_mpeg4_gif.InlineQueryResultMpeg4Gif "aiogram.types.inline_query_result_mpeg4_gif.InlineQueryResultMpeg4Gif")
    > - [`aiogram.types.inline_query_result_photo.InlineQueryResultPhoto`](inline_query_result_photo.html#aiogram.types.inline_query_result_photo.InlineQueryResultPhoto "aiogram.types.inline_query_result_photo.InlineQueryResultPhoto")
    > - [`aiogram.types.inline_query_result_venue.InlineQueryResultVenue`](inline_query_result_venue.html#aiogram.types.inline_query_result_venue.InlineQueryResultVenue "aiogram.types.inline_query_result_venue.InlineQueryResultVenue")
    > - [`aiogram.types.inline_query_result_video.InlineQueryResultVideo`](inline_query_result_video.html#aiogram.types.inline_query_result_video.InlineQueryResultVideo "aiogram.types.inline_query_result_video.InlineQueryResultVideo")
    > - [`aiogram.types.inline_query_result_voice.InlineQueryResultVoice`](inline_query_result_voice.html#aiogram.types.inline_query_result_voice.InlineQueryResultVoice "aiogram.types.inline_query_result_voice.InlineQueryResultVoice")

    **Note:** All URLs passed in inline query results will be available to end users and therefore must be assumed to be **public**.

    Source: <https://core.telegram.org/bots/api#inlinequeryresult>
