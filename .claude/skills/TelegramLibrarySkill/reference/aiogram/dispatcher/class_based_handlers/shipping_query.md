# ShippingQueryHandler

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/shipping_query.html](https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/shipping_query.html)

There is base class for callback query handlers.

## Simple usage

```
from aiogram.handlers import ShippingQueryHandler

...

@router.shipping_query()
class MyHandler(ShippingQueryHandler):
    async def handle(self) -> Any: ...
```

## Extension

This base handler is subclass of [BaseHandler](base.html#cbh-base-handler) with some extensions:

- `self.from_user` is alias for `self.event.from_user`
