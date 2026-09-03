# Client session middlewares

> Source: [https://docs.aiogram.dev/en/latest/api/session/middleware.html](https://docs.aiogram.dev/en/latest/api/session/middleware.html)

In some cases you may want to add some middlewares to the client session to customize the behavior of the client.

Some useful cases that is:

- Log the outgoing requests
- Customize the request parameters
- Handle rate limiting errors and retry the request
- others …

So, you can do it using client session middlewares.
A client session middleware is a function (or callable class) that receives the request and the next middleware to call.
The middleware can modify the request and then call the next middleware to continue the request processing.

## How to register client session middleware?

### Register using register method

```
bot.session.middleware(RequestLogging(ignore_methods=[GetUpdates]))
```

### Register using decorator

```
@bot.session.middleware()
async def my_middleware(
    make_request: NextRequestMiddlewareType[TelegramType],
    bot: "Bot",
    method: TelegramMethod[TelegramType],
) -> Response[TelegramType]:
    # do something with request
    return await make_request(bot, method)
```

## Example

### Class based session middleware

```
 1class RequestLogging(BaseRequestMiddleware):
 2    def __init__(self, ignore_methods: list[type[TelegramMethod[Any]]] | None = None):
 3        """
 4        Middleware for logging outgoing requests
 5
 6        :param ignore_methods: methods to ignore in logging middleware
 7        """
 8        self.ignore_methods = ignore_methods or []
 9
10    async def __call__(
11        self,
12        make_request: NextRequestMiddlewareType[TelegramType],
13        bot: "Bot",
14        method: TelegramMethod[TelegramType],
15    ) -> Response[TelegramType]:
16        if type(method) not in self.ignore_methods:
17            loggers.middlewares.info(
18                "Make request with method=%r by bot id=%d",
19                type(method).__name__,
20                bot.id,
21            )
22        return await make_request(bot, method)
```

Note

this middleware is already implemented inside aiogram, so, if you want to use it you can
just import it `from aiogram.client.session.middlewares.request_logging import RequestLogging`

### Function based session middleware

```
async def __call__(
    self,
    make_request: NextRequestMiddlewareType[TelegramType],
    bot: "Bot",
    method: TelegramMethod[TelegramType],
) -> Response[TelegramType]:
    try:
        # do something with request
        return await make_request(bot, method)
    finally:
        # do something after request
```
