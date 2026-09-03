# ExternalReplyInfo

> Source: [https://docs.aiogram.dev/en/latest/api/types/external_reply_info.html](https://docs.aiogram.dev/en/latest/api/types/external_reply_info.html)

*class* aiogram.types.external_reply_info.ExternalReplyInfo(*\**, *origin: [MessageOriginUser](message_origin_user.html#aiogram.types.message_origin_user.MessageOriginUser "aiogram.types.message_origin_user.MessageOriginUser") | [MessageOriginHiddenUser](message_origin_hidden_user.html#aiogram.types.message_origin_hidden_user.MessageOriginHiddenUser "aiogram.types.message_origin_hidden_user.MessageOriginHiddenUser") | [MessageOriginChat](message_origin_chat.html#aiogram.types.message_origin_chat.MessageOriginChat "aiogram.types.message_origin_chat.MessageOriginChat") | [MessageOriginChannel](message_origin_channel.html#aiogram.types.message_origin_channel.MessageOriginChannel "aiogram.types.message_origin_channel.MessageOriginChannel")*, *chat: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None = None*, *message_id: int | None = None*, *link_preview_options: [LinkPreviewOptions](link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | None = None*, *animation: [Animation](animation.html#aiogram.types.animation.Animation "aiogram.types.animation.Animation") | None = None*, *audio: [Audio](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio") | None = None*, *document: [Document](document.html#aiogram.types.document.Document "aiogram.types.document.Document") | None = None*, *live_photo: [LivePhoto](live_photo.html#aiogram.types.live_photo.LivePhoto "aiogram.types.live_photo.LivePhoto") | None = None*, *paid_media: [PaidMediaInfo](paid_media_info.html#aiogram.types.paid_media_info.PaidMediaInfo "aiogram.types.paid_media_info.PaidMediaInfo") | None = None*, *photo: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None = None*, *sticker: [Sticker](sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker") | None = None*, *story: [Story](story.html#aiogram.types.story.Story "aiogram.types.story.Story") | None = None*, *video: [Video](video.html#aiogram.types.video.Video "aiogram.types.video.Video") | None = None*, *video_note: [VideoNote](video_note.html#aiogram.types.video_note.VideoNote "aiogram.types.video_note.VideoNote") | None = None*, *voice: [Voice](voice.html#aiogram.types.voice.Voice "aiogram.types.voice.Voice") | None = None*, *has_media_spoiler: bool | None = None*, *checklist: [Checklist](checklist.html#aiogram.types.checklist.Checklist "aiogram.types.checklist.Checklist") | None = None*, *contact: [Contact](contact.html#aiogram.types.contact.Contact "aiogram.types.contact.Contact") | None = None*, *dice: [Dice](dice.html#aiogram.types.dice.Dice "aiogram.types.dice.Dice") | None = None*, *game: [Game](game.html#aiogram.types.game.Game "aiogram.types.game.Game") | None = None*, *giveaway: [Giveaway](giveaway.html#aiogram.types.giveaway.Giveaway "aiogram.types.giveaway.Giveaway") | None = None*, *giveaway_winners: [GiveawayWinners](giveaway_winners.html#aiogram.types.giveaway_winners.GiveawayWinners "aiogram.types.giveaway_winners.GiveawayWinners") | None = None*, *invoice: [Invoice](invoice.html#aiogram.types.invoice.Invoice "aiogram.types.invoice.Invoice") | None = None*, *location: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location") | None = None*, *poll: [Poll](poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") | None = None*, *venue: [Venue](venue.html#aiogram.types.venue.Venue "aiogram.types.venue.Venue") | None = None*, *\*\*extra_data: Any*)
:   This object contains information about a message that is being replied to, which may come from another chat or forum topic.

    Source: <https://core.telegram.org/bots/api#externalreplyinfo>

    origin*: MessageOriginUnion*
    :   Origin of the message replied to by the given message

    chat*: [Chat](chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") | None*
    :   *Optional*. Chat the original message belongs to. Available only if the chat is a supergroup or a channel

    message_id*: int | None*
    :   *Optional*. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel

    link_preview_options*: [LinkPreviewOptions](link_preview_options.html#aiogram.types.link_preview_options.LinkPreviewOptions "aiogram.types.link_preview_options.LinkPreviewOptions") | None*
    :   *Optional*. Options used for link preview generation for the original message, if it is a text message

    animation*: [Animation](animation.html#aiogram.types.animation.Animation "aiogram.types.animation.Animation") | None*
    :   *Optional*. Message is an animation, information about the animation

    audio*: [Audio](audio.html#aiogram.types.audio.Audio "aiogram.types.audio.Audio") | None*
    :   *Optional*. Message is an audio file, information about the file

    document*: [Document](document.html#aiogram.types.document.Document "aiogram.types.document.Document") | None*
    :   *Optional*. Message is a general file, information about the file

    live_photo*: [LivePhoto](live_photo.html#aiogram.types.live_photo.LivePhoto "aiogram.types.live_photo.LivePhoto") | None*
    :   *Optional*. Message is a live photo, information about the live photo

    paid_media*: [PaidMediaInfo](paid_media_info.html#aiogram.types.paid_media_info.PaidMediaInfo "aiogram.types.paid_media_info.PaidMediaInfo") | None*
    :   *Optional*. Message contains paid media; information about the paid media

    photo*: list[[PhotoSize](photo_size.html#aiogram.types.photo_size.PhotoSize "aiogram.types.photo_size.PhotoSize")] | None*
    :   *Optional*. Message is a photo, available sizes of the photo

    sticker*: [Sticker](sticker.html#aiogram.types.sticker.Sticker "aiogram.types.sticker.Sticker") | None*
    :   *Optional*. Message is a sticker, information about the sticker

    story*: [Story](story.html#aiogram.types.story.Story "aiogram.types.story.Story") | None*
    :   *Optional*. Message is a forwarded story

    video*: [Video](video.html#aiogram.types.video.Video "aiogram.types.video.Video") | None*
    :   *Optional*. Message is a video, information about the video

    video_note*: [VideoNote](video_note.html#aiogram.types.video_note.VideoNote "aiogram.types.video_note.VideoNote") | None*
    :   *Optional*. Message is a [video note](https://telegram.org/blog/video-messages-and-telescope), information about the video message

    voice*: [Voice](voice.html#aiogram.types.voice.Voice "aiogram.types.voice.Voice") | None*
    :   *Optional*. Message is a voice message, information about the file

    has_media_spoiler*: bool | None*
    :   *Optional*. `True`, if the message media is covered by a spoiler animation

    checklist*: [Checklist](checklist.html#aiogram.types.checklist.Checklist "aiogram.types.checklist.Checklist") | None*
    :   *Optional*. Message is a checklist

    contact*: [Contact](contact.html#aiogram.types.contact.Contact "aiogram.types.contact.Contact") | None*
    :   *Optional*. Message is a shared contact, information about the contact

    dice*: [Dice](dice.html#aiogram.types.dice.Dice "aiogram.types.dice.Dice") | None*
    :   *Optional*. Message is a dice with random value

    game*: [Game](game.html#aiogram.types.game.Game "aiogram.types.game.Game") | None*
    :   *Optional*. Message is a game, information about the game. [More about games »](https://core.telegram.org/bots/api#games)

    giveaway*: [Giveaway](giveaway.html#aiogram.types.giveaway.Giveaway "aiogram.types.giveaway.Giveaway") | None*
    :   *Optional*. Message is a scheduled giveaway, information about the giveaway

    giveaway_winners*: [GiveawayWinners](giveaway_winners.html#aiogram.types.giveaway_winners.GiveawayWinners "aiogram.types.giveaway_winners.GiveawayWinners") | None*
    :   *Optional*. A giveaway with public winners was completed

    invoice*: [Invoice](invoice.html#aiogram.types.invoice.Invoice "aiogram.types.invoice.Invoice") | None*
    :   *Optional*. Message is an invoice for a [payment](https://core.telegram.org/bots/api#payments), information about the invoice. [More about payments »](https://core.telegram.org/bots/api#payments)

    location*: [Location](location.html#aiogram.types.location.Location "aiogram.types.location.Location") | None*
    :   *Optional*. Message is a shared location, information about the location

    poll*: [Poll](poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") | None*
    :   *Optional*. Message is a native poll, information about the poll

    venue*: [Venue](venue.html#aiogram.types.venue.Venue "aiogram.types.venue.Venue") | None*
    :   *Optional*. Message is a venue, information about the venue
