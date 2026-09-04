# CallbackQueryHandler

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/callback_query.html](https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/callback_query.html)

*class* aiogram.handlers.callback_query.CallbackQueryHandler(*event: T*, *\*\*kwargs: Any*)
:   There is base class for callback query handlers.

    Example:
    :   ```
        from aiogram.handlers import CallbackQueryHandler

        ...

        @router.callback_query()
        class MyHandler(CallbackQueryHandler):
            async def handle(self) -> Any: ...
        ```

    *property* from_user*: [User](../../api/types/user.html#aiogram.types.user.User "aiogram.types.user.User")*
    :   Is alias for event.from_user

    *property* message*: [MaybeInaccessibleMessage](../../api/types/maybe_inaccessible_message.html#aiogram.types.maybe_inaccessible_message.MaybeInaccessibleMessage "aiogram.types.maybe_inaccessible_message.MaybeInaccessibleMessage") | None*
    :   Is alias for event.message

    *property* callback_data*: str | None*
    :   Is alias for event.data
