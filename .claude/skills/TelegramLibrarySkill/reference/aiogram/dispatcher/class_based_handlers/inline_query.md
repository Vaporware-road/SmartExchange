# InlineQueryHandler

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/inline_query.html](https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/inline_query.html)

There is base class for inline query handlers.

## Simple usage

```
from aiogram.handlers import InlineQueryHandler

...

@router.inline_query()
class MyHandler(InlineQueryHandler):
    async def handle(self) -> Any: ...
```

## Extension

This base handler is subclass of [BaseHandler](base.html#cbh-base-handler) with some extensions:

- `self.chat` is alias for `self.event.chat`
- `self.query` is alias for `self.event.query`
