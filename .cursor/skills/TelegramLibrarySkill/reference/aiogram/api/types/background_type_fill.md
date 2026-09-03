# BackgroundTypeFill

> Source: [https://docs.aiogram.dev/en/latest/api/types/background_type_fill.html](https://docs.aiogram.dev/en/latest/api/types/background_type_fill.html)

*class* aiogram.types.background_type_fill.BackgroundTypeFill(*\**, *type: Literal['fill'] = 'fill'*, *fill: [BackgroundFillSolid](background_fill_solid.html#aiogram.types.background_fill_solid.BackgroundFillSolid "aiogram.types.background_fill_solid.BackgroundFillSolid") | [BackgroundFillGradient](background_fill_gradient.html#aiogram.types.background_fill_gradient.BackgroundFillGradient "aiogram.types.background_fill_gradient.BackgroundFillGradient") | [BackgroundFillFreeformGradient](background_fill_freeform_gradient.html#aiogram.types.background_fill_freeform_gradient.BackgroundFillFreeformGradient "aiogram.types.background_fill_freeform_gradient.BackgroundFillFreeformGradient")*, *dark_theme_dimming: int*, *\*\*extra_data: Any*)
:   The background is automatically filled based on the selected colors.

    Source: <https://core.telegram.org/bots/api#backgroundtypefill>

    type*: Literal['fill']*
    :   Type of the background, always ‘fill’

    fill*: BackgroundFillUnion*
    :   The background fill

    dark_theme_dimming*: int*
    :   Dimming of the background in dark themes, as a percentage; 0-100
