# Webhook

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/webhook.html](https://docs.aiogram.dev/en/latest/dispatcher/webhook.html)

Telegram Bot API supports webhook.
If you set webhook for your bot, Telegram will send updates to the specified url.
You can use [`aiogram.methods.set_webhook.SetWebhook()`](../api/methods/set_webhook.html#aiogram.methods.set_webhook.SetWebhook "aiogram.methods.set_webhook.SetWebhook") method to specify a url
and receive incoming updates on it.

Note

If you use webhook, you can’t use long polling at the same time.

Before start i’ll recommend you to read [official Telegram’s documentation about webhook](https://core.telegram.org/bots/webhooks)

After you read it, you can start to read this section.

Generally to use webhook with aiogram you should use any async web framework.
By out of the box aiogram has an aiohttp integration, so we’ll use it.

Note

You can use any async web framework you want, but you should write your own integration if you don’t use aiohttp.

## aiohttp integration

Out of the box aiogram has aiohttp integration, so you can use it.

Here is available few ways to do it using different implementations of the webhook controller:

- [`aiogram.webhook.aiohttp_server.BaseRequestHandler`](#aiogram.webhook.aiohttp_server.BaseRequestHandler "aiogram.webhook.aiohttp_server.BaseRequestHandler") - Abstract class for aiohttp webhook controller
- [`aiogram.webhook.aiohttp_server.SimpleRequestHandler`](#aiogram.webhook.aiohttp_server.SimpleRequestHandler "aiogram.webhook.aiohttp_server.SimpleRequestHandler") - Simple webhook controller, uses single Bot instance
- [`aiogram.webhook.aiohttp_server.TokenBasedRequestHandler`](#aiogram.webhook.aiohttp_server.TokenBasedRequestHandler "aiogram.webhook.aiohttp_server.TokenBasedRequestHandler") - Token based webhook controller, uses multiple Bot instances and tokens

You can use it as is or inherit from it and override some methods.

*class* aiogram.webhook.aiohttp_server.BaseRequestHandler(*dispatcher: [Dispatcher](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher")*, *handle_in_background: bool = False*, *\*\*data: Any*)
:   __init__(*dispatcher: [Dispatcher](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher")*, *handle_in_background: bool = False*, *\*\*data: Any*) → None
    :   Base handler that helps to handle incoming request from aiohttp
        and propagate it to the Dispatcher

        Parameters:
        :   - **dispatcher** – instance of [`aiogram.dispatcher.dispatcher.Dispatcher`](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher")
            - **handle_in_background** – immediately responds to the Telegram instead of
              a waiting end of a handler process

    register(*app: Application*, */*, *path: str*, *\*\*kwargs: Any*) → None
    :   Register route and shutdown callback

        Parameters:
        :   - **app** – instance of aiohttp Application
            - **path** – route path
            - **kwargs**

    *abstract async* resolve_bot(*request: Request*) → Bot
    :   This method should be implemented in subclasses of this class.

        Resolve Bot instance from request.

        Parameters:
        :   **request**

        Returns:
        :   Bot instance

*class* aiogram.webhook.aiohttp_server.SimpleRequestHandler(*dispatcher: [Dispatcher](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher")*, *bot: Bot*, *handle_in_background: bool = True*, *secret_token: str | None = None*, *\*\*data: Any*)
:   __init__(*dispatcher: [Dispatcher](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher")*, *bot: Bot*, *handle_in_background: bool = True*, *secret_token: str | None = None*, *\*\*data: Any*) → None
    :   Handler for single Bot instance

        Parameters:
        :   - **dispatcher** – instance of [`aiogram.dispatcher.dispatcher.Dispatcher`](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher")
            - **handle_in_background** – immediately responds to the Telegram instead of
              a waiting end of handler process
            - **bot** – instance of `aiogram.client.bot.Bot`

    *async* close() → None
    :   Close bot session

    register(*app: Application*, */*, *path: str*, *\*\*kwargs: Any*) → None
    :   Register route and shutdown callback

        Parameters:
        :   - **app** – instance of aiohttp Application
            - **path** – route path
            - **kwargs**

    *async* resolve_bot(*request: Request*) → Bot
    :   This method should be implemented in subclasses of this class.

        Resolve Bot instance from request.

        Parameters:
        :   **request**

        Returns:
        :   Bot instance

*class* aiogram.webhook.aiohttp_server.TokenBasedRequestHandler(*dispatcher: [Dispatcher](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher")*, *handle_in_background: bool = True*, *bot_settings: dict[str, Any] | None = None*, *\*\*data: Any*)
:   __init__(*dispatcher: [Dispatcher](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher")*, *handle_in_background: bool = True*, *bot_settings: dict[str, Any] | None = None*, *\*\*data: Any*) → None
    :   Handler that supports multiple bots the context will be resolved
        from path variable ‘bot_token’

        Note

        This handler is not recommended in due to token is available in URL
        and can be logged by reverse proxy server or other middleware.

        Parameters:
        :   - **dispatcher** – instance of [`aiogram.dispatcher.dispatcher.Dispatcher`](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher")
            - **handle_in_background** – immediately responds to the Telegram instead of
              a waiting end of handler process
            - **bot_settings** – kwargs that will be passed to new Bot instance

    register(*app: Application*, */*, *path: str*, *\*\*kwargs: Any*) → None
    :   Validate path, register route and shutdown callback

        Parameters:
        :   - **app** – instance of aiohttp Application
            - **path** – route path
            - **kwargs**

    *async* resolve_bot(*request: Request*) → Bot
    :   Get bot token from a path and create or get from cache Bot instance

        Parameters:
        :   **request**

        Returns:

### Security

Telegram supports two methods to verify incoming requests that they are from Telegram:

#### Using a secret token

When you set webhook, you can specify a secret token and then use it to verify incoming requests.

#### Using IP filtering

You can specify a list of IP addresses from which you expect incoming requests, and then use it to verify incoming requests.

It can be acy using firewall rules or nginx configuration or middleware on application level.

So, aiogram has an implementation of the IP filtering middleware for aiohttp.

aiogram IP filtering middleware reads the left-most IP address from X-Forwarded-For.

Warning

X-Forwarded-For is trustworthy only if all webhook traffic goes through a trusted reverse proxy that rewrites this header.
If your application is directly reachable from the Internet, this header can be forged.

For production deployments, use defense in depth:

- Always set and verify `X-Telegram-Bot-Api-Secret-Token`
- Restrict network access to the webhook endpoint (firewall, security groups, ACL)
- Ensure the backend app is not publicly reachable and accepts requests only from the trusted proxy

aiogram.webhook.aiohttp_server.ip_filter_middleware(*ip_filter: [IPFilter](#aiogram.webhook.security.IPFilter "aiogram.webhook.security.IPFilter")*) → Callable[[Request, Callable[[Request], Awaitable[StreamResponse]]], Awaitable[Any]]
:   Parameters:
    :   **ip_filter**

    Returns:

*class* aiogram.webhook.security.IPFilter(*ips: Sequence[str | IPv4Network | IPv4Address] | None = None*)
:   __init__(*ips: Sequence[str | IPv4Network | IPv4Address] | None = None*)

### Examples

#### Behind reverse proxy

In this example we’ll use aiohttp as web framework and nginx as reverse proxy.

```
"""
This example shows how to use webhook on behind of any reverse proxy (nginx, traefik, ingress etc.)
"""

import logging
import sys
from os import getenv

from aiohttp import web

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")

# Webserver settings
# bind localhost only to prevent any external access
WEB_SERVER_HOST = "127.0.0.1"
# Port for incoming request from reverse proxy. Should be any available port
WEB_SERVER_PORT = 8080

# Path to webhook route, on which Telegram will send requests
WEBHOOK_PATH = "/webhook"
# Secret key to validate requests from Telegram (optional)
WEBHOOK_SECRET = "my-secret"
# Base URL for webhook will be used to generate webhook URL for Telegram,
# in this example it is used public DNS with HTTPS support
BASE_WEBHOOK_URL = "https://aiogram.dev"

# All handlers should be attached to the Router (or Dispatcher)
router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@router.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")

async def on_startup(bot: Bot) -> None:
    # If you have a self-signed SSL certificate, then you will need to send a public
    # certificate to Telegram
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SECRET)

def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Register startup hook to initialize webhook
    dp.startup.register(on_startup)

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Create aiohttp.web.Application instance
    app = web.Application()

    # Create an instance of request handler,
    # aiogram has few implementations for different cases of usage
    # In this example we use SimpleRequestHandler which is designed to handle simple cases
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # And finally start webserver
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
```

When you use nginx as reverse proxy, you should set proxy_pass to your aiohttp server address.

```
location /webhook {
    proxy_set_header Host $http_host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_redirect off;
    proxy_buffering off;
    proxy_pass http://127.0.0.1:8080;
}
```

#### Without reverse proxy (not recommended)

In case without using reverse proxy, you can use aiohttp’s ssl context.

Also this example contains usage with self-signed certificate.

```
"""
This example shows how to use webhook with SSL certificate.
"""

import logging
import ssl
import sys
from os import getenv

from aiohttp import web

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, Message
from aiogram.utils.markdown import hbold
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")

# Webserver settings
# bind localhost only to prevent any external access
WEB_SERVER_HOST = "127.0.0.1"
# Port for incoming request from reverse proxy. Should be any available port
WEB_SERVER_PORT = 8080

# Path to webhook route, on which Telegram will send requests
WEBHOOK_PATH = "/webhook"
# Secret key to validate requests from Telegram (optional)
WEBHOOK_SECRET = "my-secret"
# Base URL for webhook will be used to generate webhook URL for Telegram,
# in this example it is used public address with TLS support
BASE_WEBHOOK_URL = "https://aiogram.dev"

# Path to SSL certificate and private key for self-signed certificate.
WEBHOOK_SSL_CERT = "/path/to/cert.pem"
WEBHOOK_SSL_PRIV = "/path/to/private.key"

# All handlers should be attached to the Router (or Dispatcher)
router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@router.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")

async def on_startup(bot: Bot) -> None:
    # In case when you have a self-signed SSL certificate, you need to send the certificate
    # itself to Telegram servers for validation purposes
    # (see https://core.telegram.org/bots/self-signed)
    # But if you have a valid SSL certificate, you SHOULD NOT send it to Telegram servers.
    await bot.set_webhook(
        f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}",
        certificate=FSInputFile(WEBHOOK_SSL_CERT),
        secret_token=WEBHOOK_SECRET,
    )

def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Register startup hook to initialize webhook
    dp.startup.register(on_startup)

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Create aiohttp.web.Application instance
    app = web.Application()

    # Create an instance of request handler,
    # aiogram has few implementations for different cases of usage
    # In this example we use SimpleRequestHandler which is designed to handle simple cases
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # Generate SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)

    # And finally start webserver
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT, ssl_context=context)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
```

## With using other web framework

You can pass incoming request to aiogram’s webhook controller from any web framework you want.

Read more about it in `aiogram.dispatcher.dispatcher.Dispatcher.feed_webhook_update()`
or [`aiogram.dispatcher.dispatcher.Dispatcher.feed_update()`](dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher.feed_update "aiogram.dispatcher.dispatcher.Dispatcher.feed_update") methods.

```
update = Update.model_validate(await request.json(), context={"bot": bot})
await dispatcher.feed_update(bot, update)
```

Note

If you want to use reply into webhook, you should check that result of the `feed_update`
methods is an instance of API method and build `multipart/form-data`
or `application/json` response body manually.
