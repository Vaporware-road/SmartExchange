# BackgroundTypePattern

> Source: [https://docs.aiogram.dev/en/latest/api/types/background_type_pattern.html](https://docs.aiogram.dev/en/latest/api/types/background_type_pattern.html)

*class* aiogram.types.background_type_pattern.BackgroundTypePattern(*\**, *type: Literal['pattern'] = 'pattern'*, *document: [Document](document.html#aiogram.types.document.Document "aiogram.types.document.Document")*, *fill: [BackgroundFillSolid](background_fill_solid.html#aiogram.types.background_fill_solid.BackgroundFillSolid "aiogram.types.background_fill_solid.BackgroundFillSolid") | [BackgroundFillGradient](background_fill_gradient.html#aiogram.types.background_fill_gradient.BackgroundFillGradient "aiogram.types.background_fill_gradient.BackgroundFillGradient") | [BackgroundFillFreeformGradient](background_fill_freeform_gradient.html#aiogram.types.background_fill_freeform_gradient.BackgroundFillFreeformGradient "aiogram.types.background_fill_freeform_gradient.BackgroundFillFreeformGradient")*, *intensity: int*, *is_inverted: bool | None = None*, *is_moving: bool | None = None*, *\*\*extra_data: Any*)
:   The background is a .PNG or .TGV (gzipped subset of SVG with MIME type ‘application/x-tgwallpattern’) pattern to be combined with the background fill chosen by the user.

    Source: <https://core.telegram.org/bots/api#backgroundtypepattern>

    type*: Literal['pattern']*
    :   Type of the background, always ‘pattern’

    document*: [Document](document.html#aiogram.types.document.Document "aiogram.types.document.Document")*
    :   Document with the pattern

    fill*: BackgroundFillUnion*
    :   The background fill that is combined with the pattern

    intensity*: int*
    :   Intensity of the pattern when it is shown above the filled background; 0-100

    is_inverted*: bool | None*
    :   *Optional*. `True`, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only

    is_moving*: bool | None*
    :   *Optional*. `True`, if the background moves slightly when the device is tilted
