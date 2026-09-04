# Migration FAQ (2.x -> 3.0)

> Source: [https://docs.aiogram.dev/en/latest/migration_2_to_3.html](https://docs.aiogram.dev/en/latest/migration_2_to_3.html)

Danger

This guide is still in progress.

This version introduces numerous breaking changes and architectural improvements.
It helps reduce the count of global variables in your code, provides useful mechanisms
to modularize your code, and enables the creation of shareable modules via packages on PyPI.
It also makes middlewares and filters more controllable, among other improvements.

On this page, you can read about the changes made in relation to the last stable 2.x version.

Note

This page more closely resembles a detailed changelog than a migration guide,
but it will be updated in the future.

Feel free to contribute to this page, if you find something that is not mentioned here.

## Dependencies

- The dependencies required for `i18n` are no longer part of the default package.
  If your application uses translation functionality, be sure to add an optional dependency:

  `pip install aiogram[i18n]`

## Dispatcher

- The [`Dispatcher`](dispatcher/dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher") class no longer accepts a `Bot` instance in its initializer.
  Instead, the `Bot` instance should be passed to the dispatcher only for starting polling
  or handling events from webhooks. This approach also allows for the use of multiple bot
  instances simultaneously (“multibot”).
- [`Dispatcher`](dispatcher/dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher") now can be extended with another Dispatcher-like thing named [`Router`](dispatcher/router.html#aiogram.dispatcher.router.Router "aiogram.dispatcher.router.Router").
  With routes, you can easily modularize your code and potentially share these modules between projects.
  ([Read more »](dispatcher/router.html#nested-routers).)
- Removed the **_handler** suffix from all event handler decorators and registering methods.
  ([Read more »](dispatcher/router.html#event-observers))
- The `Executor` has been entirely removed; you can now use the [`Dispatcher`](dispatcher/dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher") directly to start poll the API or handle webhooks from it.
- The throttling method has been completely removed; you can now use middlewares to control
  the execution context and implement any throttling mechanism you desire.
- Removed global context variables from the API types, `Bot` and [`Dispatcher`](dispatcher/dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher") object.
  From now on, if you want to access the current bot instance within handlers or filters,
  you should accept the argument `bot: Bot` and use it instead of `Bot.get_current()`.
  In middlewares, it can be accessed via `data["bot"]`.
- To skip pending updates, you should now call the [`DeleteWebhook`](api/methods/delete_webhook.html#aiogram.methods.delete_webhook.DeleteWebhook "aiogram.methods.delete_webhook.DeleteWebhook") method directly, rather than passing `skip_updates=True` to the start polling method.
- To feed updates to the [`Dispatcher`](dispatcher/dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher"), instead of method `process_update()`,
  you should use method [`feed_update()`](dispatcher/dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher.feed_update "aiogram.dispatcher.dispatcher.Dispatcher.feed_update").
  ([Read more »](dispatcher/dispatcher.html#handling-updates))

## Filtering events

- Keyword filters can no longer be used; use filters explicitly. ([Read more »](https://github.com/aiogram/aiogram/issues/942))
- Due to the removal of keyword filters, all previously enabled-by-default filters
  (such as state and content_type) are now disabled.
  You must specify them explicitly if you wish to use them.
  For example instead of using `@dp.message_handler(content_types=ContentType.PHOTO)`
  you should use `@router.message(F.photo)`
- Most common filters have been replaced with the “magic filter.” ([Read more »](dispatcher/filters/magic_filters.html#magic-filters))
- By default, the message handler now receives any content type.
  If you want a specific one, simply add the appropriate filters (Magic or any other).
- The state filter is no longer enabled by default. This means that if you used `state="*"`
  in v2, you should not pass any state filter in v3.
  Conversely, if the state was not specified in v2, you will now need to specify it in v3.
- Added the possibility to register global filters for each router, which helps to reduce code
  repetition and provides an easier way to control the purpose of each router.

## Bot API

- All API methods are now classes with validation, implemented via
  [pydantic](https://docs.pydantic.dev/).
  These API calls are also available as methods in the Bot class.
- More pre-defined Enums have been added and moved to the aiogram.enums sub-package.
  For example, the chat type enum is now `aiogram.enums.ChatType` instead of `aiogram.types.chat.ChatType`.
- The HTTP client session has been separated into a container that can be reused
  across different Bot instances within the application.
- API Exceptions are no longer classified by specific messages,
  as Telegram has no documented error codes.
  However, all errors are classified by HTTP status codes, and for each method,
  only one type of error can be associated with a given code.
  Therefore, in most cases, you should check only the error type (by status code)
  without inspecting the error message. More details can be found in the
  exceptions section ».

## Exceptions

### Mapping (v2 -> v3)

- RetryAfter -> `TelegramRetryAfter` ([`aiogram.exceptions`](dispatcher/errors.html#module-aiogram.exceptions "aiogram.exceptions"))
  - Important attribute in v3: `retry_after` (int).
- ChatMigrated / MigrateToChat -> `TelegramMigrateToChat`
  - Important attribute in v3: `migrate_to_chat_id` (int).
- ClientDecodeError -> `ClientDecodeError`
  - Important attributes in v3: `original` (Exception) and `data` (response body).
- BadRequest -> `TelegramBadRequest`
- Unauthorized -> `TelegramUnauthorizedError`
- Forbidden -> `TelegramForbiddenError`
- NotFound -> `TelegramNotFound`
- Conflict -> `TelegramConflictError`
- ServerError -> `TelegramServerError`
- NetworkError -> `TelegramNetworkError`
- EntityTooLarge -> `TelegramEntityTooLarge`

### Exceptions removed in v3 (from v2)

The list below contains common exception names that appeared in aiogram v2 but
are not defined as separate classes in the v3 codebase. For each v2 name, a
recommended v3 replacement (or handling) is provided — keep your migration
logic simple and rely on the v3 exception classes and their attributes.

- MessageNotModified -> `TelegramBadRequest`
- MessageToEditNotFound -> `TelegramNotFound`
- MessageToDeleteNotFound -> `TelegramNotFound`
- MessageCantBeDeleted -> `TelegramForbiddenError` / `TelegramBadRequest`
- CantParseEntities -> `TelegramBadRequest`
- MessageIsTooLong -> `TelegramEntityTooLarge`
- MessageIdentifierNotFound -> `TelegramNotFound`
- UserDeactivated -> `TelegramForbiddenError`
- CantInitiateConversation -> `TelegramBadRequest`
- StickerSetNameInvalid -> `TelegramBadRequest`
- ChatAdminRequired -> `TelegramForbiddenError`

Use these replacements when migrating exception handling from v2 to v3. If
you relied on catching very specific v2 exception classes, replace those
handlers with the corresponding v3 class above (or catch a broader v3 class
such as `TelegramBadRequest` / `TelegramAPIError`) and inspect
available attributes (see “Mapping (v2 -> v3)”) for any required details.

## Middlewares

- Middlewares can now control an execution context, e.g., using context managers.
  ([Read more »](dispatcher/middlewares.html#middlewares))
- All contextual data is now shared end-to-end between middlewares, filters, and handlers.
  For example now you can easily pass some data into context inside middleware and
  get it in the filters layer as the same way as in the handlers via keyword arguments.
- Added a mechanism named **flags** that helps customize handler behavior
  in conjunction with middlewares. ([Read more »](dispatcher/flags.html#flags))

## Keyboard Markup

- Now [`aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup`](api/types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup")
  and [`aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup`](api/types/reply_keyboard_markup.html#aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup "aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup") no longer have methods for extension,
  instead you have to use markup builders [`aiogram.utils.keyboard.ReplyKeyboardBuilder`](utils/keyboard.html#aiogram.utils.keyboard.ReplyKeyboardBuilder "aiogram.utils.keyboard.ReplyKeyboardBuilder")
  and `aiogram.utils.keyboard.KeyboardBuilder` respectively
  ([Read more »](utils/keyboard.html#keyboard-builder))

## Callbacks data

- The callback data factory is now strictly typed using [pydantic](https://docs.pydantic.dev/) models.
  ([Read more »](dispatcher/filters/callback_data.html#callback-data-factory))

## Finite State machine

- State filters will no longer be automatically added to all handlers;
  you will need to specify the state if you want to use it.
- Added the possibility to change the FSM strategy. For example,
  if you want to control the state for each user based on chat topics rather than
  the user in a chat, you can specify this in the [`Dispatcher`](dispatcher/dispatcher.html#aiogram.dispatcher.dispatcher.Dispatcher "aiogram.dispatcher.dispatcher.Dispatcher").
- Now `aiogram.fsm.state.State` and `aiogram.fsm.state.StateGroup` don’t have helper
  methods like `.set()`, `.next()`, etc.
  Instead, you should set states by passing them directly to
  `aiogram.fsm.context.FSMContext` ([Read more »](dispatcher/finite_state_machine/index.html#finite-state-machine))
- The state proxy is deprecated; you should update the state data by calling
  `state.set_data(...)` and `state.get_data()` respectively.

## Sending Files

- From now on, you should wrap files in an InputFile object before sending them,
  instead of passing the IO object directly to the API method. ([Read more »](api/upload_file.html#sending-files))

## Webhook

- The aiohttp web app configuration has been simplified.
- By default, the ability to upload files has been added when you [make requests in response to updates](https://core.telegram.org/bots/faq#how-can-i-make-requests-in-response-to-updates) (available for webhook only).

## Telegram API Server

- The `server` parameter has been moved from the `Bot` instance to `api` parameter of the [`BaseSession`](api/session/base.html#aiogram.client.session.base.BaseSession "aiogram.client.session.base.BaseSession").
- The constant `aiogram.bot.api.TELEGRAM_PRODUCTION` has been moved to `aiogram.client.telegram.PRODUCTION`.

## Telegram objects transformation (to dict, to json, from json)

- Methods `TelegramObject.to_object()`, `TelegramObject.to_json()` and `TelegramObject.to_python()`
  have been removed due to the use of [pydantic](https://docs.pydantic.dev/) models.
- `TelegramObject.to_object()` should be replaced by `TelegramObject.model_validate()`
  ([Read more](https://docs.pydantic.dev/2.7/api/base_model/#pydantic.BaseModel.model_validate))
- `TelegramObject.as_json()` should be replaced by [`aiogram.utils.serialization.deserialize_telegram_object_to_python()`](utils/serialization.html#aiogram.utils.serialization.deserialize_telegram_object_to_python "aiogram.utils.serialization.deserialize_telegram_object_to_python")
- `<TelegramObject>.to_python()` should be replaced by `json.dumps(deserialize_telegram_object_to_python(<TelegramObject>))`

Here are some usage examples:

- Creating an object from a dictionary representation of an object

  ```
  # Version 2.x
  message_dict = {"id": 42, ...}
  message_obj = Message.to_object(message_dict)
  print(message_obj)
  # id=42 name='n' ...
  print(type(message_obj))
  # <class 'aiogram.types.message.Message'>
  ```

  ```
  # Version 3.x
  message_dict = {"id": 42, ...}
  message_obj = Message.model_validate(message_dict)
  print(message_obj)
  # id=42 name='n' ...
  print(type(message_obj))
  # <class 'aiogram.types.message.Message'>
  ```
- Creating a json representation of an object

  ```
  # Version 2.x
  async def handler(message: Message) -> None:
      message_json = message.as_json()
      print(message_json)
      # {"id": 42, ...}
      print(type(message_json))
      # <class 'str'>
  ```

  ```
  # Version 3.x
  async def handler(message: Message) -> None:
      message_json = json.dumps(deserialize_telegram_object_to_python(message))
      print(message_json)
      # {"id": 42, ...}
      print(type(message_json))
      # <class 'str'>
  ```
- Creating a dictionary representation of an object

  ```
  async def handler(message: Message) -> None:
      # Version 2.x
      message_dict = message.to_python()
      print(message_dict)
      # {"id": 42, ...}
      print(type(message_dict))
      # <class 'dict'>
  ```

  ```
  async def handler(message: Message) -> None:
      # Version 3.x
      message_dict = deserialize_telegram_object_to_python(message)
      print(message_dict)
      # {"id": 42, ...}
      print(type(message_dict))
      # <class 'dict'>
  ```

## ChatMember tools

- Now [`aiogram.types.chat_member.ChatMember`](api/types/chat_member.html#aiogram.types.chat_member.ChatMember "aiogram.types.chat_member.ChatMember") no longer contains tools to resolve an object with the appropriate status.

  ```
  # Version 2.x
  from aiogram.types import ChatMember

  chat_member = ChatMember.resolve(**dict_data)
  ```

  ```
  # Version 3.x
  from aiogram.utils.chat_member import ChatMemberAdapter

  chat_member = ChatMemberAdapter.validate_python(dict_data)
  ```
- Now [`aiogram.types.chat_member.ChatMember`](api/types/chat_member.html#aiogram.types.chat_member.ChatMember "aiogram.types.chat_member.ChatMember") and all its child classes no longer
  contain methods for checking for membership in certain logical groups.
  As a substitute, you can use pre-defined groups or create such groups yourself
  and check their entry using the `isinstance()` function

  ```
  # Version 2.x

  if chat_member.is_chat_admin():
      print("ChatMember is chat admin")

  if chat_member.is_chat_member():
      print("ChatMember is in the chat")
  ```

  ```
  # Version 3.x

  from aiogram.utils.chat_member import ADMINS, MEMBERS

  if isinstance(chat_member, ADMINS):
      print("ChatMember is chat admin")

  if isinstance(chat_member, MEMBERS):
      print("ChatMember is in the chat")
  ```

  Note

  You also can independently create group similar to ADMINS that fits the logic of your application.

  E.g., you can create a PUNISHED group and include banned and restricted members there!
