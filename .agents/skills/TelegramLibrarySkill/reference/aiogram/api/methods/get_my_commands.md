# getMyCommands

> Source: [https://docs.aiogram.dev/en/latest/api/methods/get_my_commands.html](https://docs.aiogram.dev/en/latest/api/methods/get_my_commands.html)

Returns: `list[BotCommand]`

*class* aiogram.methods.get_my_commands.GetMyCommands(*\**, *scope: Annotated[[BotCommandScopeDefault](../types/bot_command_scope_default.html#aiogram.types.bot_command_scope_default.BotCommandScopeDefault "aiogram.types.bot_command_scope_default.BotCommandScopeDefault") | [BotCommandScopeAllPrivateChats](../types/bot_command_scope_all_private_chats.html#aiogram.types.bot_command_scope_all_private_chats.BotCommandScopeAllPrivateChats "aiogram.types.bot_command_scope_all_private_chats.BotCommandScopeAllPrivateChats") | [BotCommandScopeAllGroupChats](../types/bot_command_scope_all_group_chats.html#aiogram.types.bot_command_scope_all_group_chats.BotCommandScopeAllGroupChats "aiogram.types.bot_command_scope_all_group_chats.BotCommandScopeAllGroupChats") | [BotCommandScopeAllChatAdministrators](../types/bot_command_scope_all_chat_administrators.html#aiogram.types.bot_command_scope_all_chat_administrators.BotCommandScopeAllChatAdministrators "aiogram.types.bot_command_scope_all_chat_administrators.BotCommandScopeAllChatAdministrators") | [BotCommandScopeChat](../types/bot_command_scope_chat.html#aiogram.types.bot_command_scope_chat.BotCommandScopeChat "aiogram.types.bot_command_scope_chat.BotCommandScopeChat") | [BotCommandScopeChatAdministrators](../types/bot_command_scope_chat_administrators.html#aiogram.types.bot_command_scope_chat_administrators.BotCommandScopeChatAdministrators "aiogram.types.bot_command_scope_chat_administrators.BotCommandScopeChatAdministrators") | [BotCommandScopeChatMember](../types/bot_command_scope_chat_member.html#aiogram.types.bot_command_scope_chat_member.BotCommandScopeChatMember "aiogram.types.bot_command_scope_chat_member.BotCommandScopeChatMember"), FieldInfo(annotation=NoneType, required=True, discriminator='type')] | None = None*, *language_code: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to get the current list of the bot’s commands for the given scope and user language. Returns an Array of [`aiogram.types.bot_command.BotCommand`](../types/bot_command.html#aiogram.types.bot_command.BotCommand "aiogram.types.bot_command.BotCommand") objects. If commands aren’t set, an empty list is returned.

    Source: <https://core.telegram.org/bots/api#getmycommands>

    scope*: BotCommandScopeUnion | None*
    :   A JSON-serialized object, describing scope of users. Defaults to [`aiogram.types.bot_command_scope_default.BotCommandScopeDefault`](../types/bot_command_scope_default.html#aiogram.types.bot_command_scope_default.BotCommandScopeDefault "aiogram.types.bot_command_scope_default.BotCommandScopeDefault")

    language_code*: str | None*
    :   A two-letter ISO 639-1 language code or an empty string

## Usage

### As bot method

```
result: list[BotCommand] = await bot.get_my_commands(...)
```

### Method as object

Imports:

- `from aiogram.methods.get_my_commands import GetMyCommands`
- alias: `from aiogram.methods import GetMyCommands`

#### With specific bot

```
result: list[BotCommand] = await bot(GetMyCommands(...))
```
