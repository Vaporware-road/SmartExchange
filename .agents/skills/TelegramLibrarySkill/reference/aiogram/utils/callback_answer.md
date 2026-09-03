# Callback answer

> Source: [https://docs.aiogram.dev/en/latest/utils/callback_answer.html](https://docs.aiogram.dev/en/latest/utils/callback_answer.html)

Helper for callback query handlers, can be useful in bots with a lot of callback
handlers to automatically take answer to all requests.

## Simple usage

For use, it is enough to register the inner middleware [`aiogram.utils.callback_answer.CallbackAnswerMiddleware`](#aiogram.utils.callback_answer.CallbackAnswerMiddleware "aiogram.utils.callback_answer.CallbackAnswerMiddleware") in dispatcher or specific router:

```
dispatcher.callback_query.middleware(CallbackAnswerMiddleware())
```

After that all handled callback queries will be answered automatically after processing the handler.

## Advanced usage

In some cases you need to have some non-standard response parameters, this can be done in several ways:

### Global defaults

Change default parameters while initializing middleware, for example change answer to pre mode and text “OK”:

```
dispatcher.callback_query.middleware(CallbackAnswerMiddleware(pre=True, text="OK"))
```

Look at [`aiogram.utils.callback_answer.CallbackAnswerMiddleware`](#aiogram.utils.callback_answer.CallbackAnswerMiddleware "aiogram.utils.callback_answer.CallbackAnswerMiddleware") to get all available parameters

### Handler specific

By using [flags](../dispatcher/flags.html#flags) you can change the behavior for specific handler

```
@router.callback_query(<filters>)
@flags.callback_answer(text="Thanks", cache_time=30)
async def my_handler(query: CallbackQuery):
    ...
```

Flag arguments is the same as in [`aiogram.utils.callback_answer.CallbackAnswerMiddleware`](#aiogram.utils.callback_answer.CallbackAnswerMiddleware "aiogram.utils.callback_answer.CallbackAnswerMiddleware")
with additional one `disabled` to disable answer.

### A special case

It is not always correct to answer the same in every case,
so there is an option to change the answer inside the handler. You can get an instance of [`aiogram.utils.callback_answer.CallbackAnswer`](#aiogram.utils.callback_answer.CallbackAnswer "aiogram.utils.callback_answer.CallbackAnswer") object inside handler and change whatever you want.

Danger

Note that is impossible to change callback answer attributes when you use `pre=True` mode.

```
@router.callback_query(<filters>)
async def my_handler(query: CallbackQuery, callback_answer: CallbackAnswer):
    ...
    if <everything is ok>:
        callback_answer.text = "All is ok"
    else:
        callback_answer.text = "Something wrong"
        callback_answer.cache_time = 10
```

### Combine that all at once

For example you want to answer in most of cases before handler with text “🤔” but at some cases need to answer after the handler with custom text,
so you can do it:

```
dispatcher.callback_query.middleware(CallbackAnswerMiddleware(pre=True, text="🤔"))

@router.callback_query(<filters>)
@flags.callback_answer(pre=False, cache_time=30)
async def my_handler(query: CallbackQuery):
    ...
    if <everything is ok>:
        callback_answer.text = "All is ok"
```

## Description of objects

*class* aiogram.utils.callback_answer.CallbackAnswerMiddleware(*pre: bool = False*, *text: str | None = None*, *show_alert: bool | None = None*, *url: str | None = None*, *cache_time: int | None = None*)
:   Bases: [`BaseMiddleware`](../dispatcher/middlewares.html#aiogram.dispatcher.middlewares.base.BaseMiddleware "aiogram.dispatcher.middlewares.base.BaseMiddleware")

    __init__(*pre: bool = False*, *text: str | None = None*, *show_alert: bool | None = None*, *url: str | None = None*, *cache_time: int | None = None*) → None
    :   Inner middleware for callback query handlers, can be useful in bots with a lot of callback
        handlers to automatically take answer to all requests

        Parameters:
        :   - **pre** – send answer before execute handler
            - **text** – answer with text
            - **show_alert** – show alert
            - **url** – game url
            - **cache_time** – cache answer for some time

*class* aiogram.utils.callback_answer.CallbackAnswer(*answered: bool*, *disabled: bool = False*, *text: str | None = None*, *show_alert: bool | None = None*, *url: str | None = None*, *cache_time: int | None = None*)
:   Bases: `object`

    __init__(*answered: bool*, *disabled: bool = False*, *text: str | None = None*, *show_alert: bool | None = None*, *url: str | None = None*, *cache_time: int | None = None*) → None
    :   Callback answer configuration

        Parameters:
        :   - **answered** – this request is already answered by middleware
            - **disabled** – answer will not be performed
            - **text** – answer with text
            - **show_alert** – show alert
            - **url** – game url
            - **cache_time** – cache answer for some time

    disable() → None
    :   Deactivate answering for this handler

    *property* disabled*: bool*
    :   Indicates that automatic answer is disabled in this handler

    *property* answered*: bool*
    :   Indicates that request is already answered by middleware

    *property* text*: str | None*
    :   Response text
        :return:

    *property* show_alert*: bool | None*
    :   Whether to display an alert

    *property* url*: str | None*
    :   Game url

    *property* cache_time*: int | None*
    :   Response cache time
