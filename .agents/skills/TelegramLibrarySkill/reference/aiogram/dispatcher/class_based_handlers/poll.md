# PollHandler

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/poll.html](https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/poll.html)

There is base class for poll handlers.

## Simple usage

```
from aiogram.handlers import PollHandler

...

@router.poll()
class MyHandler(PollHandler):
    async def handle(self) -> Any: ...
```

## Extension

This base handler is subclass of [BaseHandler](base.html#cbh-base-handler) with some extensions:

- `self.question` is alias for `self.event.question`
- `self.options` is alias for `self.event.options`
