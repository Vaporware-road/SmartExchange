# getWebhookInfo

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_webhook_info.html](https://docs.aiogram.dev/en/latest/api/methods/get_webhook_info.html)

Returns: `WebhookInfo`

*class* aiogram.methods.get_webhook_info.GetWebhookInfo(*\*\*extra_data: Any*)
:   Use this method to get current webhook status. Requires no parameters. On success, returns a [`aiogram.types.webhook_info.WebhookInfo`](../types/webhook_info.html#aiogram.types.webhook_info.WebhookInfo "aiogram.types.webhook_info.WebhookInfo") object. If the bot is using [`aiogram.methods.get_updates.GetUpdates`](get_updates.html#aiogram.methods.get_updates.GetUpdates "aiogram.methods.get_updates.GetUpdates"), will return an object with the *url* field empty.

    Source: <https://core.telegram.org/bots/api#getwebhookinfo>

## Usage

### As bot method

```
result: WebhookInfo = await bot.get_webhook_info(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_webhook_info import GetWebhookInfo`
- alias: `from aiogram.methods import GetWebhookInfo`

#### With specific bot

```
result: WebhookInfo = await bot(GetWebhookInfo(...))
```
