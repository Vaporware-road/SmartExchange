# Formatting

> Source: [https://docs.aiogram.dev/en/latest/utils/formatting.html](https://docs.aiogram.dev/en/latest/utils/formatting.html)

Make your message formatting flexible and simple

This instrument works on top of Message entities instead of using HTML or Markdown markups,
you can easily construct your message and sent it to the Telegram without the need to
remember tag parity (opening and closing) or escaping user input.

## Usage

### Basic scenario

Construct your message and send it to the Telegram.

```
content = Text("Hello, ", Bold(message.from_user.full_name), "!")
await message.answer(**content.as_kwargs())
```

Is the same as the next example, but without usage markup

```
await message.answer(
    text=f"Hello, <b>{html.quote(message.from_user.full_name)}</b>!",
    parse_mode=ParseMode.HTML
)
```

Literally when you execute `as_kwargs` method the Text object is converted
into text `Hello, Alex!` with entities list `[MessageEntity(type='bold', offset=7, length=4)]`
and passed into dict which can be used as `**kwargs` in API call.

The complete list of elements is listed [on this page below](#available-elements).

### Advanced scenario

On top of base elements can be implemented content rendering structures,
so, out of the box aiogram has a few already implemented functions that helps you to format
your messages:

aiogram.utils.formatting.as_line(*\*items: Any*, *end: str = '\n'*, *sep: str = ''*) → [Text](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")
:   Wrap multiple nodes into line with `\n` at the end of line.

    Parameters:
    :   - **items** – Text or Any
        - **end** – ending of the line, by default is `\n`
        - **sep** – separator between items, by default is empty string

    Returns:
    :   Text

aiogram.utils.formatting.as_list(*\*items: Any*, *sep: str = '\n'*) → [Text](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")
:   Wrap each element to separated lines

    Parameters:
    :   - **items**
        - **sep**

    Returns:

aiogram.utils.formatting.as_marked_list(*\*items: Any*, *marker: str = '- '*) → [Text](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")
:   Wrap elements as marked list

    Parameters:
    :   - **items**
        - **marker** – line marker, by default is ‘- ‘

    Returns:
    :   Text

aiogram.utils.formatting.as_numbered_list(*\*items: Any*, *start: int = 1*, *fmt: str = '{}. '*) → [Text](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")
:   Wrap elements as numbered list

    Parameters:
    :   - **items**
        - **start** – initial number, by default 1
        - **fmt** – number format, by default ‘{}. ‘

    Returns:
    :   Text

aiogram.utils.formatting.as_section(*title: Any*, *\*body: Any*) → [Text](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")
:   Wrap elements as simple section, section has title and body

    Parameters:
    :   - **title**
        - **body**

    Returns:
    :   Text

aiogram.utils.formatting.as_marked_section(*title: Any*, *\*body: Any*, *marker: str = '- '*) → [Text](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")
:   Wrap elements as section with marked list

    Parameters:
    :   - **title**
        - **body**
        - **marker**

    Returns:

aiogram.utils.formatting.as_numbered_section(*title: Any*, *\*body: Any*, *start: int = 1*, *fmt: str = '{}. '*) → [Text](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")
:   Wrap elements as section with numbered list

    Parameters:
    :   - **title**
        - **body**
        - **start**
        - **fmt**

    Returns:

aiogram.utils.formatting.as_key_value(*key: Any*, *value: Any*) → [Text](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")
:   Wrap elements pair as key-value line. (`<b>{key}:</b> {value}`)

    Parameters:
    :   - **key**
        - **value**

    Returns:
    :   Text

and lets complete them all:

```
content = as_list(
    as_marked_section(
        Bold("Success:"),
        "Test 1",
        "Test 3",
        "Test 4",
        marker="✅ ",
    ),
    as_marked_section(
        Bold("Failed:"),
        "Test 2",
        marker="❌ ",
    ),
    as_marked_section(
        Bold("Summary:"),
        as_key_value("Total", 4),
        as_key_value("Success", 3),
        as_key_value("Failed", 1),
        marker="  ",
    ),
    HashTag("#test"),
    sep="\n\n",
)
```

Will be rendered into:

> **Success:**
>
> ✅ Test 1
>
> ✅ Test 3
>
> ✅ Test 4
>
> **Failed:**
>
> ❌ Test 2
>
> **Summary:**
>
> > **Total**: 4
> >
> > **Success**: 3
> >
> > **Failed**: 1
>
> #test

Or as HTML:

```
<b>Success:</b>
✅ Test 1
✅ Test 3
✅ Test 4

<b>Failed:</b>
❌ Test 2

<b>Summary:</b>
  <b>Total:</b> 4
  <b>Success:</b> 3
  <b>Failed:</b> 1

#test
```

## Available methods

*class* aiogram.utils.formatting.Text(*\*body: Any*, *\*\*params: Any*)
:   Bases: `Iterable`[`Any`]

    Simple text element

    __init__(*\*body: Any*, *\*\*params: Any*) → None

    render(*\**, *_offset: int = 0*, *_sort: bool = True*, *_collect_entities: bool = True*) → tuple[str, list[[MessageEntity](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")]]
    :   Render elements tree as text with entities list

        Returns:

    as_kwargs(*\**, *text_key: str = 'text'*, *entities_key: str = 'entities'*, *replace_parse_mode: bool = True*, *parse_mode_key: str = 'parse_mode'*) → dict[str, Any]
    :   Render element tree as keyword arguments for usage in an API call, for example:

        ```
        entities = Text(...)
        await message.answer(**entities.as_kwargs())
        ```

        Parameters:
        :   - **text_key**
            - **entities_key**
            - **replace_parse_mode**
            - **parse_mode_key**

        Returns:

    as_caption_kwargs(*\**, *replace_parse_mode: bool = True*) → dict[str, Any]
    :   Shortcut for [`as_kwargs()`](#aiogram.utils.formatting.Text.as_kwargs "aiogram.utils.formatting.Text.as_kwargs") for usage with API calls that take
        `caption` as a parameter.

        ```
        entities = Text(...)
        await message.answer_photo(**entities.as_caption_kwargs(), photo=phot)
        ```

        Parameters:
        :   **replace_parse_mode** – Will be passed to [`as_kwargs()`](#aiogram.utils.formatting.Text.as_kwargs "aiogram.utils.formatting.Text.as_kwargs").

        Returns:

    as_poll_question_kwargs(*\**, *replace_parse_mode: bool = True*) → dict[str, Any]
    :   Shortcut for [`as_kwargs()`](#aiogram.utils.formatting.Text.as_kwargs "aiogram.utils.formatting.Text.as_kwargs") for usage with
        method [`aiogram.methods.send_poll.SendPoll`](../api/methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll").

        ```
        entities = Text(...)
        await message.answer_poll(**entities.as_poll_question_kwargs(), options=options)
        ```

        Parameters:
        :   **replace_parse_mode** – Will be passed to [`as_kwargs()`](#aiogram.utils.formatting.Text.as_kwargs "aiogram.utils.formatting.Text.as_kwargs").

        Returns:

    as_poll_explanation_kwargs(*\**, *replace_parse_mode: bool = True*) → dict[str, Any]
    :   Shortcut for [`as_kwargs()`](#aiogram.utils.formatting.Text.as_kwargs "aiogram.utils.formatting.Text.as_kwargs") for usage with
        method [`aiogram.methods.send_poll.SendPoll`](../api/methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll").

        ```
        question_entities = Text(...)
        explanation_entities = Text(...)
        await message.answer_poll(
            **question_entities.as_poll_question_kwargs(),
            options=options,
            **explanation_entities.as_poll_explanation_kwargs(),
        )
        ```

        Parameters:
        :   **replace_parse_mode** – Will be passed to [`as_kwargs()`](#aiogram.utils.formatting.Text.as_kwargs "aiogram.utils.formatting.Text.as_kwargs").

        Returns:

    as_gift_text_kwargs(*\**, *replace_parse_mode: bool = True*) → dict[str, Any]
    :   Shortcut for [`as_kwargs()`](#aiogram.utils.formatting.Text.as_kwargs "aiogram.utils.formatting.Text.as_kwargs") for usage with
        method [`aiogram.methods.send_gift.SendGift`](../api/methods/send_gift.html#aiogram.methods.send_gift.SendGift "aiogram.methods.send_gift.SendGift").

        ```
        entities = Text(...)
        await bot.send_gift(gift_id=gift_id, user_id=user_id, **entities.as_gift_text_kwargs())
        ```

        Parameters:
        :   **replace_parse_mode** – Will be passed to [`as_kwargs()`](#aiogram.utils.formatting.Text.as_kwargs "aiogram.utils.formatting.Text.as_kwargs").

        Returns:

    as_html() → str
    :   Render elements tree as HTML markup

    as_markdown() → str
    :   Render elements tree as MarkdownV2 markup

## Available elements

*class* aiogram.utils.formatting.Text(*\*body: Any*, *\*\*params: Any*)
:   Bases: `Iterable`[`Any`]

    Simple text element

*class* aiogram.utils.formatting.HashTag(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Hashtag element.

    Warning

    The value should always start with ‘#’ symbol

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.HASHTAG`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.HASHTAG "aiogram.enums.message_entity_type.MessageEntityType.HASHTAG")

*class* aiogram.utils.formatting.CashTag(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Cashtag element.

    Warning

    The value should always start with ‘$’ symbol

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.CASHTAG`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.CASHTAG "aiogram.enums.message_entity_type.MessageEntityType.CASHTAG")

*class* aiogram.utils.formatting.BotCommand(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Bot command element.

    Warning

    The value should always start with ‘/’ symbol

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.BOT_COMMAND`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.BOT_COMMAND "aiogram.enums.message_entity_type.MessageEntityType.BOT_COMMAND")

*class* aiogram.utils.formatting.Url(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Url element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.URL`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.URL "aiogram.enums.message_entity_type.MessageEntityType.URL")

*class* aiogram.utils.formatting.Email(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Email element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.EMAIL`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.EMAIL "aiogram.enums.message_entity_type.MessageEntityType.EMAIL")

*class* aiogram.utils.formatting.PhoneNumber(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Phone number element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.PHONE_NUMBER`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.PHONE_NUMBER "aiogram.enums.message_entity_type.MessageEntityType.PHONE_NUMBER")

*class* aiogram.utils.formatting.Bold(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Bold element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.BOLD`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.BOLD "aiogram.enums.message_entity_type.MessageEntityType.BOLD")

*class* aiogram.utils.formatting.Italic(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Italic element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.ITALIC`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.ITALIC "aiogram.enums.message_entity_type.MessageEntityType.ITALIC")

*class* aiogram.utils.formatting.Underline(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Underline element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.UNDERLINE`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.UNDERLINE "aiogram.enums.message_entity_type.MessageEntityType.UNDERLINE")

*class* aiogram.utils.formatting.Strikethrough(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Strikethrough element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.STRIKETHROUGH`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.STRIKETHROUGH "aiogram.enums.message_entity_type.MessageEntityType.STRIKETHROUGH")

*class* aiogram.utils.formatting.Spoiler(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Spoiler element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.SPOILER`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.SPOILER "aiogram.enums.message_entity_type.MessageEntityType.SPOILER")

*class* aiogram.utils.formatting.Code(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Code element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.CODE`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.CODE "aiogram.enums.message_entity_type.MessageEntityType.CODE")

*class* aiogram.utils.formatting.Pre(*\*body: Any*, *language: str | None = None*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Pre element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.PRE`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.PRE "aiogram.enums.message_entity_type.MessageEntityType.PRE")

*class* aiogram.utils.formatting.TextLink(*\*body: Any*, *url: str*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Text link element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.TEXT_LINK`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.TEXT_LINK "aiogram.enums.message_entity_type.MessageEntityType.TEXT_LINK")

*class* aiogram.utils.formatting.TextMention(*\*body: Any*, *user: [User](../api/types/user.html#aiogram.types.user.User "aiogram.types.user.User")*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Text mention element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.TEXT_MENTION`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.TEXT_MENTION "aiogram.enums.message_entity_type.MessageEntityType.TEXT_MENTION")

*class* aiogram.utils.formatting.CustomEmoji(*\*body: Any*, *custom_emoji_id: str*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Custom emoji element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.CUSTOM_EMOJI`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.CUSTOM_EMOJI "aiogram.enums.message_entity_type.MessageEntityType.CUSTOM_EMOJI")

*class* aiogram.utils.formatting.BlockQuote(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Block quote element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.BLOCKQUOTE`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.BLOCKQUOTE "aiogram.enums.message_entity_type.MessageEntityType.BLOCKQUOTE")

*class* aiogram.utils.formatting.ExpandableBlockQuote(*\*body: Any*, *\*\*params: Any*)
:   Bases: [`Text`](#aiogram.utils.formatting.Text "aiogram.utils.formatting.Text")

    Expandable block quote element.

    Will be wrapped into [`aiogram.types.message_entity.MessageEntity`](../api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity")
    with type [`aiogram.enums.message_entity_type.MessageEntityType.EXPANDABLE_BLOCKQUOTE`](../api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType.EXPANDABLE_BLOCKQUOTE "aiogram.enums.message_entity_type.MessageEntityType.EXPANDABLE_BLOCKQUOTE")
