# ChosenInlineResultHandler

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/chosen_inline_result.html](https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/chosen_inline_result.html)

There is base class for chosen inline result handlers.

## Simple usage

```
from aiogram.handlers import ChosenInlineResultHandler

...

@router.chosen_inline_result()
class MyHandler(ChosenInlineResultHandler):
    async def handle(self) -> Any: ...
```

## Extension

This base handler is subclass of [BaseHandler](base.html#cbh-base-handler) with some extensions:

- `self.chat` is alias for `self.event.chat`
- `self.from_user` is alias for `self.event.from_user`
