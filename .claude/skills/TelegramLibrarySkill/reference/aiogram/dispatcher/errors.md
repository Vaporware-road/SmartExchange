# Errors

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/errors.html](https://docs.aiogram.dev/en/latest/dispatcher/errors.html)

## Handling errors

Is recommended way that you should use errors inside handlers using try-except block,
but in common cases you can use global errors handler at router or dispatcher level.

If you specify errors handler for router - it will be used for all handlers inside this router.

If you specify errors handler for dispatcher - it will be used for all handlers inside all routers.

```
@router.error(ExceptionTypeFilter(MyCustomException), F.update.message.as_("message"))
async def handle_my_custom_exception(event: ErrorEvent, message: Message):
    # do something with error
    await message.answer("Oops, something went wrong!")

@router.error()
async def error_handler(event: ErrorEvent):
    logger.critical("Critical error caused by %s", event.exception, exc_info=True)
    # do something with error
    ...
```

## ErrorEvent

*class* aiogram.types.error_event.ErrorEvent(*\**, *update: [Update](../api/types/update.html#aiogram.types.update.Update "aiogram.types.update.Update")*, *exception: Exception*, *\*\*extra_data: Any*)
:   Internal event, should be used to receive errors while processing Updates from Telegram

    Source: <https://core.telegram.org/bots/api#error-event>

    update*: [Update](../api/types/update.html#aiogram.types.update.Update "aiogram.types.update.Update")*
    :   Received update

    exception*: Exception*
    :   Exception

## Error types

*exception* aiogram.exceptions.AiogramError
:   Base exception for all aiogram errors.

*exception* aiogram.exceptions.DetailedAiogramError(*message: str*)
:   Base exception for all aiogram errors with detailed message.

*exception* aiogram.exceptions.CallbackAnswerException
:   Exception for callback answer.

*exception* aiogram.exceptions.SceneException
:   Exception for scenes.

*exception* aiogram.exceptions.UnsupportedKeywordArgument(*message: str*)
:   Exception raised when a keyword argument is passed as filter.

*exception* aiogram.exceptions.TelegramAPIError(*method: TelegramMethod*, *message: str*)
:   Base exception for all Telegram API errors.

*exception* aiogram.exceptions.TelegramNetworkError(*method: TelegramMethod*, *message: str*)
:   Base exception for all Telegram network errors.

*exception* aiogram.exceptions.TelegramRetryAfter(*method: TelegramMethod*, *message: str*, *retry_after: int*)
:   Exception raised when flood control exceeds.

*exception* aiogram.exceptions.TelegramMigrateToChat(*method: TelegramMethod*, *message: str*, *migrate_to_chat_id: int*)
:   Exception raised when chat has been migrated to a supergroup.

*exception* aiogram.exceptions.TelegramBadRequest(*method: TelegramMethod*, *message: str*)
:   Exception raised when request is malformed.

*exception* aiogram.exceptions.TelegramNotFound(*method: TelegramMethod*, *message: str*)
:   Exception raised when chat, message, user, etc. not found.

*exception* aiogram.exceptions.TelegramConflictError(*method: TelegramMethod*, *message: str*)
:   Exception raised when bot token is already used by another application in polling mode.

*exception* aiogram.exceptions.TelegramUnauthorizedError(*method: TelegramMethod*, *message: str*)
:   Exception raised when bot token is invalid.

*exception* aiogram.exceptions.TelegramForbiddenError(*method: TelegramMethod*, *message: str*)
:   Exception raised when bot is kicked from chat or etc.

*exception* aiogram.exceptions.TelegramServerError(*method: TelegramMethod*, *message: str*)
:   Exception raised when Telegram server returns 5xx error.

*exception* aiogram.exceptions.RestartingTelegram(*method: TelegramMethod*, *message: str*)
:   Exception raised when Telegram server is restarting.

    It seems like this error is not used by Telegram anymore,
    but it’s still here for backward compatibility.

    Currently, you should expect that Telegram can raise RetryAfter (with timeout 5 seconds)
    :   error instead of this one.

*exception* aiogram.exceptions.TelegramEntityTooLarge(*method: TelegramMethod*, *message: str*)
:   Exception raised when you are trying to send a file that is too large.

*exception* aiogram.exceptions.ClientDecodeError(*message: str*, *original: Exception*, *data: Any*)
:   Exception raised when client can’t decode response. (Malformed response, etc.)

*exception* aiogram.exceptions.DataNotDictLikeError(*message: str*)
:   Exception raised when data is not dict-like.
