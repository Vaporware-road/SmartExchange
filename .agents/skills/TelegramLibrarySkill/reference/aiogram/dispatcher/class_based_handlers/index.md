# Class based handlers

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/index.html](https://docs.aiogram.dev/en/latest/dispatcher/class_based_handlers/index.html)

A handler is a async callable which takes a event with contextual data and returns a response.

In **aiogram** it can be more than just an async function, these allow you to use classes
which can be used as Telegram event handlers to structure your event handlers and reuse code by harnessing inheritance and mixins.

There are some base class based handlers what you need to use in your own handlers:

- [BaseHandler](base.html)
  - [Example](base.html#example)
- [CallbackQueryHandler](callback_query.html)
  - [`CallbackQueryHandler`](callback_query.html#aiogram.handlers.callback_query.CallbackQueryHandler)
    - [`CallbackQueryHandler.from_user`](callback_query.html#aiogram.handlers.callback_query.CallbackQueryHandler.from_user)
    - [`CallbackQueryHandler.message`](callback_query.html#aiogram.handlers.callback_query.CallbackQueryHandler.message)
    - [`CallbackQueryHandler.callback_data`](callback_query.html#aiogram.handlers.callback_query.CallbackQueryHandler.callback_data)
- [ChosenInlineResultHandler](chosen_inline_result.html)
  - [Simple usage](chosen_inline_result.html#simple-usage)
  - [Extension](chosen_inline_result.html#extension)
- [ErrorHandler](error.html)
  - [Simple usage](error.html#simple-usage)
  - [Extension](error.html#extension)
- [InlineQueryHandler](inline_query.html)
  - [Simple usage](inline_query.html#simple-usage)
  - [Extension](inline_query.html#extension)
- [MessageHandler](message.html)
  - [Simple usage](message.html#simple-usage)
  - [Extension](message.html#extension)
- [PollHandler](poll.html)
  - [Simple usage](poll.html#simple-usage)
  - [Extension](poll.html#extension)
- [PreCheckoutQueryHandler](pre_checkout_query.html)
  - [Simple usage](pre_checkout_query.html#simple-usage)
  - [Extension](pre_checkout_query.html#extension)
- [ShippingQueryHandler](shipping_query.html)
  - [Simple usage](shipping_query.html#simple-usage)
  - [Extension](shipping_query.html#extension)
- [ChatMemberHandler](chat_member.html)
  - [Simple usage](chat_member.html#simple-usage)
  - [Extension](chat_member.html#extension)
