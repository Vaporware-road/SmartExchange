# Command

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/filters/command.html](https://docs.aiogram.dev/en/latest/dispatcher/filters/command.html)

## Usage

1. Filter single variant of commands: `Command("start")`
2. Handle command by regexp pattern: `Command(re.compile(r"item_(\d+)"))`
3. Match command by multiple variants: `Command("item", re.compile(r"item_(\d+)"))`
4. Handle commands in public chats intended for other bots: `Command("command", ignore_mention=True)`
5. Use [`aiogram.types.bot_command.BotCommand`](../../api/types/bot_command.html#aiogram.types.bot_command.BotCommand "aiogram.types.bot_command.BotCommand") object as command reference `Command(BotCommand(command="command", description="My awesome command")`

Warning

Command cannot include spaces or any whitespace

*class* aiogram.filters.command.Command(*\*values: CommandPatternType*, *commands: Sequence[CommandPatternType] | CommandPatternType | None = None*, *prefix: str = '/'*, *ignore_case: bool = False*, *ignore_mention: bool = False*, *magic: MagicFilter | None = None*)
:   This filter can be helpful for handling commands from the text messages.

    Works only with [`aiogram.types.message.Message`](../../api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") events which have the `text`.

    __init__(*\*values: CommandPatternType*, *commands: Sequence[CommandPatternType] | CommandPatternType | None = None*, *prefix: str = '/'*, *ignore_case: bool = False*, *ignore_mention: bool = False*, *magic: MagicFilter | None = None*)
    :   List of commands (string or compiled regexp patterns)

        Parameters:
        :   - **prefix** – Prefix for command.
              Prefix is always a single char but here you can pass all of allowed prefixes,
              for example: `"/!"` will work with commands prefixed
              by `"/"` or `"!"`.
            - **ignore_case** – Ignore case (Does not work with regexp, use flags instead)
            - **ignore_mention** – Ignore bot mention. By default,
              bot can not handle commands intended for other bots
            - **magic** – Validate command object via Magic filter after all checks done

When filter is passed the [`aiogram.filters.command.CommandObject`](#aiogram.filters.command.CommandObject "aiogram.filters.command.CommandObject") will be passed to the handler argument `command`

*class* aiogram.filters.command.CommandObject(*prefix: str = '/'*, *command: str = ''*, *mention: str | None = None*, *args: str | None = None*, *regexp_match: Match[str] | None = None*, *magic_result: Any | None = None*)
:   Instance of this object is always has command and it prefix.
    Can be passed as keyword argument **command** to the handler

    prefix*: str* *= '/'*
    :   Command prefix

    command*: str* *= ''*
    :   Command without prefix and mention

    mention*: str | None* *= None*
    :   Mention (if available)

    args*: str | None* *= None*
    :   Command argument

    regexp_match*: Match[str] | None* *= None*
    :   Will be presented match result if the command is presented as regexp in filter

    magic_result*: Any | None* *= None*

    *property* mentioned*: bool*
    :   This command has mention?

    *property* text*: str*
    :   Generate original text from object

## Allowed handlers

Allowed update types for this filter:

- message
- edited_message
