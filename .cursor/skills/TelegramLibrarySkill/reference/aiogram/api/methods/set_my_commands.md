# setMyCommands

> Source: [https://docs.aiogram.dev/en/latest/api/methods/set_my_commands.html](https://docs.aiogram.dev/en/latest/api/methods/set_my_commands.html)

Returns: `bool`

*class* aiogram.methods.set_my_commands.SetMyCommands(*\**, *commands: list[[BotCommand](../types/bot_command.html#aiogram.types.bot_command.BotCommand "aiogram.types.bot_command.BotCommand")]*, *scope: Annotated[[BotCommandScopeDefault](../types/bot_command_scope_default.html#aiogram.types.bot_command_scope_default.BotCommandScopeDefault "aiogram.types.bot_command_scope_default.BotCommandScopeDefault") | [BotCommandScopeAllPrivateChats](../types/bot_command_scope_all_private_chats.html#aiogram.types.bot_command_scope_all_private_chats.BotCommandScopeAllPrivateChats "aiogram.types.bot_command_scope_all_private_chats.BotCommandScopeAllPrivateChats") | [BotCommandScopeAllGroupChats](../types/bot_command_scope_all_group_chats.html#aiogram.types.bot_command_scope_all_group_chats.BotCommandScopeAllGroupChats "aiogram.types.bot_command_scope_all_group_chats.BotCommandScopeAllGroupChats") | [BotCommandScopeAllChatAdministrators](../types/bot_command_scope_all_chat_administrators.html#aiogram.types.bot_command_scope_all_chat_administrators.BotCommandScopeAllChatAdministrators "aiogram.types.bot_command_scope_all_chat_administrators.BotCommandScopeAllChatAdministrators") | [BotCommandScopeChat](../types/bot_command_scope_chat.html#aiogram.types.bot_command_scope_chat.BotCommandScopeChat "aiogram.types.bot_command_scope_chat.BotCommandScopeChat") | [BotCommandScopeChatAdministrators](../types/bot_command_scope_chat_administrators.html#aiogram.types.bot_command_scope_chat_administrators.BotCommandScopeChatAdministrators "aiogram.types.bot_command_scope_chat_administrators.BotCommandScopeChatAdministrators") | [BotCommandScopeChatMember](../types/bot_command_scope_chat_member.html#aiogram.types.bot_command_scope_chat_member.BotCommandScopeChatMember "aiogram.types.bot_command_scope_chat_member.BotCommandScopeChatMember"), FieldInfo(annotation=NoneType, required=True, discriminator='type')] | None = None*, *language_code: str | None = None*, *\*\*extra_data: Any*)
:   Use this method to change the list of the bot’s commands. See [this manual](https://core.telegram.org/bots/features#commands) for more details about bot commands. Returns `True` on success.

    Source: <https://core.telegram.org/bots/api#setmycommands>

    commands*: list[[BotCommand](../types/bot_command.html#aiogram.types.bot_command.BotCommand "aiogram.types.bot_command.BotCommand")]*
    :   A JSON-serialized list of bot commands to be set as the list of the bot’s commands. At most 100 commands can be specified

    scope*: BotCommandScopeUnion | None*
    :   A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to [`aiogram.types.bot_command_scope_default.BotCommandScopeDefault`](../types/bot_command_scope_default.html#aiogram.types.bot_command_scope_default.BotCommandScopeDefault "aiogram.types.bot_command_scope_default.BotCommandScopeDefault")

    language_code*: str | None*
    :   A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands

## Usage

### As bot method

```
result: bool = await bot.set_my_commands(...)
```

### Method as object

Imports:

- `from aiogram.methods.set_my_commands import SetMyCommands`
- alias: `from aiogram.methods import SetMyCommands`

#### With specific bot

```
result: bool = await bot(SetMyCommands(...))
```

#### As reply into Webhook in handler

```
return SetMyCommands(...)
```
