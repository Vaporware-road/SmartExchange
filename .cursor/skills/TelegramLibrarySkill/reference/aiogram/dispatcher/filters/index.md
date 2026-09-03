# Filtering events

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/filters/index.html](https://docs.aiogram.dev/en/latest/dispatcher/filters/index.html)

Filters is needed for routing updates to the specific handler.
Searching of handler is always stops on first match set of filters are pass.
By default, all handlers has empty set of filters, so all updates will be passed to first handler that has empty set of filters.

*aiogram* has some builtin useful filters or you can write own filters.

## Builtin filters

Here is list of builtin filters:

- [Command](command.html)
- [ChatMemberUpdated](chat_member_updated.html)
- [Magic filters](magic_filters.html)
- [MagicData](magic_data.html)
- [Callback Data Factory & Filter](callback_data.html)
- [Exceptions](exception.html)

## Writing own filters

Filters can be:

- Asynchronous function (`async def my_filter(*args, **kwargs): pass`)
- Synchronous function (`def my_filter(*args, **kwargs): pass`)
- Anonymous function (`lambda event: True`)
- Any awaitable object
- Subclass of [`aiogram.filters.base.Filter`](#aiogram.filters.base.Filter "aiogram.filters.base.Filter")
- Instances of [MagicFilter](magic_filters.html#magic-filters)

and should return bool or dict.
If the dictionary is passed as result of filter - resulted data will be propagated to the next
filters and handler as keywords arguments.

### Base class for own filters

*class* aiogram.filters.base.Filter
:   If you want to register own filters like builtin filters you will need to write subclass
    of this class with overriding the `__call__`
    method and adding filter attributes.

    *abstract async* __call__(*\*args: Any*, *\*\*kwargs: Any*) → bool | dict[str, Any]
    :   This method should be overridden.

        Accepts incoming event and should return boolean or dict.

        Returns:
        :   `bool` or `dict[str, Any]`

    update_handler_flags(*flags: dict[str, Any]*) → None
    :   Also if you want to extend handler flags with using this filter
        you should implement this method

        Parameters:
        :   **flags** – existing flags, can be updated directly

### Own filter example

For example if you need to make simple text filter:

```
from aiogram import Router
from aiogram.filters import Filter
from aiogram.types import Message

router = Router()

class MyFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        return message.text == self.my_text

@router.message(MyFilter("hello"))
async def my_handler(message: Message) -> None: ...
```

## Combining Filters

In general, all filters can be combined in two ways

### Recommended way

If you specify multiple filters in a row, it will be checked with an “and” condition:

```
@<router>.message(F.text.startswith("show"), F.text.endswith("example"))
```

Also, if you want to use two alternative ways to run the same handler (“or” condition)
you can register the handler twice or more times as you like

```
@<router>.message(F.text == "hi")
@<router>.message(CommandStart())
```

Also sometimes you will need to invert the filter result, for example you have an *IsAdmin* filter
and you want to check if the user is not an admin

```
@<router>.message(~IsAdmin())
```

### Another possible way

An alternative way is to combine using special functions (`and_f()`, `or_f()`, `invert_f()` from `aiogram.filters` module):

```
and_f(F.text.startswith("show"), F.text.endswith("example"))
or_f(F.text(text="hi"), CommandStart())
invert_f(IsAdmin())
and_f(<A>, or_f(<B>, <C>))
```
