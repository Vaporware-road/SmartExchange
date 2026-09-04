# UniqueGiftColors

> Source: [https://docs.aiogram.dev/en/latest/api/types/unique_gift_colors.html](https://docs.aiogram.dev/en/latest/api/types/unique_gift_colors.html)

*class* aiogram.types.unique_gift_colors.UniqueGiftColors(*\**, *model_custom_emoji_id: str*, *symbol_custom_emoji_id: str*, *light_theme_main_color: int*, *light_theme_other_colors: list[int]*, *dark_theme_main_color: int*, *dark_theme_other_colors: list[int]*, *\*\*extra_data: Any*)
:   This object contains information about the color scheme for a user’s name, message replies and link previews based on a unique gift.

    Source: <https://core.telegram.org/bots/api#uniquegiftcolors>

    symbol_custom_emoji_id*: str*
    :   Custom emoji identifier of the unique gift’s symbol

    light_theme_main_color*: int*
    :   Main color used in light themes; RGB format

    light_theme_other_colors*: list[int]*
    :   List of 1-3 additional colors used in light themes; RGB format

    dark_theme_main_color*: int*
    :   Main color used in dark themes; RGB format

    dark_theme_other_colors*: list[int]*
    :   List of 1-3 additional colors used in dark themes; RGB format
