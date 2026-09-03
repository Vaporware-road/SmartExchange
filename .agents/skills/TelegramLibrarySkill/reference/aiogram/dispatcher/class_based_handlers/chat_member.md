# ChatMemberHandler

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/chat_member.html](https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/chat_member.html)

There is base class for chat member updated events.

## Simple usage

```
from aiogram.handlers import ChatMemberHandler

...

@router.chat_member()
@router.my_chat_member()
class MyHandler(ChatMemberHandler):
    async def handle(self) -> Any: ...
```

## Extension

This base handler is subclass of [BaseHandler](base.html#cbh-base-handler) with some extensions:

- `self.chat` is alias for `self.event.chat`
