# Deep Linking

> Source: [https://docs.aiogram.dev/en/latest/utils/deep_linking.html](https://docs.aiogram.dev/en/latest/utils/deep_linking.html)

Telegram bots have a deep linking mechanism, that allows for passing
additional parameters to the bot on startup. It could be a command that
launches the bot — or an auth token to connect the user’s Telegram
account to their account on some external service.

You can read detailed description in the source:
<https://core.telegram.org/bots/features#deep-linking>

We have added some utils to get deep links more handy.

## Examples

### Basic link example

```
from aiogram.utils.deep_linking import create_start_link

link = await create_start_link(bot, 'foo')

# result: 'https://t.me/MyBot?start=foo'
```

### Encoded link

```
from aiogram.utils.deep_linking import create_start_link

link = await create_start_link(bot, 'foo', encode=True)
# result: 'https://t.me/MyBot?start=Zm9v'
```

### Decode it back

```
from aiogram.utils.deep_linking import decode_payload
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message

@router.message(CommandStart(deep_link=True))
async def handler(message: Message, command: CommandObject):
    args = command.args
    payload = decode_payload(args)
    await message.answer(f"Your payload: {payload}")
```

## References

*async* aiogram.utils.deep_linking.create_start_link(*bot: Bot*, *payload: str*, *encode: bool = False*, *encoder: Callable[[bytes], bytes] | None = None*) → str
:   Create ‘start’ deep link with your payload.

    If you need to encode payload or pass special characters - set encode as True

    Parameters:
    :   - **bot** – bot instance
        - **payload** – args passed with /start
        - **encode** – encode payload with base64url or custom encoder
        - **encoder** – custom encoder callable

    Returns:
    :   link

*async* aiogram.utils.deep_linking.create_startgroup_link(*bot: Bot*, *payload: str*, *encode: bool = False*, *encoder: Callable[[bytes], bytes] | None = None*) → str
:   Create ‘startgroup’ deep link with your payload.

    If you need to encode payload or pass special characters - set encode as True

    Parameters:
    :   - **bot** – bot instance
        - **payload** – args passed with /start
        - **encode** – encode payload with base64url or custom encoder
        - **encoder** – custom encoder callable

    Returns:
    :   link

*async* aiogram.utils.deep_linking.create_startapp_link(*bot: Bot*, *payload: str*, *encode: bool = False*, *app_name: str | None = None*, *encoder: Callable[[bytes], bytes] | None = None*) → str
:   Create ‘startapp’ deep link with your payload.

    If you need to encode payload or pass special characters - set encode as True

    **Read more**:

    - [Main Mini App links](https://core.telegram.org/api/links#main-mini-app-links)
    - [Direct mini app links](https://core.telegram.org/api/links#direct-mini-app-links)

    Parameters:
    :   - **bot** – bot instance
        - **payload** – args passed with /start
        - **encode** – encode payload with base64url or custom encoder
        - **app_name** – if you want direct mini app link
        - **encoder** – custom encoder callable

    Returns:
    :   link

aiogram.utils.deep_linking.decode_payload(*payload: str*, *decoder: Callable[[bytes], bytes] | None = None*) → str
:   Decode URL-safe base64url payload with decoder.
