# PaidMediaInfo

> Source: [https://docs.aiogram.dev/en/latest/api/types/paid_media_info.html](https://docs.aiogram.dev/en/latest/api/types/paid_media_info.html)

*class* aiogram.types.paid_media_info.PaidMediaInfo(*\**, *star_count: int*, *paid_media: list[Annotated[[PaidMediaLivePhoto](paid_media_live_photo.html#aiogram.types.paid_media_live_photo.PaidMediaLivePhoto "aiogram.types.paid_media_live_photo.PaidMediaLivePhoto") | [PaidMediaPhoto](paid_media_photo.html#aiogram.types.paid_media_photo.PaidMediaPhoto "aiogram.types.paid_media_photo.PaidMediaPhoto") | [PaidMediaPreview](paid_media_preview.html#aiogram.types.paid_media_preview.PaidMediaPreview "aiogram.types.paid_media_preview.PaidMediaPreview") | [PaidMediaVideo](paid_media_video.html#aiogram.types.paid_media_video.PaidMediaVideo "aiogram.types.paid_media_video.PaidMediaVideo"), FieldInfo(annotation=NoneType, required=True, discriminator='type')]]*, *\*\*extra_data: Any*)
:   Describes the paid media added to a message.

    Source: <https://core.telegram.org/bots/api#paidmediainfo>

    star_count*: int*
    :   The number of Telegram Stars that must be paid to buy access to the media

    paid_media*: list[PaidMediaUnion]*
    :   Information about the paid media
