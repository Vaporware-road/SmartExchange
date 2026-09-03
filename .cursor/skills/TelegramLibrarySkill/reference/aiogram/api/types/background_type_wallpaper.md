# BackgroundTypeWallpaper

> Source: [https://docs.aiogram.dev/en/latest/api/types/background_type_wallpaper.html](https://docs.aiogram.dev/en/latest/api/types/background_type_wallpaper.html)

*class* aiogram.types.background_type_wallpaper.BackgroundTypeWallpaper(*\**, *type: Literal['wallpaper'] = 'wallpaper'*, *document: [Document](document.html#aiogram.types.document.Document "aiogram.types.document.Document")*, *dark_theme_dimming: int*, *is_blurred: bool | None = None*, *is_moving: bool | None = None*, *\*\*extra_data: Any*)
:   The background is a wallpaper in the JPEG format.

    Source: <https://core.telegram.org/bots/api#backgroundtypewallpaper>

    type*: Literal['wallpaper']*
    :   Type of the background, always ‘wallpaper’

    document*: [Document](document.html#aiogram.types.document.Document "aiogram.types.document.Document")*
    :   Document with the wallpaper

    dark_theme_dimming*: int*
    :   Dimming of the background in dark themes, as a percentage; 0-100

    is_blurred*: bool | None*
    :   *Optional*. `True`, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12

    is_moving*: bool | None*
    :   *Optional*. `True`, if the background moves slightly when the device is tilted
