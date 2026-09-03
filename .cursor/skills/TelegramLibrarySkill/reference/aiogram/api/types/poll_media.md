# PollMedia

> Source: [https://docs.aiogram.dev/en/latest/api/types/poll_media.html](https://docs.aiogram.dev/en/latest/api/types/poll_media.html)

*class* aiogram.types.poll_media.PollMedia(*\**, *animation: [Animation](animation.html#aiogram.types.animation.Animation "aiogram.types.animation.Animation") | None = None*, *audio: [Audio](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio") | None = None*, *document: [Document](document.html#aiogram.types.document.Document "aiogram.types.document.Document") | None = None*, *live_photo: [LivePhoto](live_photo.html#aiogram.types.live_photo.LivePhoto "aiogram.types.live_photo.LivePhoto") | None = None*, *location: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location") | None = None*, *photo: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None = None*, *sticker: [Sticker](sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker") | None = None*, *venue: [Venue](venue.html#aiogram.types.venue.Venue "aiogram.types.venue.Venue") | None = None*, *video: [Video](video.html#aiogram.types.video.Video "aiogram.types.video.Video") | None = None*, *link: [Link](link.html#aiogram.types.link.Link "aiogram.types.link.Link") | None = None*, *\*\*extra_data: Any*)
:   At most **one** of the optional fields can be present in any given object.

    Source: <https://core.telegram.org/bots/api#pollmedia>

    animation*: [Animation](animation.html#aiogram.types.animation.Animation "aiogram.types.animation.Animation") | None*
    :   *Optional*. Media is an animation, information about the animation

    audio*: [Audio](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio") | None*
    :   *Optional*. Media is an audio file, information about the file; currently, can’t be received in a poll option

    document*: [Document](document.html#aiogram.types.document.Document "aiogram.types.document.Document") | None*
    :   *Optional*. Media is a general file, information about the file; currently, can’t be received in a poll option

    live_photo*: [LivePhoto](live_photo.html#aiogram.types.live_photo.LivePhoto "aiogram.types.live_photo.LivePhoto") | None*
    :   *Optional*. Media is a live photo, information about the live photo

    location*: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location") | None*
    :   *Optional*. Media is a shared location, information about the location

    photo*: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None*
    :   *Optional*. Media is a photo, available sizes of the photo

    sticker*: [Sticker](sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker") | None*
    :   *Optional*. Media is a sticker, information about the sticker; currently, for poll options only

    venue*: [Venue](venue.html#aiogram.types.venue.Venue "aiogram.types.venue.Venue") | None*
    :   *Optional*. Media is a venue, information about the venue

    video*: [Video](video.html#aiogram.types.video.Video "aiogram.types.video.Video") | None*
    :   *Optional*. Media is a video, information about the video

    link*: [Link](link.html#aiogram.types.link.Link "aiogram.types.link.Link") | None*
    :   *Optional*. The HTTP link attached to the poll option
