# setWebhook

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_webhook.html](https://docs.aiogram.dev/en/latest/api/methods/set_webhook.html)

Returns: `bool`

*class* aiogram.methods.set_webhook.SetWebhook(*\**, *url: str*, *certificate: [InputFile](../types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile") | None = None*, *ip_address: str | None = None*, *max_connections: int | None = None*, *allowed_updates: list[str] | None = None*, *drop_pending_updates: bool | None = None*, *secret_token: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to specify a URL and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified URL, containing a JSON-serialized [`aiogram.types.update.Update`](../types/update.html#aiogram.types.update.Update "aiogram.types.update.Update"). In case of an unsuccessful request (a request with response [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) different from `2XY`), we will repeat the request and give up after a reasonable amount of attempts. Returns `True` on success.
    If you’d like to make sure that the webhook was set by you, you can specify secret data in the parameter *secret_token*. If specified, the request will contain a header ‘X-Telegram-Bot-Api-Secret-Token’ with the secret token as content.

    > **Notes**
    >
    > **1.** You will not be able to receive updates using [`aiogram.methods.get_updates.GetUpdates`](get_updates.html#aiogram.methods.get_updates.GetUpdates "aiogram.methods.get_updates.GetUpdates") for as long as an outgoing webhook is set up.
    >
    > **2.** To use a self-signed certificate, you need to upload your [public key certificate](https://core.telegram.org/bots/self-signed) using *certificate* parameter. Please upload as InputFile, sending a String will not work.
    >
    > **3.** Ports currently supported *for webhooks*: **443, 80, 88, 8443**.
    > If you’re having any trouble setting up webhooks, please check out this [amazing guide to webhooks](https://core.telegram.org/bots/webhooks).

    Source: <https://core.telegram.org/bots/api#setwebhook>

    url*: str*
    :   HTTPS URL to send updates to. Use an empty string to remove webhook integration

    certificate*: [InputFile](../types/input_file.html#aiogram.types.input_file.InputFile "aiogram.types.input_file.InputFile") | None*
    :   Upload your public key certificate so that the root certificate in use can be checked. See our [self-signed guide](https://core.telegram.org/bots/self-signed) for details

    ip_address*: str | None*
    :   The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS

    max_connections*: int | None*
    :   The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to *40*. Use lower values to limit the load on your bot’s server, and higher values to increase your bot’s throughput

    allowed_updates*: list[str] | None*
    :   A JSON-serialized list of the update types you want your bot to receive. For example, specify `["message", "edited_channel_post", "callback_query"]` to only receive updates of these types. See [`aiogram.types.update.Update`](../types/update.html#aiogram.types.update.Update "aiogram.types.update.Update") for a complete list of available update types. Specify an empty list to receive all update types except *chat_member*, *message_reaction*, and *message_reaction_count* (default). If not specified, the previous setting will be used

    drop_pending_updates*: bool | None*
    :   Pass `True` to drop all pending updates

    secret_token*: str | None*
    :   A secret token to be sent in a header ‘X-Telegram-Bot-Api-Secret-Token’ in every webhook request, 1-256 characters. Only characters `A-Z`, `a-z`, `0-9`, `_` and `-` are allowed. The header is useful to ensure that the request comes from a webhook set by you

## Usage

### As bot method

```
result: bool = await bot.set_webhook(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_webhook import SetWebhook`
- alias: `from aiogram.methods import SetWebhook`

#### With specific bot

```
result: bool = await bot(SetWebhook(...))
```

#### As reply into Webhook in handler

```
return SetWebhook(...)
```
