# LinkPreviewOptions

> Source: [https://docs.aiogram.dev/en/latest/api/types/link_preview_options.html](https://docs.aiogram.dev/en/latest/api/types/link_preview_options.html)

*class* aiogram.types.link_preview_options.LinkPreviewOptions(*\**, *is_disabled: bool | ~aiogram.client.default.Default | None = <Default('link_preview_is_disabled')>*, *url: str | None = None*, *prefer_small_media: bool | ~aiogram.client.default.Default | None = <Default('link_preview_prefer_small_media')>*, *prefer_large_media: bool | ~aiogram.client.default.Default | None = <Default('link_preview_prefer_large_media')>*, *show_above_text: bool | ~aiogram.client.default.Default | None = <Default('link_preview_show_above_text')>*, *\*\*extra_data: ~typing.Any*)
:   Describes the options used for link preview generation.

    Source: <https://core.telegram.org/bots/api#linkpreviewoptions>

    is_disabled*: bool | Default | None*
    :   *Optional*. `True`, if the link preview is disabled

    url*: str | None*
    :   *Optional*. URL to use for the link preview. If empty, then the first URL found in the message text will be used

    prefer_small_media*: bool | Default | None*
    :   *Optional*. `True`, if the media in the link preview is supposed to be shrunk; ignored if the URL isn’t explicitly specified or media size change isn’t supported for the preview

    prefer_large_media*: bool | Default | None*
    :   *Optional*. `True`, if the media in the link preview is supposed to be enlarged; ignored if the URL isn’t explicitly specified or media size change isn’t supported for the preview

    show_above_text*: bool | Default | None*
    :   *Optional*. `True`, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text
