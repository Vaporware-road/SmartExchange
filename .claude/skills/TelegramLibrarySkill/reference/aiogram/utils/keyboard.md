# Keyboard builder

> Source: [https://docs.aiogram.dev/en/latest/utils/keyboard.html](https://docs.aiogram.dev/en/latest/utils/keyboard.html)

Keyboard builder helps to dynamically generate markup.

Note

Note that if you have static markup, it’s best to define it explicitly rather than using builder,
but if you have dynamic markup configuration, feel free to use builder as you wish.

## Usage example

For example you want to generate inline keyboard with 10 buttons

```
builder = InlineKeyboardBuilder()

for index in range(1, 11):
    builder.button(text=f"Set {index}", callback_data=f"set:{index}")
```

then adjust this buttons to some grid, for example first line will have 3 buttons, the next lines will have 2 buttons

```
builder.adjust(3, 2)
```

also you can attach another builder to this one

```
another_builder = InlineKeyboardBuilder(...)...  # Another builder with some buttons
builder.attach(another_builder)
```

or you can attach some already generated markup

```
markup = InlineKeyboardMarkup(inline_keyboard=[...])  # Some markup
builder.attach(InlineKeyboardBuilder.from_markup(markup))
```

and finally you can export this markup to use it in your message

```
await message.answer("Some text here", reply_markup=builder.as_markup())
```

Reply keyboard builder has the same interface

Warning

Note that you can’t attach reply keyboard builder to inline keyboard builder and vice versa

## Inline Keyboard

*class* aiogram.utils.keyboard.InlineKeyboardBuilder(*markup: list[list[[InlineKeyboardButton](../api/types/inline_keyboard_button.html#aiogram.types.inline_keyboard_button.InlineKeyboardButton "aiogram.types.inline_keyboard_button.InlineKeyboardButton")]] | None = None*)
:   Inline keyboard builder inherits all methods from generic builder

    button(*text: str*, *url: str | None = None*, *login_url: [LoginUrl](../api/types/login_url.html#aiogram.types.login_url.LoginUrl "aiogram.types.login_url.LoginUrl") | None = None*, *callback_data: str | [CallbackData](../dispatcher/filters/callback_data.html#aiogram.filters.callback_data.CallbackData "aiogram.filters.callback_data.CallbackData") | None = None*, *switch_inline_query: str | None = None*, *switch_inline_query_current_chat: str | None = None*, *callback_game: [CallbackGame](../api/types/callback_game.html#aiogram.types.callback_game.CallbackGame "aiogram.types.callback_game.CallbackGame") | None = None*, *pay: bool | None = None*, *\*\*kwargs: Any*) → [aiogram.utils.keyboard.InlineKeyboardBuilder](#aiogram.utils.keyboard.InlineKeyboardBuilder "aiogram.utils.keyboard.InlineKeyboardBuilder")
    :   Add new inline button to markup

    as_markup() → [aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup](../api/types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup")
    :   Construct an InlineKeyboardMarkup

    __init__(*markup: list[list[[InlineKeyboardButton](../api/types/inline_keyboard_button.html#aiogram.types.inline_keyboard_button.InlineKeyboardButton "aiogram.types.inline_keyboard_button.InlineKeyboardButton")]] | None = None*) → None

    add(*\*buttons: ButtonType*) → KeyboardBuilder[ButtonType]
    :   Add one or many buttons to markup.

        Parameters:
        :   **buttons**

        Returns:

    adjust(*\*sizes: int*, *repeat: bool = False*) → KeyboardBuilder[ButtonType]
    :   Adjust previously added buttons to specific row sizes.

        By default, when the sum of passed sizes is lower than buttons count the last
        one size will be used for tail of the markup.
        If repeat=True is passed - all sizes will be cycled when available more buttons
        count than all sizes

        Parameters:
        :   - **sizes**
            - **repeat**

        Returns:

    *property* buttons*: Generator[ButtonType, None, None]*
    :   Get flatten set of all buttons

        Returns:

    copy() → [InlineKeyboardBuilder](#aiogram.utils.keyboard.InlineKeyboardBuilder "aiogram.utils.keyboard.InlineKeyboardBuilder")
    :   Make full copy of current builder with markup

        Returns:

    export() → list[list[ButtonType]]
    :   Export configured markup as list of lists of buttons

        ```
        >>> builder = KeyboardBuilder(button_type=InlineKeyboardButton)
        >>> ... # Add buttons to builder
        >>> markup = InlineKeyboardMarkup(inline_keyboard=builder.export())
        ```

        Returns:

    *classmethod* from_markup(*markup: [InlineKeyboardMarkup](../api/types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup")*) → [InlineKeyboardBuilder](#aiogram.utils.keyboard.InlineKeyboardBuilder "aiogram.utils.keyboard.InlineKeyboardBuilder")
    :   Create builder from existing markup

        Parameters:
        :   **markup**

        Returns:

    row(*\*buttons: ButtonType*, *width: int | None = None*) → KeyboardBuilder[ButtonType]
    :   Add row to markup

        When too much buttons is passed it will be separated to many rows

        Parameters:
        :   - **buttons**
            - **width**

        Returns:

## Reply Keyboard

*class* aiogram.utils.keyboard.ReplyKeyboardBuilder(*markup: list[list[[KeyboardButton](../api/types/keyboard_button.html#aiogram.types.keyboard_button.KeyboardButton "aiogram.types.keyboard_button.KeyboardButton")]] | None = None*)
:   Reply keyboard builder inherits all methods from generic builder

    button(*text: str*, *request_contact: bool | None = None*, *request_location: bool | None = None*, *request_poll: [KeyboardButtonPollType](../api/types/keyboard_button_poll_type.html#aiogram.types.keyboard_button_poll_type.KeyboardButtonPollType "aiogram.types.keyboard_button_poll_type.KeyboardButtonPollType") | None = None*, *\*\*kwargs: Any*) → [aiogram.utils.keyboard.ReplyKeyboardBuilder](#aiogram.utils.keyboard.ReplyKeyboardBuilder "aiogram.utils.keyboard.ReplyKeyboardBuilder")
    :   Add new button to markup

    as_markup() → [aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup](../api/types/reply_keyboard_markup.html#aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup "aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup")
    :   Construct an ReplyKeyboardMarkup

    __init__(*markup: list[list[[KeyboardButton](../api/types/keyboard_button.html#aiogram.types.keyboard_button.KeyboardButton "aiogram.types.keyboard_button.KeyboardButton")]] | None = None*) → None

    add(*\*buttons: ButtonType*) → KeyboardBuilder[ButtonType]
    :   Add one or many buttons to markup.

        Parameters:
        :   **buttons**

        Returns:

    adjust(*\*sizes: int*, *repeat: bool = False*) → KeyboardBuilder[ButtonType]
    :   Adjust previously added buttons to specific row sizes.

        By default, when the sum of passed sizes is lower than buttons count the last
        one size will be used for tail of the markup.
        If repeat=True is passed - all sizes will be cycled when available more buttons
        count than all sizes

        Parameters:
        :   - **sizes**
            - **repeat**

        Returns:

    *property* buttons*: Generator[ButtonType, None, None]*
    :   Get flatten set of all buttons

        Returns:

    copy() → [ReplyKeyboardBuilder](#aiogram.utils.keyboard.ReplyKeyboardBuilder "aiogram.utils.keyboard.ReplyKeyboardBuilder")
    :   Make full copy of current builder with markup

        Returns:

    export() → list[list[ButtonType]]
    :   Export configured markup as list of lists of buttons

        ```
        >>> builder = KeyboardBuilder(button_type=InlineKeyboardButton)
        >>> ... # Add buttons to builder
        >>> markup = InlineKeyboardMarkup(inline_keyboard=builder.export())
        ```

        Returns:

    *classmethod* from_markup(*markup: [ReplyKeyboardMarkup](../api/types/reply_keyboard_markup.html#aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup "aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup")*) → [ReplyKeyboardBuilder](#aiogram.utils.keyboard.ReplyKeyboardBuilder "aiogram.utils.keyboard.ReplyKeyboardBuilder")
    :   Create builder from existing markup

        Parameters:
        :   **markup**

        Returns:

    row(*\*buttons: ButtonType*, *width: int | None = None*) → KeyboardBuilder[ButtonType]
    :   Add row to markup

        When too much buttons is passed it will be separated to many rows

        Parameters:
        :   - **buttons**
            - **width**

        Returns:
