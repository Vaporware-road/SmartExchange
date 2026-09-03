# BackgroundFillGradient

> Source: [https://docs.aiogram.dev/en/latest/api/types/background_fill_gradient.html](https://docs.aiogram.dev/en/latest/api/types/background_fill_gradient.html)

*class* aiogram.types.background_fill_gradient.BackgroundFillGradient(*\**, *type: Literal['gradient'] = 'gradient'*, *top_color: int*, *bottom_color: int*, *rotation_angle: int*, *\*\*extra_data: Any*)
:   The background is a gradient fill.

    Source: <https://core.telegram.org/bots/api#backgroundfillgradient>

    type*: Literal['gradient']*
    :   Type of the background fill, always ‘gradient’

    top_color*: int*
    :   Top color of the gradient in the RGB24 format

    bottom_color*: int*
    :   Bottom color of the gradient in the RGB24 format

    rotation_angle*: int*
    :   Clockwise rotation angle of the background fill in degrees; 0-359
