# MessageHandler

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/message.html](https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/message.html)

There is base class for message handlers.

## Simple usage

```
from aiogram.handlers import MessageHandler

...

@router.message()
class MyHandler(MessageHandler):
    async def handle(self) -> Any:
        return SendMessage(chat_id=self.chat.id, text="PASS")
```

## Extension

This base handler is subclass of [BaseHandler](base.html#cbh-base-handler) with some extensions:

- `self.chat` is alias for `self.event.chat`
- `self.from_user` is alias for `self.event.from_user`
