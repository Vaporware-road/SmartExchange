# ErrorHandler

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/error.html](https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/error.html)

There is base class for error handlers.

## Simple usage

```
from aiogram.handlers import ErrorHandler

...

@router.errors()
class MyHandler(ErrorHandler):
    async def handle(self) -> Any:
        log.exception(
            "Cause unexpected exception %s: %s",
            self.exception_name,
            self.exception_message
        )
```

## Extension

This base handler is subclass of [BaseHandler](base.html#cbh-base-handler) with some extensions:

- `self.exception_name` is alias for `self.event.__class__.__name__`
- `self.exception_message` is alias for `str(self.event)`
