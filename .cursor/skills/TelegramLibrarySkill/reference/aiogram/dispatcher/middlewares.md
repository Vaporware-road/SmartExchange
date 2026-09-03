# Middlewares

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/middlewares.html](https://docs.aiogram.dev/en/latest/dispatcher/middlewares.html)

**aiogram** provides powerful mechanism for customizing event handlers via middlewares.

Middlewares in bot framework seems like Middlewares mechanism in web-frameworks
like [aiohttp](https://docs.aiohttp.org/en/stable/web_advanced.html#aiohttp-web-middlewares),
[fastapi](https://fastapi.tiangolo.com/tutorial/middleware/),
[Django](https://docs.djangoproject.com/en/3.0/topics/http/middleware/) or etc.)
with small difference - here is implemented two layers of middlewares (before and after filters).

Note

Middleware is function that triggered on every event received from
Telegram Bot API in many points on processing pipeline.

## Base theory

As many books and other literature in internet says:

> Middleware is reusable software that leverages patterns and frameworks to bridge
> the gap between the functional requirements of applications and the underlying operating systems,
> network protocol stacks, and databases.

Middleware can modify, extend or reject processing event in many places of pipeline.

## Basics

Middleware instance can be applied for every type of Telegram Event (Update, Message, etc.) in two places

1. Outer scope - before processing filters (`<router>.<event>.outer_middleware(...)`)
2. Inner scope - after processing filters but before handler (`<router>.<event>.middleware(...)`)

Attention

Middleware should be subclass of `BaseMiddleware` (`from aiogram import BaseMiddleware`) or any async callable

## Arguments specification

*class* aiogram.dispatcher.middlewares.base.BaseMiddleware
:   Bases: `ABC`

    Generic middleware class

    *abstract async* __call__(*handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]]*, *event: TelegramObject*, *data: dict[str, Any]*) → Any
    :   Execute middleware

        Parameters:
        :   - **handler** – Wrapped handler in middlewares chain
            - **event** – Incoming event (Subclass of `aiogram.types.base.TelegramObject`)
            - **data** – Contextual data. Will be mapped to handler arguments

        Returns:
        :   `Any`

## Examples

Danger

Middleware should always call `await handler(event, data)` to propagate event for next middleware/handler.
If you want to stop processing event in middleware you should not call `await handler(event, data)`.

### Class-based

```
from aiogram import BaseMiddleware
from aiogram.types import Message

class CounterMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        self.counter += 1
        data['counter'] = self.counter
        return await handler(event, data)
```

and then

```
router = Router()
router.message.middleware(CounterMiddleware())
```

### Function-based

```
@dispatcher.update.outer_middleware()
async def database_transaction_middleware(
    handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
    event: Update,
    data: Dict[str, Any]
) -> Any:
    async with database.transaction():
        return await handler(event, data)
```

## Facts

1. Middlewares from outer scope will be called on every incoming event
2. Middlewares from inner scope will be called only when filters pass
3. Inner middlewares is always calls for [`aiogram.types.update.Update`](../api/types/update.html#aiogram.types.update.Update "aiogram.types.update.Update") event type in due to all incoming updates going to specific event type handler through built in update handler
