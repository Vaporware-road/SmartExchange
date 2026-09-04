# PaidMediaPreview

> Source: [https://docs.aiogram.dev/en/latest/api/types/paid_media_preview.html](https://docs.aiogram.dev/en/latest/api/types/paid_media_preview.html)

*class* aiogram.types.paid_media_preview.PaidMediaPreview(*\**, *type: Literal[PaidMediaType.PREVIEW] = PaidMediaType.PREVIEW*, *width: int | None = None*, *height: int | None = None*, *duration: int | None = None*, *\*\*extra_data: Any*)
:   The paid media isn’t available before the payment.

    Source: <https://core.telegram.org/bots/api#paidmediapreview>

    type*: Literal[PaidMediaType.PREVIEW]*
    :   Type of the paid media, always ‘preview’

    width*: int | None*
    :   *Optional*. Media width as defined by the sender

    height*: int | None*
    :   *Optional*. Media height as defined by the sender

    duration*: int | None*
    :   *Optional*. Duration of the media in seconds as defined by the sender
