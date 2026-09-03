# Router

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/router.html](https://docs.aiogram.dev/en/latest/dispatcher/router.html)

Usage:

```
from aiogram import Router
from aiogram.types import Message

my_router = Router(name=__name__)

@my_router.message()
async def message_handler(message: Message) -> Any:
    await message.answer('Hello from my router!')
```

*class* aiogram.dispatcher.router.Router(*\**, *name: str | None = None*)
:   Bases: `object`

    Router can route update, and it nested update types like messages, callback query,
    polls and all other event types.

    Event handlers can be registered in observer by two ways:

    - By observer method - `router.<event_type>.register(handler, <filters, ...>)`
    - By decorator - `@router.<event_type>(<filters, ...>)`

    __init__(*\**, *name: str | None = None*) → None
    :   Parameters:
        :   **name** – Optional router name, can be useful for debugging

    include_router(*router: [Router](#aiogram.dispatcher.router.Router "aiogram.dispatcher.router.Router")*) → [Router](#aiogram.dispatcher.router.Router "aiogram.dispatcher.router.Router")
    :   Attach another router.

        Parameters:
        :   **router**

        Returns:

    include_routers(*\*routers: [Router](#aiogram.dispatcher.router.Router "aiogram.dispatcher.router.Router")*) → None
    :   Attach multiple routers.

        Parameters:
        :   **routers**

        Returns:

    resolve_used_update_types(*skip_events: set[str] | None = None*) → list[str]
    :   Resolve registered event names

        Is useful for getting updates only for registered event types.

        Parameters:
        :   **skip_events** – skip specified event names

        Returns:
        :   sorted list of registered names

## Event observers

Warning

All handlers always should be asynchronous.
The name of the handler function is not important. The event argument name is also not important but it is recommended to not overlap the name with contextual data in due to function can not accept two arguments with the same name.

Here is the list of available observers and examples of how to register handlers

In these examples only decorator-style registering handlers are used, but if you don’t like @decorators just use `<event type>.register(...)` method instead.

### Message

Attention

Be attentive with filtering this event

You should expect that this event can be with different sets of attributes in different cases

(For example text, sticker and document are always of different content types of message)

Recommended way to check field availability before usage, for example via [magic filter](filters/magic_filters.html#magic-filters):
`F.text` to handle text, `F.sticker` to handle stickers only and etc.

```
@router.message()
async def message_handler(message: types.Message) -> Any: pass
```

### Edited message

```
@router.edited_message()
async def edited_message_handler(edited_message: types.Message) -> Any: pass
```

### Channel post

```
@router.channel_post()
async def channel_post_handler(channel_post: types.Message) -> Any: pass
```

### Edited channel post

```
@router.edited_channel_post()
async def edited_channel_post_handler(edited_channel_post: types.Message) -> Any: pass
```

### Inline query

```
@router.inline_query()
async def inline_query_handler(inline_query: types.InlineQuery) -> Any: pass
```

### Chosen inline query

```
@router.chosen_inline_result()
async def chosen_inline_result_handler(chosen_inline_result: types.ChosenInlineResult) -> Any: pass
```

### Callback query

```
@router.callback_query()
async def callback_query_handler(callback_query: types.CallbackQuery) -> Any: pass
```

### Shipping query

```
@router.shipping_query()
async def shipping_query_handler(shipping_query: types.ShippingQuery) -> Any: pass
```

### Pre checkout query

```
@router.pre_checkout_query()
async def pre_checkout_query_handler(pre_checkout_query: types.PreCheckoutQuery) -> Any: pass
```

### Poll

```
@router.poll()
async def poll_handler(poll: types.Poll) -> Any: pass
```

### Poll answer

```
@router.poll_answer()
async def poll_answer_handler(poll_answer: types.PollAnswer) -> Any: pass
```

### My chat member

```
@router.my_chat_member()
async def my_chat_member_handler(my_chat_member: types.ChatMemberUpdated) -> Any: pass
```

### Chat member

```
@router.chat_member()
async def chat_member_handler(chat_member: types.ChatMemberUpdated) -> Any: pass
```

### Chat join request

```
@router.chat_join_request()
async def chat_join_request_handler(chat_join_request: types.ChatJoinRequest) -> Any: pass
```

### Message reaction

```
@router.message_reaction()
async def message_reaction_handler(message_reaction: types.MessageReactionUpdated) -> Any: pass
```

### Message reaction count

```
@router.message_reaction_count()
async def message_reaction_count_handler(message_reaction_count: types.MessageReactionCountUpdated) -> Any: pass
```

### Chat boost

```
@router.chat_boost()
async def chat_boost_handler(chat_boost: types.ChatBoostUpdated) -> Any: pass
```

### Remove chat boost

```
@router.removed_chat_boost()
async def removed_chat_boost_handler(removed_chat_boost: types.ChatBoostRemoved) -> Any: pass
```

### Errors

```
@router.errors()
async def error_handler(exception: types.ErrorEvent) -> Any: pass
```

Is useful for handling errors from other handlers, error event described [here](errors.html#error-event)

## Nested routers

Warning

Routers by the way can be nested to an another routers with some limitations:
:   1. Router **CAN NOT** include itself
    1. Routers **CAN NOT** be used for circular including (router 1 include router 2, router 2 include router 3, router 3 include router 1)

Example:

module_1.py

```
router2 = Router()

@router2.message()
...
```

module_2.py

```
from module_2 import router2

router1 = Router()
router1.include_router(router2)
```

### Update

```
@dispatcher.update()
async def message_handler(update: types.Update) -> Any: pass
```

Warning

The only root Router (Dispatcher) can handle this type of event.

Note

Dispatcher already has default handler for this event type, so you can use it for handling all updates that are not handled by any other handlers.

### How it works?

For example, dispatcher has 2 routers, the last router also has one nested router:

In this case update propagation flow will have form:
