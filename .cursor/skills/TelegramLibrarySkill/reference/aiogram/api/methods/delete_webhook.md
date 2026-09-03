# deleteWebhook

> Source: [https://docs.aiogram.dev/en/latest/api/methods/delete_webhook.html](https://docs.aiogram.dev/en/latest/api/methods/delete_webhook.html)

Returns: `bool`

*class* aiogram.methods.delete_webhook.DeleteWebhook(*\**, *drop_pending_updates: bool | None = None*, *\*\*extra_data: Any*)
:   Use this method to remove webhook integration if you decide to switch back to [`aiogram.methods.get_updates.GetUpdates`](get_updates.html#aiogram.methods.get_updates.GetUpdates "aiogram.methods.get_updates.GetUpdates"). Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#deletewebhook>

    drop_pending_updates*: bool | None*
    :   Pass `True` to drop all pending updates

## Usage

### As bot method

```
result: bool = await bot.delete_webhook(...)
```

### Method as object

Imports:

- `from aiogram.methods.delete_webhook import DeleteWebhook`
- alias: `from aiogram.methods import DeleteWebhook`

#### With specific bot

```
result: bool = await bot(DeleteWebhook(...))
```

#### As reply into Webhook in handler

```
return DeleteWebhook(...)
```
