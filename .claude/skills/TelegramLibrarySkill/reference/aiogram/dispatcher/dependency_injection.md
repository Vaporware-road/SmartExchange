# Dependency injection

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/dependency_injection.html](https://docs.aiogram.dev/en/latest/dispatcher/dependency_injection.html)

Dependency injection is a programming technique that makes a class independent of its dependencies.
It achieves that by decoupling the usage of an object from its creation.
This helps you to follow [SOLID’s](https://en.wikipedia.org/wiki/SOLID) dependency
inversion and single responsibility principles.

## How it works in aiogram

For each update [`aiogram.dispatcher.dispatcher.Dispatcher`](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher") passes handling context data.
Filters and middleware can also make changes to the context.

To access contextual data you should specify corresponding keyword parameter in handler or filter.
For example, to get `aiogram.fsm.context.FSMContext` we do it like that:

```
@router.message(ProfileCompletion.add_photo, F.photo)
async def add_photo(
    message: types.Message, bot: Bot, state: FSMContext
) -> Any:
    ... # do something with photo
```

## Injecting own dependencies

Aiogram provides several ways to complement / modify contextual data.

The first and easiest way is to simply specify the named arguments in
[`aiogram.dispatcher.dispatcher.Dispatcher`](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher") initialization, polling start methods
or [`aiogram.webhook.aiohttp_server.SimpleRequestHandler`](webhook.html#aiogram.webhook.aiohttp_server.SimpleRequestHandler "aiogram.webhook.aiohttp_server.SimpleRequestHandler") initialization if you use webhooks.

```
async def main() -> None:
    dp = Dispatcher(..., foo=42)
    return await dp.start_polling(
        bot, bar="Bazz"
    )
```

Analogy for webhook:

```
async def main() -> None:
    dp = Dispatcher(..., foo=42)
    handler = SimpleRequestHandler(dispatcher=dp, bot=bot, bar="Bazz")
    ... # starting webhook
```

[`aiogram.dispatcher.dispatcher.Dispatcher`](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher")’s workflow data also can be supplemented
by setting values as in a dictionary:

```
dp = Dispatcher(...)
dp["eggs"] = Spam()
```

The middlewares updates the context quite often.
You can read more about them on this page:

- [Middlewares](middlewares.html#middlewares)

The last way is to return a dictionary from the filter:

```
from typing import Any

from aiogram import Router
from aiogram.filters import Filter
from aiogram.types import Message, User

router = Router(name=__name__)

class HelloFilter(Filter):
    def __init__(self, name: str | None = None) -> None:
        self.name = name

    async def __call__(
        self,
        message: Message,
        event_from_user: User,
        # Filters also can accept keyword parameters like in handlers
    ) -> bool | dict[str, Any]:
        if message.text.casefold() == "hello":
            # Returning a dictionary that will update the context data
            return {"name": event_from_user.mention_html(name=self.name)}
        return False

@router.message(HelloFilter())
async def my_handler(
    message: Message,
    name: str,  # Now we can accept "name" as named parameter
) -> Any:
    return message.answer(f"Hello, {name}!")
```

…or using [MagicFilter](filters/magic_filters.html#magic-filters) with `.as_(...)` method.

## Using type hints

Note

Type-hinting middleware data is optional and is not required for the correct operation of the dispatcher.
However, it is recommended to use it to improve the readability of the code.

You can use type hints to specify the type of the context data in the middlewares, filters and handlers.

The default middleware data typed dict can be found in [`aiogram.dispatcher.middlewares.data.MiddlewareData`](#aiogram.dispatcher.middlewares.data.MiddlewareData "aiogram.dispatcher.middlewares.data.MiddlewareData").

In case when you have extended the context data, you can use the [`aiogram.dispatcher.middlewares.data.MiddlewareData`](#aiogram.dispatcher.middlewares.data.MiddlewareData "aiogram.dispatcher.middlewares.data.MiddlewareData") as a base class and specify the type hints for the new fields.

Warning

If you using type checking tools like mypy, you can experience warnings about that this type hint against Liskov substitution principle in due stricter type is not a subclass of `dict[str, Any]`.
This is a known issue and it is not a bug. You can ignore this warning or use `# type: ignore` comment.

Example of using type hints:

```
from aiogram.dispatcher.middlewares.data import MiddlewareData

class MyMiddlewareData(MiddlewareData, total=False):
    my_custom_value: int

class MyMessageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, MyMiddlewareData], Awaitable[Any]],
        event: Message,
        data: MyMiddlewareData,
    ) -> Any:
        bot = data["bot"]  # <-- IDE will show you that data has `bot` key and its type is `Bot`

        data["my_custom_value"] = bot.id * 42  # <-- IDE will show you that you can set `my_custom_value` key with int value and warn you if you try to set it with other type
        return await handler(event, data)
```

### Available context data type helpers

*class* aiogram.dispatcher.middlewares.data.MiddlewareData
:   Data passed to the handler by the middlewares.

    You can add your own data by extending this class.

    dispatcher*: [Dispatcher](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher")*

    bot*: Bot*

    bots*: NotRequired[list[Bot]]*

    event_update*: [Update](../api/types/update.html#aiogram.types.update.Update "aiogram.types.update.Update")*

    event_router*: [Router](router.html#aiogram.dispatcher.router.Router "aiogram.dispatcher.router.Router")*

    handler*: NotRequired[HandlerObject]*

    event_context*: EventContext*

    event_from_user*: NotRequired[[User](../api/types/user.html#aiogram.types.user.User "aiogram.types.user.User")]*

    event_chat*: NotRequired[[Chat](../api/types/chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat")]*

    event_thread_id*: NotRequired[int]*

    event_business_connection_id*: NotRequired[str]*

    fsm_storage*: [BaseStorage](finite_state_machine/storages.html#aiogram.fsm.storage.base.BaseStorage "aiogram.fsm.storage.base.BaseStorage")*

    state*: NotRequired[FSMContext]*

    raw_state*: NotRequired[str | None]*

*class* aiogram.dispatcher.middlewares.data.I18nData
:   I18n related data.

    Is not included by default, you need to add it to your own Data class if you need it.

    i18n*: I18n*
    :   I18n object.

    i18n_middleware*: [I18nMiddleware](../utils/i18n.html#aiogram.utils.i18n.middleware.I18nMiddleware "aiogram.utils.i18n.middleware.I18nMiddleware")*
    :   I18n middleware.
