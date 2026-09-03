# Changelog

> Source: [https://docs.aiogram.dev/en/latest/changelog.html](https://docs.aiogram.dev/en/latest/changelog.html)

## 3.30.0 (2026-07-17)

### Improved Documentation

- Added documentation with examples for testing handlers directly and routing updates through `Dispatcher.feed_raw_update`.
  [#378](https://github.com/aiogram/aiogram/issues/378)
- Remove await from dispatcher.fsm.get_context in “Changing state for another user” doc
  [#1854](https://github.com/aiogram/aiogram/issues/1854)

### Misc

- Updated to [Bot API 10.2](https://core.telegram.org/bots/api-changelog#july-14-2026)

  **Rich Messages**

  *New Types:*

  - Added [`aiogram.types.input_rich_message_media.InputRichMessageMedia`](api/types/input_rich_message_media.html#aiogram.types.input_rich_message_media.InputRichMessageMedia "aiogram.types.input_rich_message_media.InputRichMessageMedia") type - media item attached to a rich message to be sent
  - Added [`aiogram.types.input_media_voice_note.InputMediaVoiceNote`](api/types/input_media_voice_note.html#aiogram.types.input_media_voice_note.InputMediaVoiceNote "aiogram.types.input_media_voice_note.InputMediaVoiceNote") type - voice note to be sent as part of a rich message
  - Added [`aiogram.types.input_rich_block.InputRichBlock`](api/types/input_rich_block.html#aiogram.types.input_rich_block.InputRichBlock "aiogram.types.input_rich_block.InputRichBlock") type - base class for all rich block elements to be sent
  - Added [`aiogram.types.input_rich_block_paragraph.InputRichBlockParagraph`](api/types/input_rich_block_paragraph.html#aiogram.types.input_rich_block_paragraph.InputRichBlockParagraph "aiogram.types.input_rich_block_paragraph.InputRichBlockParagraph") type - text paragraph block to be sent
  - Added [`aiogram.types.input_rich_block_section_heading.InputRichBlockSectionHeading`](api/types/input_rich_block_section_heading.html#aiogram.types.input_rich_block_section_heading.InputRichBlockSectionHeading "aiogram.types.input_rich_block_section_heading.InputRichBlockSectionHeading") type - section heading block to be sent
  - Added [`aiogram.types.input_rich_block_preformatted.InputRichBlockPreformatted`](api/types/input_rich_block_preformatted.html#aiogram.types.input_rich_block_preformatted.InputRichBlockPreformatted "aiogram.types.input_rich_block_preformatted.InputRichBlockPreformatted") type - preformatted (code) block to be sent
  - Added [`aiogram.types.input_rich_block_footer.InputRichBlockFooter`](api/types/input_rich_block_footer.html#aiogram.types.input_rich_block_footer.InputRichBlockFooter "aiogram.types.input_rich_block_footer.InputRichBlockFooter") type - footer block to be sent
  - Added [`aiogram.types.input_rich_block_divider.InputRichBlockDivider`](api/types/input_rich_block_divider.html#aiogram.types.input_rich_block_divider.InputRichBlockDivider "aiogram.types.input_rich_block_divider.InputRichBlockDivider") type - horizontal divider block to be sent
  - Added [`aiogram.types.input_rich_block_mathematical_expression.InputRichBlockMathematicalExpression`](api/types/input_rich_block_mathematical_expression.html#aiogram.types.input_rich_block_mathematical_expression.InputRichBlockMathematicalExpression "aiogram.types.input_rich_block_mathematical_expression.InputRichBlockMathematicalExpression") type - mathematical expression block to be sent
  - Added [`aiogram.types.input_rich_block_anchor.InputRichBlockAnchor`](api/types/input_rich_block_anchor.html#aiogram.types.input_rich_block_anchor.InputRichBlockAnchor "aiogram.types.input_rich_block_anchor.InputRichBlockAnchor") type - anchor/target block to be sent
  - Added [`aiogram.types.input_rich_block_list.InputRichBlockList`](api/types/input_rich_block_list.html#aiogram.types.input_rich_block_list.InputRichBlockList "aiogram.types.input_rich_block_list.InputRichBlockList") type - ordered or unordered list block to be sent
  - Added [`aiogram.types.input_rich_block_list_item.InputRichBlockListItem`](api/types/input_rich_block_list_item.html#aiogram.types.input_rich_block_list_item.InputRichBlockListItem "aiogram.types.input_rich_block_list_item.InputRichBlockListItem") type - individual item in a rich block list to be sent
  - Added [`aiogram.types.input_rich_block_block_quotation.InputRichBlockBlockQuotation`](api/types/input_rich_block_block_quotation.html#aiogram.types.input_rich_block_block_quotation.InputRichBlockBlockQuotation "aiogram.types.input_rich_block_block_quotation.InputRichBlockBlockQuotation") type - block quotation block to be sent
  - Added [`aiogram.types.input_rich_block_pull_quotation.InputRichBlockPullQuotation`](api/types/input_rich_block_pull_quotation.html#aiogram.types.input_rich_block_pull_quotation.InputRichBlockPullQuotation "aiogram.types.input_rich_block_pull_quotation.InputRichBlockPullQuotation") type - pull quotation block to be sent
  - Added [`aiogram.types.input_rich_block_collage.InputRichBlockCollage`](api/types/input_rich_block_collage.html#aiogram.types.input_rich_block_collage.InputRichBlockCollage "aiogram.types.input_rich_block_collage.InputRichBlockCollage") type - collage of media items block to be sent
  - Added [`aiogram.types.input_rich_block_slideshow.InputRichBlockSlideshow`](api/types/input_rich_block_slideshow.html#aiogram.types.input_rich_block_slideshow.InputRichBlockSlideshow "aiogram.types.input_rich_block_slideshow.InputRichBlockSlideshow") type - slideshow block to be sent
  - Added [`aiogram.types.input_rich_block_table.InputRichBlockTable`](api/types/input_rich_block_table.html#aiogram.types.input_rich_block_table.InputRichBlockTable "aiogram.types.input_rich_block_table.InputRichBlockTable") type - table block to be sent
  - Added [`aiogram.types.input_rich_block_details.InputRichBlockDetails`](api/types/input_rich_block_details.html#aiogram.types.input_rich_block_details.InputRichBlockDetails "aiogram.types.input_rich_block_details.InputRichBlockDetails") type - expandable details/summary block to be sent
  - Added [`aiogram.types.input_rich_block_map.InputRichBlockMap`](api/types/input_rich_block_map.html#aiogram.types.input_rich_block_map.InputRichBlockMap "aiogram.types.input_rich_block_map.InputRichBlockMap") type - embedded map block to be sent
  - Added [`aiogram.types.input_rich_block_animation.InputRichBlockAnimation`](api/types/input_rich_block_animation.html#aiogram.types.input_rich_block_animation.InputRichBlockAnimation "aiogram.types.input_rich_block_animation.InputRichBlockAnimation") type - animation (GIF) block to be sent
  - Added [`aiogram.types.input_rich_block_audio.InputRichBlockAudio`](api/types/input_rich_block_audio.html#aiogram.types.input_rich_block_audio.InputRichBlockAudio "aiogram.types.input_rich_block_audio.InputRichBlockAudio") type - audio block to be sent
  - Added [`aiogram.types.input_rich_block_photo.InputRichBlockPhoto`](api/types/input_rich_block_photo.html#aiogram.types.input_rich_block_photo.InputRichBlockPhoto "aiogram.types.input_rich_block_photo.InputRichBlockPhoto") type - photo block to be sent
  - Added [`aiogram.types.input_rich_block_video.InputRichBlockVideo`](api/types/input_rich_block_video.html#aiogram.types.input_rich_block_video.InputRichBlockVideo "aiogram.types.input_rich_block_video.InputRichBlockVideo") type - video block to be sent
  - Added [`aiogram.types.input_rich_block_voice_note.InputRichBlockVoiceNote`](api/types/input_rich_block_voice_note.html#aiogram.types.input_rich_block_voice_note.InputRichBlockVoiceNote "aiogram.types.input_rich_block_voice_note.InputRichBlockVoiceNote") type - voice note block to be sent
  - Added [`aiogram.types.input_rich_block_thinking.InputRichBlockThinking`](api/types/input_rich_block_thinking.html#aiogram.types.input_rich_block_thinking.InputRichBlockThinking "aiogram.types.input_rich_block_thinking.InputRichBlockThinking") type - thinking/reasoning block for AI-generated content to be sent

  *New Fields:*

  - Added `blocks` field to [`aiogram.types.input_rich_message.InputRichMessage`](api/types/input_rich_message.html#aiogram.types.input_rich_message.InputRichMessage "aiogram.types.input_rich_message.InputRichMessage") - list of rich blocks the message is composed of
  - Added `media` field to [`aiogram.types.input_rich_message.InputRichMessage`](api/types/input_rich_message.html#aiogram.types.input_rich_message.InputRichMessage "aiogram.types.input_rich_message.InputRichMessage") - list of media items attached to the message

  **Ephemeral Messages**

  *New Methods:*

  - Added [`aiogram.methods.edit_ephemeral_message_text.EditEphemeralMessageText`](api/methods/edit_ephemeral_message_text.html#aiogram.methods.edit_ephemeral_message_text.EditEphemeralMessageText "aiogram.methods.edit_ephemeral_message_text.EditEphemeralMessageText") method - edits the text of an ephemeral message
  - Added [`aiogram.methods.edit_ephemeral_message_caption.EditEphemeralMessageCaption`](api/methods/edit_ephemeral_message_caption.html#aiogram.methods.edit_ephemeral_message_caption.EditEphemeralMessageCaption "aiogram.methods.edit_ephemeral_message_caption.EditEphemeralMessageCaption") method - edits the caption of an ephemeral message
  - Added [`aiogram.methods.edit_ephemeral_message_media.EditEphemeralMessageMedia`](api/methods/edit_ephemeral_message_media.html#aiogram.methods.edit_ephemeral_message_media.EditEphemeralMessageMedia "aiogram.methods.edit_ephemeral_message_media.EditEphemeralMessageMedia") method - replaces the media of an ephemeral message
  - Added [`aiogram.methods.edit_ephemeral_message_reply_markup.EditEphemeralMessageReplyMarkup`](api/methods/edit_ephemeral_message_reply_markup.html#aiogram.methods.edit_ephemeral_message_reply_markup.EditEphemeralMessageReplyMarkup "aiogram.methods.edit_ephemeral_message_reply_markup.EditEphemeralMessageReplyMarkup") method - edits the reply markup of an ephemeral message
  - Added [`aiogram.methods.delete_ephemeral_message.DeleteEphemeralMessage`](api/methods/delete_ephemeral_message.html#aiogram.methods.delete_ephemeral_message.DeleteEphemeralMessage "aiogram.methods.delete_ephemeral_message.DeleteEphemeralMessage") method - deletes an ephemeral message

  *New Fields:*

  - Added `is_ephemeral` field to [`aiogram.types.bot_command.BotCommand`](api/types/bot_command.html#aiogram.types.bot_command.BotCommand "aiogram.types.bot_command.BotCommand") - indicates whether the command produces an ephemeral message
  - Added `receiver_user` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - the user an ephemeral message is shown to
  - Added `ephemeral_message_id` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - identifier of the ephemeral message, unique for its receiver
  - Added `ephemeral_message_id` field to [`aiogram.types.reply_parameters.ReplyParameters`](api/types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") - identifier of the ephemeral message to reply to

  *New Shortcuts:*

  - Added [`aiogram.types.message.Message.edit_ephemeral_text()`](api/types/message.html#aiogram.types.message.Message.edit_ephemeral_text "aiogram.types.message.Message.edit_ephemeral_text") shortcut - edits the text of an ephemeral message
  - Added [`aiogram.types.message.Message.edit_ephemeral_caption()`](api/types/message.html#aiogram.types.message.Message.edit_ephemeral_caption "aiogram.types.message.Message.edit_ephemeral_caption") shortcut - edits the caption of an ephemeral message
  - Added [`aiogram.types.message.Message.edit_ephemeral_media()`](api/types/message.html#aiogram.types.message.Message.edit_ephemeral_media "aiogram.types.message.Message.edit_ephemeral_media") shortcut - replaces the media of an ephemeral message
  - Added [`aiogram.types.message.Message.edit_ephemeral_reply_markup()`](api/types/message.html#aiogram.types.message.Message.edit_ephemeral_reply_markup "aiogram.types.message.Message.edit_ephemeral_reply_markup") shortcut - edits the reply markup of an ephemeral message
  - Added [`aiogram.types.message.Message.delete_ephemeral()`](api/types/message.html#aiogram.types.message.Message.delete_ephemeral "aiogram.types.message.Message.delete_ephemeral") shortcut - deletes an ephemeral message

    All of them fill `chat_id`, `receiver_user_id` and `ephemeral_message_id` from the message itself.

  *Changed Shortcuts:*

  - [`aiogram.types.message.Message.as_reply_parameters()`](api/types/message.html#aiogram.types.message.Message.as_reply_parameters "aiogram.types.message.Message.as_reply_parameters") now targets an ephemeral message by its `ephemeral_message_id` instead of `message_id`/`chat_id` - an ephemeral message has `message_id` equal to 0, and `chat_id` is not supported for it
  - The `reply_*` shortcuts of [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") now fill `receiver_user_id` automatically, because a reply to an ephemeral message must itself be an ephemeral message. As a result they no longer accept `receiver_user_id` as an argument. To send an ephemeral message *in reply to a regular one*, use [`aiogram.types.message.Message.answer()`](api/types/message.html#aiogram.types.message.Message.answer "aiogram.types.message.Message.answer") with an explicit `receiver_user_id` and `reply_parameters`.

  *Changed Fields:*

  - `message_id` in [`aiogram.types.reply_parameters.ReplyParameters`](api/types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") is now **optional** (`int | None`) - it may be omitted when `ephemeral_message_id` is specified instead

  *New Parameters for* [`aiogram.methods.send_message.SendMessage`](api/methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage"), [`aiogram.methods.send_photo.SendPhoto`](api/methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto"), [`aiogram.methods.send_video.SendVideo`](api/methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo"), [`aiogram.methods.send_animation.SendAnimation`](api/methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation"), [`aiogram.methods.send_audio.SendAudio`](api/methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio"), [`aiogram.methods.send_document.SendDocument`](api/methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument"), [`aiogram.methods.send_sticker.SendSticker`](api/methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker"), [`aiogram.methods.send_voice.SendVoice`](api/methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice"), [`aiogram.methods.send_video_note.SendVideoNote`](api/methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote"), [`aiogram.methods.send_live_photo.SendLivePhoto`](api/methods/send_live_photo.html#aiogram.methods.send_live_photo.SendLivePhoto "aiogram.methods.send_live_photo.SendLivePhoto"), [`aiogram.methods.send_location.SendLocation`](api/methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation"), [`aiogram.methods.send_venue.SendVenue`](api/methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue") *and* [`aiogram.methods.send_contact.SendContact`](api/methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact"):

  - Added `receiver_user_id` - sends the message as an ephemeral message visible only to the specified user
  - Added `callback_query_id` - identifier of the callback query the ephemeral message is sent in response to

  **Communities**

  *New Types:*

  - Added [`aiogram.types.community.Community`](api/types/community.html#aiogram.types.community.Community "aiogram.types.community.Community") type - represents a community (a group of chats)
  - Added [`aiogram.types.community_chat_added.CommunityChatAdded`](api/types/community_chat_added.html#aiogram.types.community_chat_added.CommunityChatAdded "aiogram.types.community_chat_added.CommunityChatAdded") type - service message about a chat being added to a community
  - Added [`aiogram.types.community_chat_removed.CommunityChatRemoved`](api/types/community_chat_removed.html#aiogram.types.community_chat_removed.CommunityChatRemoved "aiogram.types.community_chat_removed.CommunityChatRemoved") type - service message about a chat being removed from a community

  *New Fields:*

  - Added `community` field to [`aiogram.types.chat_full_info.ChatFullInfo`](api/types/chat_full_info.html#aiogram.types.chat_full_info.ChatFullInfo "aiogram.types.chat_full_info.ChatFullInfo") - the community the chat belongs to, if any
  - Added `community_chat_added` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - service message: chat added to a community
  - Added `community_chat_removed` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - service message: chat removed from a community

  **General**

  *New Types:*

  - Added [`aiogram.types.bot_subscription_updated.BotSubscriptionUpdated`](api/types/bot_subscription_updated.html#aiogram.types.bot_subscription_updated.BotSubscriptionUpdated "aiogram.types.bot_subscription_updated.BotSubscriptionUpdated") type - describes a change to a user payment subscription toward the bot

  *New Fields:*

  - Added `subscription` field to [`aiogram.types.update.Update`](api/types/update.html#aiogram.types.update.Update "aiogram.types.update.Update") - user payment subscription has changed; dispatched as the new `subscription` event, so handlers can be registered via `@router.subscription()`

  [#1852](https://github.com/aiogram/aiogram/issues/1852)

## 3.29.1 (2026-07-02)

### Bugfixes

- Fixed severe (exponential) slowdown when validating nested [`aiogram.types.rich_block.RichBlock`](api/types/rich_block.html#aiogram.types.rich_block.RichBlock "aiogram.types.rich_block.RichBlock")
  structures (e.g. nested `blockquote`/`collage`/`details` blocks).
  Subtype unions whose members share a unique constant tag field (`RichBlockUnion`, `ReactionTypeUnion`,
  `ChatMemberUnion`, `MessageOriginUnion` and others) are now generated as Pydantic *discriminated* unions
  keyed on that field (`type`/`status`/`source`), so the correct member is selected directly instead of
  being found via smart-union backtracking.
  [#1842](https://github.com/aiogram/aiogram/issues/1842)

## 3.29.0 (2026-06-14)

### Misc

- Updated to [Bot API 10.1](https://core.telegram.org/bots/api-changelog#june-11-2026)

  **Rich Messages**

  *New Methods:*

  - Added [`aiogram.methods.send_rich_message.SendRichMessage`](api/methods/send_rich_message.html#aiogram.methods.send_rich_message.SendRichMessage "aiogram.methods.send_rich_message.SendRichMessage") method - sends a rich formatted message to a chat
  - Added [`aiogram.methods.send_rich_message_draft.SendRichMessageDraft`](api/methods/send_rich_message_draft.html#aiogram.methods.send_rich_message_draft.SendRichMessageDraft "aiogram.methods.send_rich_message_draft.SendRichMessageDraft") method - streams a partial rich message draft to a user while the message is being generated

  *New Types:*

  - Added [`aiogram.types.rich_message.RichMessage`](api/types/rich_message.html#aiogram.types.rich_message.RichMessage "aiogram.types.rich_message.RichMessage") type - represents a rich formatted message received in a chat
  - Added [`aiogram.types.input_rich_message.InputRichMessage`](api/types/input_rich_message.html#aiogram.types.input_rich_message.InputRichMessage "aiogram.types.input_rich_message.InputRichMessage") type - describes a rich message to be sent, using HTML or Markdown formatting
  - Added [`aiogram.types.input_rich_message_content.InputRichMessageContent`](api/types/input_rich_message_content.html#aiogram.types.input_rich_message_content.InputRichMessageContent "aiogram.types.input_rich_message_content.InputRichMessageContent") type - inline query result content backed by a rich message
  - Added [`aiogram.types.rich_text.RichText`](api/types/rich_text.html#aiogram.types.rich_text.RichText "aiogram.types.rich_text.RichText") type - base class for all rich text formatting nodes
  - Added [`aiogram.types.rich_text_bold.RichTextBold`](api/types/rich_text_bold.html#aiogram.types.rich_text_bold.RichTextBold "aiogram.types.rich_text_bold.RichTextBold") type - bold rich text node
  - Added [`aiogram.types.rich_text_italic.RichTextItalic`](api/types/rich_text_italic.html#aiogram.types.rich_text_italic.RichTextItalic "aiogram.types.rich_text_italic.RichTextItalic") type - italic rich text node
  - Added [`aiogram.types.rich_text_underline.RichTextUnderline`](api/types/rich_text_underline.html#aiogram.types.rich_text_underline.RichTextUnderline "aiogram.types.rich_text_underline.RichTextUnderline") type - underline rich text node
  - Added [`aiogram.types.rich_text_strikethrough.RichTextStrikethrough`](api/types/rich_text_strikethrough.html#aiogram.types.rich_text_strikethrough.RichTextStrikethrough "aiogram.types.rich_text_strikethrough.RichTextStrikethrough") type - strikethrough rich text node
  - Added [`aiogram.types.rich_text_spoiler.RichTextSpoiler`](api/types/rich_text_spoiler.html#aiogram.types.rich_text_spoiler.RichTextSpoiler "aiogram.types.rich_text_spoiler.RichTextSpoiler") type - spoiler rich text node
  - Added [`aiogram.types.rich_text_date_time.RichTextDateTime`](api/types/rich_text_date_time.html#aiogram.types.rich_text_date_time.RichTextDateTime "aiogram.types.rich_text_date_time.RichTextDateTime") type - date/time rich text node
  - Added [`aiogram.types.rich_text_text_mention.RichTextTextMention`](api/types/rich_text_text_mention.html#aiogram.types.rich_text_text_mention.RichTextTextMention "aiogram.types.rich_text_text_mention.RichTextTextMention") type - text mention rich text node
  - Added [`aiogram.types.rich_text_subscript.RichTextSubscript`](api/types/rich_text_subscript.html#aiogram.types.rich_text_subscript.RichTextSubscript "aiogram.types.rich_text_subscript.RichTextSubscript") type - subscript rich text node
  - Added [`aiogram.types.rich_text_superscript.RichTextSuperscript`](api/types/rich_text_superscript.html#aiogram.types.rich_text_superscript.RichTextSuperscript "aiogram.types.rich_text_superscript.RichTextSuperscript") type - superscript rich text node
  - Added [`aiogram.types.rich_text_marked.RichTextMarked`](api/types/rich_text_marked.html#aiogram.types.rich_text_marked.RichTextMarked "aiogram.types.rich_text_marked.RichTextMarked") type - highlighted/marked rich text node
  - Added [`aiogram.types.rich_text_code.RichTextCode`](api/types/rich_text_code.html#aiogram.types.rich_text_code.RichTextCode "aiogram.types.rich_text_code.RichTextCode") type - inline code rich text node
  - Added [`aiogram.types.rich_text_custom_emoji.RichTextCustomEmoji`](api/types/rich_text_custom_emoji.html#aiogram.types.rich_text_custom_emoji.RichTextCustomEmoji "aiogram.types.rich_text_custom_emoji.RichTextCustomEmoji") type - custom emoji rich text node
  - Added [`aiogram.types.rich_text_mathematical_expression.RichTextMathematicalExpression`](api/types/rich_text_mathematical_expression.html#aiogram.types.rich_text_mathematical_expression.RichTextMathematicalExpression "aiogram.types.rich_text_mathematical_expression.RichTextMathematicalExpression") type - mathematical expression rich text node
  - Added [`aiogram.types.rich_text_url.RichTextUrl`](api/types/rich_text_url.html#aiogram.types.rich_text_url.RichTextUrl "aiogram.types.rich_text_url.RichTextUrl") type - URL rich text node
  - Added [`aiogram.types.rich_text_email_address.RichTextEmailAddress`](api/types/rich_text_email_address.html#aiogram.types.rich_text_email_address.RichTextEmailAddress "aiogram.types.rich_text_email_address.RichTextEmailAddress") type - email address rich text node
  - Added [`aiogram.types.rich_text_phone_number.RichTextPhoneNumber`](api/types/rich_text_phone_number.html#aiogram.types.rich_text_phone_number.RichTextPhoneNumber "aiogram.types.rich_text_phone_number.RichTextPhoneNumber") type - phone number rich text node
  - Added [`aiogram.types.rich_text_bank_card_number.RichTextBankCardNumber`](api/types/rich_text_bank_card_number.html#aiogram.types.rich_text_bank_card_number.RichTextBankCardNumber "aiogram.types.rich_text_bank_card_number.RichTextBankCardNumber") type - bank card number rich text node
  - Added [`aiogram.types.rich_text_mention.RichTextMention`](api/types/rich_text_mention.html#aiogram.types.rich_text_mention.RichTextMention "aiogram.types.rich_text_mention.RichTextMention") type - user mention rich text node
  - Added [`aiogram.types.rich_text_hashtag.RichTextHashtag`](api/types/rich_text_hashtag.html#aiogram.types.rich_text_hashtag.RichTextHashtag "aiogram.types.rich_text_hashtag.RichTextHashtag") type - hashtag rich text node
  - Added [`aiogram.types.rich_text_cashtag.RichTextCashtag`](api/types/rich_text_cashtag.html#aiogram.types.rich_text_cashtag.RichTextCashtag "aiogram.types.rich_text_cashtag.RichTextCashtag") type - cashtag rich text node
  - Added [`aiogram.types.rich_text_bot_command.RichTextBotCommand`](api/types/rich_text_bot_command.html#aiogram.types.rich_text_bot_command.RichTextBotCommand "aiogram.types.rich_text_bot_command.RichTextBotCommand") type - bot command rich text node
  - Added [`aiogram.types.rich_text_anchor.RichTextAnchor`](api/types/rich_text_anchor.html#aiogram.types.rich_text_anchor.RichTextAnchor "aiogram.types.rich_text_anchor.RichTextAnchor") type - anchor (named target) rich text node
  - Added [`aiogram.types.rich_text_anchor_link.RichTextAnchorLink`](api/types/rich_text_anchor_link.html#aiogram.types.rich_text_anchor_link.RichTextAnchorLink "aiogram.types.rich_text_anchor_link.RichTextAnchorLink") type - link to an in-message anchor rich text node
  - Added [`aiogram.types.rich_text_reference.RichTextReference`](api/types/rich_text_reference.html#aiogram.types.rich_text_reference.RichTextReference "aiogram.types.rich_text_reference.RichTextReference") type - footnote reference rich text node
  - Added [`aiogram.types.rich_text_reference_link.RichTextReferenceLink`](api/types/rich_text_reference_link.html#aiogram.types.rich_text_reference_link.RichTextReferenceLink "aiogram.types.rich_text_reference_link.RichTextReferenceLink") type - link to a footnote reference rich text node
  - Added [`aiogram.types.rich_block.RichBlock`](api/types/rich_block.html#aiogram.types.rich_block.RichBlock "aiogram.types.rich_block.RichBlock") type - base class for all rich block elements
  - Added [`aiogram.types.rich_block_paragraph.RichBlockParagraph`](api/types/rich_block_paragraph.html#aiogram.types.rich_block_paragraph.RichBlockParagraph "aiogram.types.rich_block_paragraph.RichBlockParagraph") type - text paragraph block
  - Added [`aiogram.types.rich_block_section_heading.RichBlockSectionHeading`](api/types/rich_block_section_heading.html#aiogram.types.rich_block_section_heading.RichBlockSectionHeading "aiogram.types.rich_block_section_heading.RichBlockSectionHeading") type - section heading block
  - Added [`aiogram.types.rich_block_preformatted.RichBlockPreformatted`](api/types/rich_block_preformatted.html#aiogram.types.rich_block_preformatted.RichBlockPreformatted "aiogram.types.rich_block_preformatted.RichBlockPreformatted") type - preformatted (code) block
  - Added [`aiogram.types.rich_block_footer.RichBlockFooter`](api/types/rich_block_footer.html#aiogram.types.rich_block_footer.RichBlockFooter "aiogram.types.rich_block_footer.RichBlockFooter") type - footer block
  - Added [`aiogram.types.rich_block_divider.RichBlockDivider`](api/types/rich_block_divider.html#aiogram.types.rich_block_divider.RichBlockDivider "aiogram.types.rich_block_divider.RichBlockDivider") type - horizontal divider block
  - Added [`aiogram.types.rich_block_mathematical_expression.RichBlockMathematicalExpression`](api/types/rich_block_mathematical_expression.html#aiogram.types.rich_block_mathematical_expression.RichBlockMathematicalExpression "aiogram.types.rich_block_mathematical_expression.RichBlockMathematicalExpression") type - mathematical expression block
  - Added [`aiogram.types.rich_block_anchor.RichBlockAnchor`](api/types/rich_block_anchor.html#aiogram.types.rich_block_anchor.RichBlockAnchor "aiogram.types.rich_block_anchor.RichBlockAnchor") type - anchor/target block
  - Added [`aiogram.types.rich_block_list.RichBlockList`](api/types/rich_block_list.html#aiogram.types.rich_block_list.RichBlockList "aiogram.types.rich_block_list.RichBlockList") type - ordered or unordered list block
  - Added [`aiogram.types.rich_block_block_quotation.RichBlockBlockQuotation`](api/types/rich_block_block_quotation.html#aiogram.types.rich_block_block_quotation.RichBlockBlockQuotation "aiogram.types.rich_block_block_quotation.RichBlockBlockQuotation") type - block quotation block
  - Added [`aiogram.types.rich_block_pull_quotation.RichBlockPullQuotation`](api/types/rich_block_pull_quotation.html#aiogram.types.rich_block_pull_quotation.RichBlockPullQuotation "aiogram.types.rich_block_pull_quotation.RichBlockPullQuotation") type - pull quotation block
  - Added [`aiogram.types.rich_block_collage.RichBlockCollage`](api/types/rich_block_collage.html#aiogram.types.rich_block_collage.RichBlockCollage "aiogram.types.rich_block_collage.RichBlockCollage") type - collage of media items block
  - Added [`aiogram.types.rich_block_slideshow.RichBlockSlideshow`](api/types/rich_block_slideshow.html#aiogram.types.rich_block_slideshow.RichBlockSlideshow "aiogram.types.rich_block_slideshow.RichBlockSlideshow") type - slideshow block
  - Added [`aiogram.types.rich_block_table.RichBlockTable`](api/types/rich_block_table.html#aiogram.types.rich_block_table.RichBlockTable "aiogram.types.rich_block_table.RichBlockTable") type - table block
  - Added [`aiogram.types.rich_block_details.RichBlockDetails`](api/types/rich_block_details.html#aiogram.types.rich_block_details.RichBlockDetails "aiogram.types.rich_block_details.RichBlockDetails") type - expandable details/summary block
  - Added [`aiogram.types.rich_block_map.RichBlockMap`](api/types/rich_block_map.html#aiogram.types.rich_block_map.RichBlockMap "aiogram.types.rich_block_map.RichBlockMap") type - embedded map block
  - Added [`aiogram.types.rich_block_animation.RichBlockAnimation`](api/types/rich_block_animation.html#aiogram.types.rich_block_animation.RichBlockAnimation "aiogram.types.rich_block_animation.RichBlockAnimation") type - animation (GIF) block
  - Added [`aiogram.types.rich_block_audio.RichBlockAudio`](api/types/rich_block_audio.html#aiogram.types.rich_block_audio.RichBlockAudio "aiogram.types.rich_block_audio.RichBlockAudio") type - audio block
  - Added [`aiogram.types.rich_block_photo.RichBlockPhoto`](api/types/rich_block_photo.html#aiogram.types.rich_block_photo.RichBlockPhoto "aiogram.types.rich_block_photo.RichBlockPhoto") type - photo block
  - Added [`aiogram.types.rich_block_video.RichBlockVideo`](api/types/rich_block_video.html#aiogram.types.rich_block_video.RichBlockVideo "aiogram.types.rich_block_video.RichBlockVideo") type - video block
  - Added [`aiogram.types.rich_block_voice_note.RichBlockVoiceNote`](api/types/rich_block_voice_note.html#aiogram.types.rich_block_voice_note.RichBlockVoiceNote "aiogram.types.rich_block_voice_note.RichBlockVoiceNote") type - voice note block
  - Added [`aiogram.types.rich_block_thinking.RichBlockThinking`](api/types/rich_block_thinking.html#aiogram.types.rich_block_thinking.RichBlockThinking "aiogram.types.rich_block_thinking.RichBlockThinking") type - thinking/reasoning block for AI-generated content
  - Added [`aiogram.types.rich_block_caption.RichBlockCaption`](api/types/rich_block_caption.html#aiogram.types.rich_block_caption.RichBlockCaption "aiogram.types.rich_block_caption.RichBlockCaption") type - caption for a rich block media element
  - Added [`aiogram.types.rich_block_list_item.RichBlockListItem`](api/types/rich_block_list_item.html#aiogram.types.rich_block_list_item.RichBlockListItem "aiogram.types.rich_block_list_item.RichBlockListItem") type - individual item in a rich block list
  - Added [`aiogram.types.rich_block_table_cell.RichBlockTableCell`](api/types/rich_block_table_cell.html#aiogram.types.rich_block_table_cell.RichBlockTableCell "aiogram.types.rich_block_table_cell.RichBlockTableCell") type - individual cell in a rich block table

  *New Fields:*

  - Added `rich_message` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - the rich formatted message contained in the message

  *New Parameters for* [`aiogram.methods.edit_message_text.EditMessageText`](api/methods/edit_message_text.html#aiogram.methods.edit_message_text.EditMessageText "aiogram.methods.edit_message_text.EditMessageText"):

  - Added `rich_message` - new rich content of the message; required if `text` is not specified

  *Changed Parameters for* [`aiogram.methods.edit_message_text.EditMessageText`](api/methods/edit_message_text.html#aiogram.methods.edit_message_text.EditMessageText "aiogram.methods.edit_message_text.EditMessageText"):

  - `text` is now **optional** (`str | None`) — previously it was a required positional argument; now either `text` or `rich_message` must be provided.

  **Join Request Queries**

  *New Methods:*

  - Added [`aiogram.methods.answer_chat_join_request_query.AnswerChatJoinRequestQuery`](api/methods/answer_chat_join_request_query.html#aiogram.methods.answer_chat_join_request_query.AnswerChatJoinRequestQuery "aiogram.methods.answer_chat_join_request_query.AnswerChatJoinRequestQuery") method - processes a received chat join request query
  - Added [`aiogram.methods.send_chat_join_request_web_app.SendChatJoinRequestWebApp`](api/methods/send_chat_join_request_web_app.html#aiogram.methods.send_chat_join_request_web_app.SendChatJoinRequestWebApp "aiogram.methods.send_chat_join_request_web_app.SendChatJoinRequestWebApp") method - processes a join request query by showing a Mini App to the user before deciding the outcome

  *New Shortcuts:*

  - Added [`aiogram.types.chat_join_request.ChatJoinRequest.answer_query()`](api/types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.answer_query "aiogram.types.chat_join_request.ChatJoinRequest.answer_query") shortcut - answers a join request query using the request’s `query_id`
  - Added [`aiogram.types.chat_join_request.ChatJoinRequest.send_webapp()`](api/types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest.send_webapp "aiogram.types.chat_join_request.ChatJoinRequest.send_webapp") shortcut - shows a Mini App to the user for a join request query using the request’s `query_id`

  *New Fields:*

  - Added `supports_join_request_queries` field to [`aiogram.types.user.User`](api/types/user.html#aiogram.types.user.User "aiogram.types.user.User") - indicates whether the user supports join request queries
  - Added `guard_bot` field to [`aiogram.types.chat_full_info.ChatFullInfo`](api/types/chat_full_info.html#aiogram.types.chat_full_info.ChatFullInfo "aiogram.types.chat_full_info.ChatFullInfo") - the guard bot configured for the chat, if any
  - Added `query_id` field to [`aiogram.types.chat_join_request.ChatJoinRequest`](api/types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest "aiogram.types.chat_join_request.ChatJoinRequest") - unique identifier of the join request query

  **Polls**

  *New Types:*

  - Added [`aiogram.types.link.Link`](api/types/link.html#aiogram.types.link.Link "aiogram.types.link.Link") type - represents a hyperlink for use in poll media
  - Added [`aiogram.types.input_media_link.InputMediaLink`](api/types/input_media_link.html#aiogram.types.input_media_link.InputMediaLink "aiogram.types.input_media_link.InputMediaLink") type - represents a link as poll option media input

  *New Fields:*

  - Added `link` field to [`aiogram.types.poll_media.PollMedia`](api/types/poll_media.html#aiogram.types.poll_media.PollMedia "aiogram.types.poll_media.PollMedia") - hyperlink associated with the poll media

  [#1830](https://github.com/aiogram/aiogram/issues/1830)

## 3.28.1 and 3.28.2 (2026-05-10)

### Bugfixes

- Fixed [`aiogram.types.input_poll_option.InputPollOption`](api/types/input_poll_option.html#aiogram.types.input_poll_option.InputPollOption "aiogram.types.input_poll_option.InputPollOption") rejecting [`aiogram.types.input_media_photo.InputMediaPhoto`](api/types/input_media_photo.html#aiogram.types.input_media_photo.InputMediaPhoto "aiogram.types.input_media_photo.InputMediaPhoto") (and other `InputMedia*` subclasses) for the `media` field. Added `aiogram.types.input_poll_option_media_union.InputPollOptionMediaUnion` type alias and made all valid media classes inherit from [`aiogram.types.input_poll_option_media.InputPollOptionMedia`](api/types/input_poll_option_media.html#aiogram.types.input_poll_option_media.InputPollOptionMedia "aiogram.types.input_poll_option_media.InputPollOptionMedia").
  [#1808](https://github.com/aiogram/aiogram/issues/1808)

## 3.28.0 (2026-05-09)

### Bugfixes

- Added the `link_preview_options` parameter to [`aiogram.types.message.Message.send_copy()`](api/types/message.html#aiogram.types.message.Message.send_copy "aiogram.types.message.Message.send_copy"). When copying a text message, the new parameter is forwarded to [`aiogram.methods.send_message.SendMessage`](api/methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage"); if it is not provided, the original message’s `link_preview_options` are used as a fallback.
  [#1620](https://github.com/aiogram/aiogram/issues/1620)

### Improved Documentation

- Improve grammar in MemoryStorage, PyMongoStorage, and RedisStorage docstrings.
  [#1796](https://github.com/aiogram/aiogram/issues/1796)

### Deprecations and Removals

- Dropped PyPy 3.10 support because required optional dependencies no longer support it.
  [#1805](https://github.com/aiogram/aiogram/issues/1805)

### Misc

- Bumped upper version bounds for `pydantic` (`<2.14`) and `pymongo` (`<4.17`); refreshed dev/test dependencies (`ruff`, `packaging`, `pytest`, `pytest-html`, `pytest-cov`, `pytz`).
  [#1795](https://github.com/aiogram/aiogram/issues/1795)
- Bump `ruff` pre-commit hook from `v0.14.0` to `v0.15.11` and rename hook id from `ruff` to `ruff-check`
  [#1801](https://github.com/aiogram/aiogram/issues/1801)
- Bumped `mypy` to `2.0.0` and fixed typing issues reported by the new version.
  [#1804](https://github.com/aiogram/aiogram/issues/1804)
- Updated to [Bot API 10.0](https://core.telegram.org/bots/api-changelog#may-8-2026)

  **Guest Mode**

  *New Methods:*

  - Added [`aiogram.methods.answer_guest_query.AnswerGuestQuery`](api/methods/answer_guest_query.html#aiogram.methods.answer_guest_query.AnswerGuestQuery "aiogram.methods.answer_guest_query.AnswerGuestQuery") method - enables bots to respond to queries from users browsing outside the chat

  *New Types:*

  - Added [`aiogram.types.sent_guest_message.SentGuestMessage`](api/types/sent_guest_message.html#aiogram.types.sent_guest_message.SentGuestMessage "aiogram.types.sent_guest_message.SentGuestMessage") type - represents a message sent in response to a guest query

  *New Shortcuts:*

  - Added [`aiogram.types.message.Message.answer_guest_query()`](api/types/message.html#aiogram.types.message.Message.answer_guest_query "aiogram.types.message.Message.answer_guest_query") shortcut on [`Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - replies to a guest query using the message’s `guest_query_id`

  *New Router handlers:*

  - Added `Router.guest_message` observer - handles incoming `guest_message` updates

  *New Fields:*

  - Added `supports_guest_queries` field to [`aiogram.types.user.User`](api/types/user.html#aiogram.types.user.User "aiogram.types.user.User") - indicates whether the user supports guest queries
  - Added `guest_bot_caller_user` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - the user who initiated the guest interaction
  - Added `guest_bot_caller_chat` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - the chat context of the guest query
  - Added `guest_query_id` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - identifier of the guest query
  - Added `guest_message` field to [`aiogram.types.update.Update`](api/types/update.html#aiogram.types.update.Update "aiogram.types.update.Update") - contains a guest-related message update

  **Chat Management**

  *New Methods:*

  - Added [`aiogram.methods.delete_all_message_reactions.DeleteAllMessageReactions`](api/methods/delete_all_message_reactions.html#aiogram.methods.delete_all_message_reactions.DeleteAllMessageReactions "aiogram.methods.delete_all_message_reactions.DeleteAllMessageReactions") method - removes all reactions from a message
  - Added [`aiogram.methods.delete_message_reaction.DeleteMessageReaction`](api/methods/delete_message_reaction.html#aiogram.methods.delete_message_reaction.DeleteMessageReaction "aiogram.methods.delete_message_reaction.DeleteMessageReaction") method - removes a specific reaction from a message

  *New Fields:*

  - Added `can_react_to_messages` field to [`aiogram.types.chat_member_restricted.ChatMemberRestricted`](api/types/chat_member_restricted.html#aiogram.types.chat_member_restricted.ChatMemberRestricted "aiogram.types.chat_member_restricted.ChatMemberRestricted") - indicates whether the restricted member is allowed to react to messages
  - Added `can_react_to_messages` field to [`aiogram.types.chat_permissions.ChatPermissions`](api/types/chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions") - controls whether chat members can react to messages

  *New Parameters for* [`aiogram.methods.get_chat_administrators.GetChatAdministrators`](api/methods/get_chat_administrators.html#aiogram.methods.get_chat_administrators.GetChatAdministrators "aiogram.methods.get_chat_administrators.GetChatAdministrators"):

  - Added `return_bots` - when `True`, bot administrators are included in the returned list

  **Polls**

  *New Types:*

  - Added [`aiogram.types.poll_media.PollMedia`](api/types/poll_media.html#aiogram.types.poll_media.PollMedia "aiogram.types.poll_media.PollMedia") type - represents media attached to a poll or quiz explanation
  - Added [`aiogram.types.input_poll_media.InputPollMedia`](api/types/input_poll_media.html#aiogram.types.input_poll_media.InputPollMedia "aiogram.types.input_poll_media.InputPollMedia") type - input for media to attach to a poll
  - Added [`aiogram.types.input_poll_option_media.InputPollOptionMedia`](api/types/input_poll_option_media.html#aiogram.types.input_poll_option_media.InputPollOptionMedia "aiogram.types.input_poll_option_media.InputPollOptionMedia") type - input for media to attach to a poll option
  - Added [`aiogram.types.input_media_sticker.InputMediaSticker`](api/types/input_media_sticker.html#aiogram.types.input_media_sticker.InputMediaSticker "aiogram.types.input_media_sticker.InputMediaSticker") type - represents a sticker as poll media input
  - Added [`aiogram.types.input_media_location.InputMediaLocation`](api/types/input_media_location.html#aiogram.types.input_media_location.InputMediaLocation "aiogram.types.input_media_location.InputMediaLocation") type - represents a location as poll media input
  - Added [`aiogram.types.input_media_venue.InputMediaVenue`](api/types/input_media_venue.html#aiogram.types.input_media_venue.InputMediaVenue "aiogram.types.input_media_venue.InputMediaVenue") type - represents a venue as poll media input

  *New Fields:*

  - Added `media` field to [`aiogram.types.poll.Poll`](api/types/poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") - media content attached to the poll
  - Added `explanation_media` field to [`aiogram.types.poll.Poll`](api/types/poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") - media shown as the quiz explanation
  - Added `members_only` field to [`aiogram.types.poll.Poll`](api/types/poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") - indicates the poll is restricted to chat members
  - Added `country_codes` field to [`aiogram.types.poll.Poll`](api/types/poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") - list of country codes for geographic filtering
  - Added `media` field to [`aiogram.types.poll_option.PollOption`](api/types/poll_option.html#aiogram.types.poll_option.PollOption "aiogram.types.poll_option.PollOption") - media associated with the poll option

  *New Parameters for* [`aiogram.methods.send_poll.SendPoll`](api/methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll"):

  - Added `media` - media to attach to the poll
  - Added `explanation_media` - media to display as the quiz explanation
  - Added `members_only` - restricts the poll to chat members
  - Added `country_codes` - list of country codes for geographic filtering

  **Live Photos**

  *New Methods:*

  - Added [`aiogram.methods.send_live_photo.SendLivePhoto`](api/methods/send_live_photo.html#aiogram.methods.send_live_photo.SendLivePhoto "aiogram.methods.send_live_photo.SendLivePhoto") method - sends a live photo (a photo with a short embedded video)

  *New Types:*

  - Added [`aiogram.types.live_photo.LivePhoto`](api/types/live_photo.html#aiogram.types.live_photo.LivePhoto "aiogram.types.live_photo.LivePhoto") type - represents a live photo
  - Added [`aiogram.types.input_media_live_photo.InputMediaLivePhoto`](api/types/input_media_live_photo.html#aiogram.types.input_media_live_photo.InputMediaLivePhoto "aiogram.types.input_media_live_photo.InputMediaLivePhoto") type - input for sending a live photo as part of a media group
  - Added [`aiogram.types.paid_media_live_photo.PaidMediaLivePhoto`](api/types/paid_media_live_photo.html#aiogram.types.paid_media_live_photo.PaidMediaLivePhoto "aiogram.types.paid_media_live_photo.PaidMediaLivePhoto") type - represents a live photo as paid media
  - Added [`aiogram.types.input_paid_media_live_photo.InputPaidMediaLivePhoto`](api/types/input_paid_media_live_photo.html#aiogram.types.input_paid_media_live_photo.InputPaidMediaLivePhoto "aiogram.types.input_paid_media_live_photo.InputPaidMediaLivePhoto") type - input for sending a live photo as paid media

  *New Fields:*

  - Added `live_photo` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - the live photo contained in the message
  - Added `live_photo` field to [`aiogram.types.external_reply_info.ExternalReplyInfo`](api/types/external_reply_info.html#aiogram.types.external_reply_info.ExternalReplyInfo "aiogram.types.external_reply_info.ExternalReplyInfo") - live photo referenced in an external reply

  **Managed Bots**

  *New Methods:*

  - Added [`aiogram.methods.get_managed_bot_access_settings.GetManagedBotAccessSettings`](api/methods/get_managed_bot_access_settings.html#aiogram.methods.get_managed_bot_access_settings.GetManagedBotAccessSettings "aiogram.methods.get_managed_bot_access_settings.GetManagedBotAccessSettings") method - retrieves the access settings of a managed bot
  - Added [`aiogram.methods.set_managed_bot_access_settings.SetManagedBotAccessSettings`](api/methods/set_managed_bot_access_settings.html#aiogram.methods.set_managed_bot_access_settings.SetManagedBotAccessSettings "aiogram.methods.set_managed_bot_access_settings.SetManagedBotAccessSettings") method - updates the access settings of a managed bot
  - Added [`aiogram.methods.get_user_personal_chat_messages.GetUserPersonalChatMessages`](api/methods/get_user_personal_chat_messages.html#aiogram.methods.get_user_personal_chat_messages.GetUserPersonalChatMessages "aiogram.methods.get_user_personal_chat_messages.GetUserPersonalChatMessages") method - retrieves messages from a user’s personal chat

  *New Types:*

  - Added [`aiogram.types.bot_access_settings.BotAccessSettings`](api/types/bot_access_settings.html#aiogram.types.bot_access_settings.BotAccessSettings "aiogram.types.bot_access_settings.BotAccessSettings") type - defines the access configuration for a bot

  [#1806](https://github.com/aiogram/aiogram/issues/1806)

## 3.27.0 (2026-04-04)

### Features

- Added __eq__ and __hash__ methods to the Default class.
  [#1707](https://github.com/aiogram/aiogram/issues/1707)

### Bugfixes

- `CommandStart(deep_link=False)` now correctly rejects messages that contain deep-link arguments. Previously `deep_link=False` (the default) did not distinguish between `/start` and `/start <payload>`. The default is changed to `None` (accept both) to preserve backward compatibility.
  [#1713](https://github.com/aiogram/aiogram/issues/1713)
- Fixed `HtmlDecoration.custom_emoji()` to use the correct `emoji-id` attribute name instead of `emoji_id` in the `<tg-emoji>` tag, matching the Telegram Bot API specification.
  [#1782](https://github.com/aiogram/aiogram/issues/1782)
- Remove redundant list() around sorted() and fix router type name in validation error message
  [#1788](https://github.com/aiogram/aiogram/issues/1788)

### Misc

- Updated to [Bot API 9.6](https://core.telegram.org/bots/api-changelog#april-3-2026)

  **Managed Bots**

  *New Methods:*

  - Added [`aiogram.methods.get_managed_bot_token.GetManagedBotToken`](api/methods/get_managed_bot_token.html#aiogram.methods.get_managed_bot_token.GetManagedBotToken "aiogram.methods.get_managed_bot_token.GetManagedBotToken") method - retrieves the token of a managed bot
  - Added [`aiogram.methods.replace_managed_bot_token.ReplaceManagedBotToken`](api/methods/replace_managed_bot_token.html#aiogram.methods.replace_managed_bot_token.ReplaceManagedBotToken "aiogram.methods.replace_managed_bot_token.ReplaceManagedBotToken") method - generates a new token for a managed bot, invalidating the previous one
  - Added [`aiogram.methods.save_prepared_keyboard_button.SavePreparedKeyboardButton`](api/methods/save_prepared_keyboard_button.html#aiogram.methods.save_prepared_keyboard_button.SavePreparedKeyboardButton "aiogram.methods.save_prepared_keyboard_button.SavePreparedKeyboardButton") method - saves a keyboard button to be used in Mini Apps via `requestChat`

  *New Types:*

  - Added [`aiogram.types.keyboard_button_request_managed_bot.KeyboardButtonRequestManagedBot`](api/types/keyboard_button_request_managed_bot.html#aiogram.types.keyboard_button_request_managed_bot.KeyboardButtonRequestManagedBot "aiogram.types.keyboard_button_request_managed_bot.KeyboardButtonRequestManagedBot") type - defines criteria for selecting a managed bot via a keyboard button
  - Added [`aiogram.types.managed_bot_created.ManagedBotCreated`](api/types/managed_bot_created.html#aiogram.types.managed_bot_created.ManagedBotCreated "aiogram.types.managed_bot_created.ManagedBotCreated") type - describes a service message about a managed bot being created
  - Added [`aiogram.types.managed_bot_updated.ManagedBotUpdated`](api/types/managed_bot_updated.html#aiogram.types.managed_bot_updated.ManagedBotUpdated "aiogram.types.managed_bot_updated.ManagedBotUpdated") type - describes updates to a managed bot
  - Added [`aiogram.types.prepared_keyboard_button.PreparedKeyboardButton`](api/types/prepared_keyboard_button.html#aiogram.types.prepared_keyboard_button.PreparedKeyboardButton "aiogram.types.prepared_keyboard_button.PreparedKeyboardButton") type - represents a prepared keyboard button for use in Mini Apps

  *New Fields:*

  - Added `can_manage_bots` field to [`aiogram.types.user.User`](api/types/user.html#aiogram.types.user.User "aiogram.types.user.User") - indicates whether the bot can manage other bots
  - Added `request_managed_bot` field to [`aiogram.types.keyboard_button.KeyboardButton`](api/types/keyboard_button.html#aiogram.types.keyboard_button.KeyboardButton "aiogram.types.keyboard_button.KeyboardButton") - requests the user to select a managed bot
  - Added `managed_bot_created` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - service message about a managed bot being created (type: [`aiogram.types.managed_bot_created.ManagedBotCreated`](api/types/managed_bot_created.html#aiogram.types.managed_bot_created.ManagedBotCreated "aiogram.types.managed_bot_created.ManagedBotCreated"))
  - Added `managed_bot` field to [`aiogram.types.update.Update`](api/types/update.html#aiogram.types.update.Update "aiogram.types.update.Update") - contains updates received by a managed bot

  **Polls**

  *New Types:*

  - Added [`aiogram.types.poll_option_added.PollOptionAdded`](api/types/poll_option_added.html#aiogram.types.poll_option_added.PollOptionAdded "aiogram.types.poll_option_added.PollOptionAdded") type - describes a service message about a new option added to a poll
  - Added [`aiogram.types.poll_option_deleted.PollOptionDeleted`](api/types/poll_option_deleted.html#aiogram.types.poll_option_deleted.PollOptionDeleted "aiogram.types.poll_option_deleted.PollOptionDeleted") type - describes a service message about a poll option being deleted

  *New Fields:*

  - Replaced `correct_option_id` with `correct_option_ids` in [`aiogram.types.poll.Poll`](api/types/poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") - supports multiple correct answers for quiz polls
  - Added `allows_revoting` field to [`aiogram.types.poll.Poll`](api/types/poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") - indicates whether users are allowed to change their vote
  - Added `description` and `description_entities` fields to [`aiogram.types.poll.Poll`](api/types/poll.html#aiogram.types.poll.Poll "aiogram.types.poll.Poll") - optional poll description with formatting entities
  - Added `persistent_id` field to [`aiogram.types.poll_option.PollOption`](api/types/poll_option.html#aiogram.types.poll_option.PollOption "aiogram.types.poll_option.PollOption") - stable identifier for a poll option
  - Added `added_by_user` and `added_by_chat` fields to [`aiogram.types.poll_option.PollOption`](api/types/poll_option.html#aiogram.types.poll_option.PollOption "aiogram.types.poll_option.PollOption") - identifies who added the option
  - Added `addition_date` field to [`aiogram.types.poll_option.PollOption`](api/types/poll_option.html#aiogram.types.poll_option.PollOption "aiogram.types.poll_option.PollOption") - date when the option was added
  - Added `option_persistent_ids` field to [`aiogram.types.poll_answer.PollAnswer`](api/types/poll_answer.html#aiogram.types.poll_answer.PollAnswer "aiogram.types.poll_answer.PollAnswer") - persistent IDs of the chosen options
  - Added `poll_option_id` field to [`aiogram.types.reply_parameters.ReplyParameters`](api/types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters") - allows replying to a specific poll option
  - Added `reply_to_poll_option_id` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - the persistent ID of the poll option the message replies to

  *New Parameters for* [`aiogram.methods.send_poll.SendPoll`](api/methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll"):

  - Replaced `correct_option_id` with `correct_option_ids` - supports multiple correct answers for quiz polls
  - Added `allows_revoting` - allows users to change their vote after submission
  - Added `shuffle_options` - randomizes the order of poll options for each user
  - Added `allow_adding_options` - allows users to add their own poll options
  - Added `hide_results_until_closes` - hides vote results until the poll is closed
  - Added `description`, `description_parse_mode`, `description_entities` - optional poll description with parse mode and formatting

  [#1792](https://github.com/aiogram/aiogram/issues/1792)

## 3.26.0 (2026-03-03)

### Bugfixes

- Fixed scene transitions to preserve middleware-injected data when moving between scenes via `SceneWizard.goto`.
  [#1687](https://github.com/aiogram/aiogram/issues/1687)
- Added `icon_custom_emoji_id` and `style` parameters to `InlineKeyboardBuilder.button` and `ReplyKeyboardBuilder.button` signatures.
  [#1768](https://github.com/aiogram/aiogram/issues/1768)
- Fixed Pydantic protected namespace warning for model_custom_emoji_id by adding protected_namespaces=() to model_config.
  [#1772](https://github.com/aiogram/aiogram/issues/1772)

### Misc

- Documented webhook security constraints for proxy deployments, including trust requirements for `X-Forwarded-For` and recommended defense-in-depth checks.
  [#47](https://github.com/aiogram/aiogram/issues/47)
- Updated to [Bot API 9.5](https://core.telegram.org/bots/api-changelog#march-1-2026)

  **New Methods:**

  - Added [`aiogram.methods.send_message_draft.SendMessageDraft`](api/methods/send_message_draft.html#aiogram.methods.send_message_draft.SendMessageDraft "aiogram.methods.send_message_draft.SendMessageDraft") method - allowed for all bots to stream partial messages while they are being generated
  - Added [`aiogram.methods.set_chat_member_tag.SetChatMemberTag`](api/methods/set_chat_member_tag.html#aiogram.methods.set_chat_member_tag.SetChatMemberTag "aiogram.methods.set_chat_member_tag.SetChatMemberTag") method - allows bots to set a custom tag for a chat member; available via [`aiogram.types.chat.Chat.set_member_tag()`](api/types/chat.html#aiogram.types.chat.Chat.set_member_tag "aiogram.types.chat.Chat.set_member_tag") shortcut

  **New Fields:**

  - Added `date_time` type to [`aiogram.types.message_entity.MessageEntity`](api/types/message_entity.html#aiogram.types.message_entity.MessageEntity "aiogram.types.message_entity.MessageEntity") with `unix_time` and `date_time_format` fields - allows bots to display a formatted date and time to the user
  - Added `tag` field to [`aiogram.types.chat_member_member.ChatMemberMember`](api/types/chat_member_member.html#aiogram.types.chat_member_member.ChatMemberMember "aiogram.types.chat_member_member.ChatMemberMember") and [`aiogram.types.chat_member_restricted.ChatMemberRestricted`](api/types/chat_member_restricted.html#aiogram.types.chat_member_restricted.ChatMemberRestricted "aiogram.types.chat_member_restricted.ChatMemberRestricted") - the custom tag set for the chat member
  - Added `can_edit_tag` field to [`aiogram.types.chat_member_restricted.ChatMemberRestricted`](api/types/chat_member_restricted.html#aiogram.types.chat_member_restricted.ChatMemberRestricted "aiogram.types.chat_member_restricted.ChatMemberRestricted") and [`aiogram.types.chat_permissions.ChatPermissions`](api/types/chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions") - indicates whether the user is allowed to edit their own tag
  - Added `can_manage_tags` field to [`aiogram.types.chat_member_administrator.ChatMemberAdministrator`](api/types/chat_member_administrator.html#aiogram.types.chat_member_administrator.ChatMemberAdministrator "aiogram.types.chat_member_administrator.ChatMemberAdministrator") and [`aiogram.types.chat_administrator_rights.ChatAdministratorRights`](api/types/chat_administrator_rights.html#aiogram.types.chat_administrator_rights.ChatAdministratorRights "aiogram.types.chat_administrator_rights.ChatAdministratorRights") - indicates whether the administrator can manage tags of other chat members
  - Added `can_manage_tags` parameter to [`aiogram.methods.promote_chat_member.PromoteChatMember`](api/methods/promote_chat_member.html#aiogram.methods.promote_chat_member.PromoteChatMember "aiogram.methods.promote_chat_member.PromoteChatMember") method
  - Added `sender_tag` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") - the tag of the message sender in the chat

  [#1780](https://github.com/aiogram/aiogram/issues/1780)

## 3.25.0 (2026-02-10)

### Features

- Add full_name property to Contact and corresponding tests
  [#1758](https://github.com/aiogram/aiogram/issues/1758)
- Updated to [Bot API 9.4 (February 9, 2026)](https://core.telegram.org/bots/api-changelog#february-9-2026)

  **New Features:**

  - Bots with Premium subscriptions can now use custom emoji directly in messages to private, group, and supergroup chats
  - Bots can create topics in private chats via the [`aiogram.methods.create_forum_topic.CreateForumTopic`](api/methods/create_forum_topic.html#aiogram.methods.create_forum_topic.CreateForumTopic "aiogram.methods.create_forum_topic.CreateForumTopic") method
  - Bots can prevent users from creating/deleting topics in private chats through BotFather settings

  **New Fields:**

  - Added `allows_users_to_create_topics` field to [`aiogram.types.user.User`](api/types/user.html#aiogram.types.user.User "aiogram.types.user.User") class - indicates whether the user allows others to create topics in chats with them
  - Added `icon_custom_emoji_id` field to [`aiogram.types.keyboard_button.KeyboardButton`](api/types/keyboard_button.html#aiogram.types.keyboard_button.KeyboardButton "aiogram.types.keyboard_button.KeyboardButton") and [`aiogram.types.inline_keyboard_button.InlineKeyboardButton`](api/types/inline_keyboard_button.html#aiogram.types.inline_keyboard_button.InlineKeyboardButton "aiogram.types.inline_keyboard_button.InlineKeyboardButton") classes - allows displaying custom emoji icons on buttons
  - Added `style` field to [`aiogram.types.keyboard_button.KeyboardButton`](api/types/keyboard_button.html#aiogram.types.keyboard_button.KeyboardButton "aiogram.types.keyboard_button.KeyboardButton") and [`aiogram.types.inline_keyboard_button.InlineKeyboardButton`](api/types/inline_keyboard_button.html#aiogram.types.inline_keyboard_button.InlineKeyboardButton "aiogram.types.inline_keyboard_button.InlineKeyboardButton") classes - changes button color/style
  - Added `chat_owner_left` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") class - service message indicating chat owner has left (type: [`aiogram.types.chat_owner_left.ChatOwnerLeft`](api/types/chat_owner_left.html#aiogram.types.chat_owner_left.ChatOwnerLeft "aiogram.types.chat_owner_left.ChatOwnerLeft"))
  - Added `chat_owner_changed` field to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") class - service message indicating chat ownership has transferred (type: [`aiogram.types.chat_owner_changed.ChatOwnerChanged`](api/types/chat_owner_changed.html#aiogram.types.chat_owner_changed.ChatOwnerChanged "aiogram.types.chat_owner_changed.ChatOwnerChanged"))
  - Added `qualities` field to [`aiogram.types.video.Video`](api/types/video.html#aiogram.types.video.Video "aiogram.types.video.Video") class - list of available video quality options (type: `list[`[`aiogram.types.video_quality.VideoQuality`](api/types/video_quality.html#aiogram.types.video_quality.VideoQuality "aiogram.types.video_quality.VideoQuality")`]`)
  - Added `first_profile_audio` field to [`aiogram.types.chat_full_info.ChatFullInfo`](api/types/chat_full_info.html#aiogram.types.chat_full_info.ChatFullInfo "aiogram.types.chat_full_info.ChatFullInfo") class - user’s first profile audio
  - Added `rarity` field to [`aiogram.types.unique_gift_model.UniqueGiftModel`](api/types/unique_gift_model.html#aiogram.types.unique_gift_model.UniqueGiftModel "aiogram.types.unique_gift_model.UniqueGiftModel") class
  - Added `is_burned` field to [`aiogram.types.unique_gift.UniqueGift`](api/types/unique_gift.html#aiogram.types.unique_gift.UniqueGift "aiogram.types.unique_gift.UniqueGift") class

  **New Methods:**

  - Added [`aiogram.methods.set_my_profile_photo.SetMyProfilePhoto`](api/methods/set_my_profile_photo.html#aiogram.methods.set_my_profile_photo.SetMyProfilePhoto "aiogram.methods.set_my_profile_photo.SetMyProfilePhoto") method - allows bots to set their profile photo
  - Added [`aiogram.methods.remove_my_profile_photo.RemoveMyProfilePhoto`](api/methods/remove_my_profile_photo.html#aiogram.methods.remove_my_profile_photo.RemoveMyProfilePhoto "aiogram.methods.remove_my_profile_photo.RemoveMyProfilePhoto") method - allows bots to remove their profile photo
  - Added [`aiogram.methods.get_user_profile_audios.GetUserProfileAudios`](api/methods/get_user_profile_audios.html#aiogram.methods.get_user_profile_audios.GetUserProfileAudios "aiogram.methods.get_user_profile_audios.GetUserProfileAudios") method - retrieves a user’s profile audio list
  - Added [`aiogram.types.user.User.get_profile_audios()`](api/types/user.html#aiogram.types.user.User.get_profile_audios "aiogram.types.user.User.get_profile_audios") shortcut - creates a prefilled [`aiogram.methods.get_user_profile_audios.GetUserProfileAudios`](api/methods/get_user_profile_audios.html#aiogram.methods.get_user_profile_audios.GetUserProfileAudios "aiogram.methods.get_user_profile_audios.GetUserProfileAudios") request with `user_id`

  **New Types:**

  - Added [`aiogram.types.chat_owner_left.ChatOwnerLeft`](api/types/chat_owner_left.html#aiogram.types.chat_owner_left.ChatOwnerLeft "aiogram.types.chat_owner_left.ChatOwnerLeft") type - describes a service message about the chat owner leaving the chat
  - Added [`aiogram.types.chat_owner_changed.ChatOwnerChanged`](api/types/chat_owner_changed.html#aiogram.types.chat_owner_changed.ChatOwnerChanged "aiogram.types.chat_owner_changed.ChatOwnerChanged") type - describes a service message about an ownership change in the chat
  - Added [`aiogram.types.video_quality.VideoQuality`](api/types/video_quality.html#aiogram.types.video_quality.VideoQuality "aiogram.types.video_quality.VideoQuality") type - describes available video quality options
  - Added [`aiogram.types.user_profile_audios.UserProfileAudios`](api/types/user_profile_audios.html#aiogram.types.user_profile_audios.UserProfileAudios "aiogram.types.user_profile_audios.UserProfileAudios") type - represents the collection of audios displayed on a user’s profile

  [#1761](https://github.com/aiogram/aiogram/issues/1761)

### Bugfixes

- Fixed scene handling for `channel_post` and `edited_channel_post` when Scenes are registered but FSM state is unavailable, and added channel-scoped FSM context support for `CHAT`/`CHAT_TOPIC` strategies.
  [#1743](https://github.com/aiogram/aiogram/issues/1743)

### Misc

- Migrated from Black and isort to Ruff for code formatting and linting, a modern, blazingly fast formatter and linter written in Rust.

  Enabled additional ruff rule sets.

  **For end users:**

  No changes required. This is purely a development tooling change that doesn’t affect the library API or behavior.

  **For contributors:**

  - Use `make reformat` or `uv run ruff format` to format code (replaces `black` and `isort`)
  - Use `make lint` to check code quality (now includes formatting, linting, and type checking)
  - Pre-commit hooks automatically updated to use `ruff` and `ruff-format`
  - CI/CD pipelines updated to use ruff in GitHub Actions workflows

  **Benefits:**

  - 10-100x faster formatting and linting compared to Black + isort + flake8
  - Single tool for formatting, import sorting, and linting
  - More comprehensive code quality checks out of the box
  - Auto-fixes for many common issues (33 issues auto-fixed during migration)
  - Better integration with modern Python development workflows

  This change improves the developer experience and code quality while maintaining the same code style standards.
  [#1750](https://github.com/aiogram/aiogram/issues/1750)

## 3.24.0 (2026-01-02)

### Features

- Added full support for Telegram Bot API 9.3

  **Topics in Private Chats**

  Bot API 9.3 introduces forum topics functionality for private chats:

  - Added new `sendMessageDraft` method for streaming partial messages while being generated (requires forum topic mode enabled)
  - Added `has_topics_enabled` field to the `User` class to determine if forum topic mode is enabled in private chats
  - Added `message_thread_id` and `is_topic_message` fields to the `Message` class for private chat topic support
  - Added `message_thread_id` parameter support to messaging methods: `sendMessage`, `sendPhoto`, `sendVideo`, `sendAnimation`, `sendAudio`, `sendDocument`, `sendPaidMedia`, `sendSticker`, `sendVideoNote`, `sendVoice`, `sendLocation`, `sendVenue`, `sendContact`, `sendPoll`, `sendDice`, `sendInvoice`, `sendGame`, `sendMediaGroup`, `copyMessage`, `copyMessages`, `forwardMessage`, `forwardMessages`
  - Updated `sendChatAction` to support `message_thread_id` parameter in private chats
  - Updated `editForumTopic`, `deleteForumTopic`, `unpinAllForumTopicMessages` methods to manage private chat topics
  - Added `is_name_implicit` field to `ForumTopic` class

  **Gifts System Enhancements**

  Enhanced gifts functionality with new methods and extended capabilities:

  - Added `getUserGifts` method to retrieve gifts owned and hosted by a user
  - Added `getChatGifts` method to retrieve gifts owned by a chat
  - Updated `UniqueGiftInfo` class: replaced `last_resale_star_count` with `last_resale_currency` and `last_resale_amount` fields, added “gifted_upgrade” and “offer” as origin values
  - Updated `getBusinessAccountGifts` method: replaced `exclude_limited` parameter with `exclude_limited_upgradable` and `exclude_limited_non_upgradable`, added `exclude_from_blockchain` parameter
  - Added new fields to `Gift` class: `personal_total_count`, `personal_remaining_count`, `is_premium`, `has_colors`, `unique_gift_variant_count`, `gift_background`
  - Added new fields to `UniqueGift` class: `gift_id`, `is_from_blockchain`, `is_premium`, `colors`
  - Added new fields to gift info classes: `is_upgrade_separate`, `unique_gift_number`
  - Added `gift_upgrade_sent` field to the `Message` class
  - Added `gifts_from_channels` field to the `AcceptedGiftTypes` class
  - Added new `UniqueGiftColors` class for color schemes in user names and link previews
  - Added new `GiftBackground` class for gift background styling

  **Business Accounts & Stories**

  - Added `repostStory` method to enable reposting stories across managed business accounts

  **Miscellaneous Updates**

  - Bots can now disable main usernames and set `can_restrict_members` rights in channels
  - Maximum paid media price increased to 25000 Telegram Stars
  - Added new `UserRating` class
  - Added `rating`, `paid_message_star_count`, `unique_gift_colors` fields to the `ChatFullInfo` class
  - Added support for `message_effect_id` parameter in forward/copy operations
  - Added `completed_by_chat` field to the `ChecklistTask` class

  [#1747](https://github.com/aiogram/aiogram/issues/1747)

### Bugfixes

- Fixed I18n initialization with relative path
  [#1740](https://github.com/aiogram/aiogram/issues/1740)
- Fixed dependency injection for arguments that have “ForwardRef” annotations in Py3.14+
  since inspect.getfullargspec(callback) can’t process callback if it’s arguments have “ForwardRef” annotations
  [#1741](https://github.com/aiogram/aiogram/issues/1741)

### Misc

- Migrated from `hatch` to `uv` for dependency management and development workflows.

  This change improves developer experience with significantly faster dependency resolution (10-100x faster than pip), automatic virtual environment management, and reproducible builds through lockfile support.

  **What changed for contributors:**

  - Install dependencies with `uv sync --all-extras --group dev --group test` instead of `pip install -e .[dev,test,docs]`
  - Run commands with `uv run` prefix (e.g., `uv run pytest`, `uv run black`)
  - All Makefile commands now use `uv` internally (`make install`, `make test`, `make lint`, etc.)
  - Version bumping now uses a custom `scripts/bump_version.py` script instead of `hatch version`

  **What stayed the same:**

  - Build backend remains `hatchling` (no changes to package building)
  - Dynamic version reading from `aiogram/__meta__.py` still works
  - All GitHub Actions CI/CD workflows updated to use `uv`
  - ReadTheDocs builds continue to work without changes
  - Development dependencies (`dev`, `test`) moved to `[dependency-groups]` section
  - Documentation dependencies (`docs`) remain in `[project.optional-dependencies]` for compatibility

  Contributors can use either the traditional `pip`/`venv` workflow or the new `uv` workflow - both are documented in the contributing guide.
  [#1748](https://github.com/aiogram/aiogram/issues/1748)
- Updated type hints in the codebase to Python 3.10+ style unions and optionals.
  [#1749](https://github.com/aiogram/aiogram/issues/1749)

## 3.23.0 (2025-12-07)

### Features

- This PR updates the codebase to support Python 3.14.

  - Updated project dep aiohttp
  - Updated development deps
  - Fixed tests to support Py3.14
  - Refactored uvloop using due to deprecation of asyncio.set_event_loop_police

  [#1730](https://github.com/aiogram/aiogram/issues/1730)

### Deprecations and Removals

- This PR updates the codebase following the end of life for Python 3.9.

  Reference: <https://devguide.python.org/versions/>

  - Updated type annotations to Python 3.10+ style, replacing deprecated `List`, `Set`, etc., with built-in `list`, `set`, and related types.
  - Refactored code by simplifying nested `if` expressions.
  - Updated several dependencies, including security-related upgrades.

  [#1726](https://github.com/aiogram/aiogram/issues/1726)

### Misc

- Updated pydantic to 2.12, which supports Python 3.14
  [#1729](https://github.com/aiogram/aiogram/issues/1729)
- Temporary silents warn when uvloop uses deprecated asyncio.iscoroutinefunction function in py3.14+ in tests
  [#1739](https://github.com/aiogram/aiogram/issues/1739)

## 3.22.0 (2025-08-17)

### Features

- Support validating init data using only bot id.
  [#1715](https://github.com/aiogram/aiogram/issues/1715)
- Added full support for the [Bot API 9.2](https://core.telegram.org/bots/api-changelog#august-15-2025):

  **Direct Messages in Channels**

  - Added the field `is_direct_messages` to the classes [`aiogram.types.chat.Chat`](api/types/chat.html#aiogram.types.chat.Chat "aiogram.types.chat.Chat") and [`aiogram.types.chat_full_info.ChatFullInfo`](api/types/chat_full_info.html#aiogram.types.chat_full_info.ChatFullInfo "aiogram.types.chat_full_info.ChatFullInfo"), indicating whether the chat is a direct messages chat.
  - Added the field `parent_chat` to the class [`aiogram.types.chat_full_info.ChatFullInfo`](api/types/chat_full_info.html#aiogram.types.chat_full_info.ChatFullInfo "aiogram.types.chat_full_info.ChatFullInfo"), describing the parent channel for direct messages chats.
  - Added the class [`aiogram.types.direct_messages_topic.DirectMessagesTopic`](api/types/direct_messages_topic.html#aiogram.types.direct_messages_topic.DirectMessagesTopic "aiogram.types.direct_messages_topic.DirectMessagesTopic") representing a direct messages topic.
  - Added the field `direct_messages_topic` to the class [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message"), describing the direct messages topic associated with a message.
  - Added the parameter `direct_messages_topic_id` to multiple sending methods for directing messages to specific direct message topics.

  **Suggested Posts**

  - Added the class [`aiogram.types.suggested_post_parameters.SuggestedPostParameters`](api/types/suggested_post_parameters.html#aiogram.types.suggested_post_parameters.SuggestedPostParameters "aiogram.types.suggested_post_parameters.SuggestedPostParameters") representing parameters for suggested posts.
  - Added the parameter `suggested_post_parameters` to various sending methods, allowing bots to create suggested posts for channel approval.
  - Added the method [`aiogram.methods.approve_suggested_post.ApproveSuggestedPost`](api/methods/approve_suggested_post.html#aiogram.methods.approve_suggested_post.ApproveSuggestedPost "aiogram.methods.approve_suggested_post.ApproveSuggestedPost"), allowing bots to approve suggested posts in direct messages chats.
  - Added the method [`aiogram.methods.decline_suggested_post.DeclineSuggestedPost`](api/methods/decline_suggested_post.html#aiogram.methods.decline_suggested_post.DeclineSuggestedPost "aiogram.methods.decline_suggested_post.DeclineSuggestedPost"), allowing bots to decline suggested posts in direct messages chats.
  - Added the field `can_manage_direct_messages` to administrator-related classes [`aiogram.types.chat_administrator_rights.ChatAdministratorRights`](api/types/chat_administrator_rights.html#aiogram.types.chat_administrator_rights.ChatAdministratorRights "aiogram.types.chat_administrator_rights.ChatAdministratorRights") and [`aiogram.types.chat_member_administrator.ChatMemberAdministrator`](api/types/chat_member_administrator.html#aiogram.types.chat_member_administrator.ChatMemberAdministrator "aiogram.types.chat_member_administrator.ChatMemberAdministrator").
  - Added the class [`aiogram.types.suggested_post_info.SuggestedPostInfo`](api/types/suggested_post_info.html#aiogram.types.suggested_post_info.SuggestedPostInfo "aiogram.types.suggested_post_info.SuggestedPostInfo") representing information about a suggested post.
  - Added the class [`aiogram.types.suggested_post_price.SuggestedPostPrice`](api/types/suggested_post_price.html#aiogram.types.suggested_post_price.SuggestedPostPrice "aiogram.types.suggested_post_price.SuggestedPostPrice") representing the price for a suggested post.
  - Added service message classes for suggested post events:

    - [`aiogram.types.suggested_post_approved.SuggestedPostApproved`](api/types/suggested_post_approved.html#aiogram.types.suggested_post_approved.SuggestedPostApproved "aiogram.types.suggested_post_approved.SuggestedPostApproved") and the field `suggested_post_approved` to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message")
    - [`aiogram.types.suggested_post_approval_failed.SuggestedPostApprovalFailed`](api/types/suggested_post_approval_failed.html#aiogram.types.suggested_post_approval_failed.SuggestedPostApprovalFailed "aiogram.types.suggested_post_approval_failed.SuggestedPostApprovalFailed") and the field `suggested_post_approval_failed` to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message")
    - [`aiogram.types.suggested_post_declined.SuggestedPostDeclined`](api/types/suggested_post_declined.html#aiogram.types.suggested_post_declined.SuggestedPostDeclined "aiogram.types.suggested_post_declined.SuggestedPostDeclined") and the field `suggested_post_declined` to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message")
    - [`aiogram.types.suggested_post_paid.SuggestedPostPaid`](api/types/suggested_post_paid.html#aiogram.types.suggested_post_paid.SuggestedPostPaid "aiogram.types.suggested_post_paid.SuggestedPostPaid") and the field `suggested_post_paid` to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message")
    - [`aiogram.types.suggested_post_refunded.SuggestedPostRefunded`](api/types/suggested_post_refunded.html#aiogram.types.suggested_post_refunded.SuggestedPostRefunded "aiogram.types.suggested_post_refunded.SuggestedPostRefunded") and the field `suggested_post_refunded` to [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message")

  **Enhanced Checklists**

  - Added the field `checklist_task_id` to the class [`aiogram.types.reply_parameters.ReplyParameters`](api/types/reply_parameters.html#aiogram.types.reply_parameters.ReplyParameters "aiogram.types.reply_parameters.ReplyParameters"), allowing replies to specific checklist tasks.
  - Added the field `reply_to_checklist_task_id` to the class [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message"), indicating which checklist task a message is replying to.

  **Gifts Improvements**

  - Added the field `publisher_chat` to the classes [`aiogram.types.gift.Gift`](api/types/gift.html#aiogram.types.gift.Gift "aiogram.types.gift.Gift") and [`aiogram.types.unique_gift.UniqueGift`](api/types/unique_gift.html#aiogram.types.unique_gift.UniqueGift "aiogram.types.unique_gift.UniqueGift"), describing the chat that published the gift.

  **Additional Features**

  - Added the field `is_paid_post` to the class [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message"), indicating whether a message is a paid post.

  [#1720](https://github.com/aiogram/aiogram/issues/1720)

### Bugfixes

- Use hmac.compare_digest for validating WebApp data to prevent timing attacks.
  [#1709](https://github.com/aiogram/aiogram/issues/1709)

### Misc

- Migrated MongoStorage from relying on deprecated motor package to using new async PyMongo. To use mongo storage with new async PyMongo, you need to install the PyMongo package instead of motor and just substitute deprecated MongoStorage with PyMongoStorage class, no other action needed.
  [#1705](https://github.com/aiogram/aiogram/issues/1705)

## 3.21.0 (2025-07-05)

### Features

- Refactor methods input types to calm down MyPy. #1682

  Dict[str, Any] is replaced with Mapping[str, Any] in the following methods:

  - FSMContext.set_data
  - FSMContext.update_data
  - BaseStorage.set_data
  - BaseStorage.update_data
  - BaseStorage’s child methods
  - SceneWizard.set_data
  - SceneWizard.update_data

  [#1683](https://github.com/aiogram/aiogram/issues/1683)
- Add support for State type in scenes methods like goto, enter, get
  [#1685](https://github.com/aiogram/aiogram/issues/1685)
- Added full support for the [Bot API 9.1](https://core.telegram.org/bots/api-changelog#july-3-2025):

  **Checklists**

  - Added the class [`aiogram.types.checklist_task.ChecklistTask`](api/types/checklist_task.html#aiogram.types.checklist_task.ChecklistTask "aiogram.types.checklist_task.ChecklistTask") representing a task in a checklist.
  - Added the class [`aiogram.types.checklist.Checklist`](api/types/checklist.html#aiogram.types.checklist.Checklist "aiogram.types.checklist.Checklist") representing a checklist.
  - Added the class [`aiogram.types.input_checklist_task.InputChecklistTask`](api/types/input_checklist_task.html#aiogram.types.input_checklist_task.InputChecklistTask "aiogram.types.input_checklist_task.InputChecklistTask") representing a task to add to a checklist.
  - Added the class [`aiogram.types.input_checklist.InputChecklist`](api/types/input_checklist.html#aiogram.types.input_checklist.InputChecklist "aiogram.types.input_checklist.InputChecklist") representing a checklist to create.
  - Added the field `checklist` to the classes [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") and [`aiogram.types.external_reply_info.ExternalReplyInfo`](api/types/external_reply_info.html#aiogram.types.external_reply_info.ExternalReplyInfo "aiogram.types.external_reply_info.ExternalReplyInfo"), describing a checklist in a message.
  - Added the class [`aiogram.types.checklist_tasks_done.ChecklistTasksDone`](api/types/checklist_tasks_done.html#aiogram.types.checklist_tasks_done.ChecklistTasksDone "aiogram.types.checklist_tasks_done.ChecklistTasksDone") and the field `checklist_tasks_done` to the class [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message"), describing a service message about status changes for tasks in a checklist (i.e., marked as done/not done).
  - Added the class [`aiogram.types.checklist_tasks_added.ChecklistTasksAdded`](api/types/checklist_tasks_added.html#aiogram.types.checklist_tasks_added.ChecklistTasksAdded "aiogram.types.checklist_tasks_added.ChecklistTasksAdded") and the field `checklist_tasks_added` to the class [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message"), describing a service message about the addition of new tasks to a checklist.
  - Added the method [`aiogram.methods.send_checklist.SendChecklist`](api/methods/send_checklist.html#aiogram.methods.send_checklist.SendChecklist "aiogram.methods.send_checklist.SendChecklist"), allowing bots to send a checklist on behalf of a business account.
  - Added the method [`aiogram.methods.edit_message_checklist.EditMessageChecklist`](api/methods/edit_message_checklist.html#aiogram.methods.edit_message_checklist.EditMessageChecklist "aiogram.methods.edit_message_checklist.EditMessageChecklist"), allowing bots to edit a checklist on behalf of a business account.

  **Gifts**

  - Added the field `next_transfer_date` to the classes [`aiogram.types.owned_gift_unique.OwnedGiftUnique`](api/types/owned_gift_unique.html#aiogram.types.owned_gift_unique.OwnedGiftUnique "aiogram.types.owned_gift_unique.OwnedGiftUnique") and [`aiogram.types.unique_gift_info.UniqueGiftInfo`](api/types/unique_gift_info.html#aiogram.types.unique_gift_info.UniqueGiftInfo "aiogram.types.unique_gift_info.UniqueGiftInfo").
  - Added the field `last_resale_star_count` to the class [`aiogram.types.unique_gift_info.UniqueGiftInfo`](api/types/unique_gift_info.html#aiogram.types.unique_gift_info.UniqueGiftInfo "aiogram.types.unique_gift_info.UniqueGiftInfo").
  - Added “resale” as the possible value of the field `origin` in the class [`aiogram.types.unique_gift_info.UniqueGiftInfo`](api/types/unique_gift_info.html#aiogram.types.unique_gift_info.UniqueGiftInfo "aiogram.types.unique_gift_info.UniqueGiftInfo").

  **General**

  - Increased the maximum number of options in a poll to 12.
  - Added the method [`aiogram.methods.get_my_star_balance.GetMyStarBalance`](api/methods/get_my_star_balance.html#aiogram.methods.get_my_star_balance.GetMyStarBalance "aiogram.methods.get_my_star_balance.GetMyStarBalance"), allowing bots to get their current balance of Telegram Stars.
  - Added the class [`aiogram.types.direct_message_price_changed.DirectMessagePriceChanged`](api/types/direct_message_price_changed.html#aiogram.types.direct_message_price_changed.DirectMessagePriceChanged "aiogram.types.direct_message_price_changed.DirectMessagePriceChanged") and the field `direct_message_price_changed` to the class [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message"), describing a service message about a price change for direct messages sent to the channel chat.

  [#1704](https://github.com/aiogram/aiogram/issues/1704)

### Bugfixes

- Fixed an issue where the scene entry handler (`enter`) was not receiving data
  passed to the context by middleware, which could result in a `TypeError`.

  Also updated the documentation to clarify how to enter the scene.
  [#1672](https://github.com/aiogram/aiogram/issues/1672)
- Correctly pass error message in TelegramMigrateToChat.
  [#1694](https://github.com/aiogram/aiogram/issues/1694)

### Improved Documentation

- Added documentation for changing state of another user in FSM
  [#1633](https://github.com/aiogram/aiogram/issues/1633)

### Misc

- Fixed MyPy [return-value] error in InlineKeyboardBuilder().as_markup().
  as_markup method now overloads parent class method and uses super(), to call parent’s
  as_markup method.
  Also added correct type hint to as_markup’s return in InlineKeyboardBuilder and
  ReplyKeyboardBuilder classes.
  [#1677](https://github.com/aiogram/aiogram/issues/1677)
- Changed Babel’s pinned version from minor to major.
  [#1681](https://github.com/aiogram/aiogram/issues/1681)
- Increased max `aiohttp` version support from “<3.12” to “<3.13”
  [#1700](https://github.com/aiogram/aiogram/issues/1700)

## 3.20.0 (2025-04-14)

### Features

- Add different shortcut methods for `aiogram.utils.formatting.Text.as_kwargs()`
  [#1657](https://github.com/aiogram/aiogram/issues/1657)
- Added full support for the [Bot API 9.0](https://core.telegram.org/bots/api-changelog#april-11-2025):

  **Business Accounts**

  - Added the class [`aiogram.types.business_bot_rights.BusinessBotRights`](api/types/business_bot_rights.html#aiogram.types.business_bot_rights.BusinessBotRights "aiogram.types.business_bot_rights.BusinessBotRights") and replaced
    the field `can_reply` with the field `rights` of the type
    [`aiogram.types.business_bot_rights.BusinessBotRights`](api/types/business_bot_rights.html#aiogram.types.business_bot_rights.BusinessBotRights "aiogram.types.business_bot_rights.BusinessBotRights") in the class
    [`aiogram.types.business_connection.BusinessConnection`](api/types/business_connection.html#aiogram.types.business_connection.BusinessConnection "aiogram.types.business_connection.BusinessConnection").
  - Added the method [`aiogram.methods.read_business_message.ReadBusinessMessage`](api/methods/read_business_message.html#aiogram.methods.read_business_message.ReadBusinessMessage "aiogram.methods.read_business_message.ReadBusinessMessage"),
    allowing bots to mark incoming messages as read on behalf of a business account.
  - Added the method [`aiogram.methods.delete_business_messages.DeleteBusinessMessages`](api/methods/delete_business_messages.html#aiogram.methods.delete_business_messages.DeleteBusinessMessages "aiogram.methods.delete_business_messages.DeleteBusinessMessages"),
    allowing bots to delete messages on behalf of a business account.
  - Added the method [`aiogram.methods.set_business_account_name.SetBusinessAccountName`](api/methods/set_business_account_name.html#aiogram.methods.set_business_account_name.SetBusinessAccountName "aiogram.methods.set_business_account_name.SetBusinessAccountName"),
    allowing bots to change the first and last name of a managed business account.
  - Added the method [`aiogram.methods.set_business_account_username.SetBusinessAccountUsername`](api/methods/set_business_account_username.html#aiogram.methods.set_business_account_username.SetBusinessAccountUsername "aiogram.methods.set_business_account_username.SetBusinessAccountUsername"),
    allowing bots to change the username of a managed business account.
  - Added the method [`aiogram.methods.set_business_account_bio.SetBusinessAccountBio`](api/methods/set_business_account_bio.html#aiogram.methods.set_business_account_bio.SetBusinessAccountBio "aiogram.methods.set_business_account_bio.SetBusinessAccountBio"),
    allowing bots to change the bio of a managed business account.
  - Added the class [`aiogram.types.input_profile_photo.InputProfilePhoto`](api/types/input_profile_photo.html#aiogram.types.input_profile_photo.InputProfilePhoto "aiogram.types.input_profile_photo.InputProfilePhoto"),
    describing a profile photo to be set.
  - Added the methods [`aiogram.methods.set_business_account_profile_photo.SetBusinessAccountProfilePhoto`](api/methods/set_business_account_profile_photo.html#aiogram.methods.set_business_account_profile_photo.SetBusinessAccountProfilePhoto "aiogram.methods.set_business_account_profile_photo.SetBusinessAccountProfilePhoto")
    and [`aiogram.methods.remove_business_account_profile_photo.RemoveBusinessAccountProfilePhoto`](api/methods/remove_business_account_profile_photo.html#aiogram.methods.remove_business_account_profile_photo.RemoveBusinessAccountProfilePhoto "aiogram.methods.remove_business_account_profile_photo.RemoveBusinessAccountProfilePhoto"),
    allowing bots to change the profile photo of a managed business account.
  - Added the method [`aiogram.methods.set_business_account_gift_settings.SetBusinessAccountGiftSettings`](api/methods/set_business_account_gift_settings.html#aiogram.methods.set_business_account_gift_settings.SetBusinessAccountGiftSettings "aiogram.methods.set_business_account_gift_settings.SetBusinessAccountGiftSettings"),
    allowing bots to change the privacy settings pertaining to incoming gifts in a managed business account.
  - Added the class [`aiogram.types.star_amount.StarAmount`](api/types/star_amount.html#aiogram.types.star_amount.StarAmount "aiogram.types.star_amount.StarAmount") and the method
    [`aiogram.methods.get_business_account_star_balance.GetBusinessAccountStarBalance`](api/methods/get_business_account_star_balance.html#aiogram.methods.get_business_account_star_balance.GetBusinessAccountStarBalance "aiogram.methods.get_business_account_star_balance.GetBusinessAccountStarBalance"),
    allowing bots to check the current Telegram Star balance of a managed business account.
  - Added the method [`aiogram.methods.transfer_business_account_stars.TransferBusinessAccountStars`](api/methods/transfer_business_account_stars.html#aiogram.methods.transfer_business_account_stars.TransferBusinessAccountStars "aiogram.methods.transfer_business_account_stars.TransferBusinessAccountStars"),
    allowing bots to transfer Telegram Stars from the balance of a managed business account to their own balance
    for withdrawal.
  - Added the classes [`aiogram.types.owned_gift_regular.OwnedGiftRegular`](api/types/owned_gift_regular.html#aiogram.types.owned_gift_regular.OwnedGiftRegular "aiogram.types.owned_gift_regular.OwnedGiftRegular"),
    [`aiogram.types.owned_gift_unique.OwnedGiftUnique`](api/types/owned_gift_unique.html#aiogram.types.owned_gift_unique.OwnedGiftUnique "aiogram.types.owned_gift_unique.OwnedGiftUnique"), [`aiogram.types.owned_gifts.OwnedGifts`](api/types/owned_gifts.html#aiogram.types.owned_gifts.OwnedGifts "aiogram.types.owned_gifts.OwnedGifts")
    and the method [`aiogram.methods.get_business_account_gifts.GetBusinessAccountGifts`](api/methods/get_business_account_gifts.html#aiogram.methods.get_business_account_gifts.GetBusinessAccountGifts "aiogram.methods.get_business_account_gifts.GetBusinessAccountGifts"),
    allowing bots to fetch the list of gifts owned by a managed business account.
  - Added the method [`aiogram.methods.convert_gift_to_stars.ConvertGiftToStars`](api/methods/convert_gift_to_stars.html#aiogram.methods.convert_gift_to_stars.ConvertGiftToStars "aiogram.methods.convert_gift_to_stars.ConvertGiftToStars"),
    allowing bots to convert gifts received by a managed business account to Telegram Stars.
  - Added the method [`aiogram.methods.upgrade_gift.UpgradeGift`](api/methods/upgrade_gift.html#aiogram.methods.upgrade_gift.UpgradeGift "aiogram.methods.upgrade_gift.UpgradeGift"),
    allowing bots to upgrade regular gifts received by a managed business account to unique gifts.
  - Added the method [`aiogram.methods.transfer_gift.TransferGift`](api/methods/transfer_gift.html#aiogram.methods.transfer_gift.TransferGift "aiogram.methods.transfer_gift.TransferGift"),
    allowing bots to transfer unique gifts owned by a managed business account.
  - Added the classes [`aiogram.types.input_story_content_photo.InputStoryContentPhoto`](api/types/input_story_content_photo.html#aiogram.types.input_story_content_photo.InputStoryContentPhoto "aiogram.types.input_story_content_photo.InputStoryContentPhoto")
    and [`aiogram.types.input_story_content_video.InputStoryContentVideo`](api/types/input_story_content_video.html#aiogram.types.input_story_content_video.InputStoryContentVideo "aiogram.types.input_story_content_video.InputStoryContentVideo")
    representing the content of a story to post.
  - Added the classes [`aiogram.types.story_area.StoryArea`](api/types/story_area.html#aiogram.types.story_area.StoryArea "aiogram.types.story_area.StoryArea"),
    [`aiogram.types.story_area_position.StoryAreaPosition`](api/types/story_area_position.html#aiogram.types.story_area_position.StoryAreaPosition "aiogram.types.story_area_position.StoryAreaPosition"),
    [`aiogram.types.location_address.LocationAddress`](api/types/location_address.html#aiogram.types.location_address.LocationAddress "aiogram.types.location_address.LocationAddress"),
    [`aiogram.types.story_area_type_location.StoryAreaTypeLocation`](api/types/story_area_type_location.html#aiogram.types.story_area_type_location.StoryAreaTypeLocation "aiogram.types.story_area_type_location.StoryAreaTypeLocation"),
    [`aiogram.types.story_area_type_suggested_reaction.StoryAreaTypeSuggestedReaction`](api/types/story_area_type_suggested_reaction.html#aiogram.types.story_area_type_suggested_reaction.StoryAreaTypeSuggestedReaction "aiogram.types.story_area_type_suggested_reaction.StoryAreaTypeSuggestedReaction"),
    [`aiogram.types.story_area_type_link.StoryAreaTypeLink`](api/types/story_area_type_link.html#aiogram.types.story_area_type_link.StoryAreaTypeLink "aiogram.types.story_area_type_link.StoryAreaTypeLink"),
    [`aiogram.types.story_area_type_weather.StoryAreaTypeWeather`](api/types/story_area_type_weather.html#aiogram.types.story_area_type_weather.StoryAreaTypeWeather "aiogram.types.story_area_type_weather.StoryAreaTypeWeather")
    and [`aiogram.types.story_area_type_unique_gift.StoryAreaTypeUniqueGift`](api/types/story_area_type_unique_gift.html#aiogram.types.story_area_type_unique_gift.StoryAreaTypeUniqueGift "aiogram.types.story_area_type_unique_gift.StoryAreaTypeUniqueGift"),
    describing clickable active areas on stories.
  - Added the methods [`aiogram.methods.post_story.PostStory`](api/methods/post_story.html#aiogram.methods.post_story.PostStory "aiogram.methods.post_story.PostStory"),
    [`aiogram.methods.edit_story.EditStory`](api/methods/edit_story.html#aiogram.methods.edit_story.EditStory "aiogram.methods.edit_story.EditStory")
    and [`aiogram.methods.delete_story.DeleteStory`](api/methods/delete_story.html#aiogram.methods.delete_story.DeleteStory "aiogram.methods.delete_story.DeleteStory"),
    allowing bots to post, edit and delete stories on behalf of a managed business account.

  **Mini Apps**

  - Added the field `DeviceStorage`, allowing Mini Apps to use persistent
    local storage on the user’s device.
  - Added the field `SecureStorage`, allowing Mini Apps to use a secure local
    storage on the user’s device for sensitive data.

  **Gifts**

  - Added the classes [`aiogram.types.unique_gift_model.UniqueGiftModel`](api/types/unique_gift_model.html#aiogram.types.unique_gift_model.UniqueGiftModel "aiogram.types.unique_gift_model.UniqueGiftModel"),
    [`aiogram.types.unique_gift_symbol.UniqueGiftSymbol`](api/types/unique_gift_symbol.html#aiogram.types.unique_gift_symbol.UniqueGiftSymbol "aiogram.types.unique_gift_symbol.UniqueGiftSymbol"),
    [`aiogram.types.unique_gift_backdrop_colors.UniqueGiftBackdropColors`](api/types/unique_gift_backdrop_colors.html#aiogram.types.unique_gift_backdrop_colors.UniqueGiftBackdropColors "aiogram.types.unique_gift_backdrop_colors.UniqueGiftBackdropColors"),
    and [`aiogram.types.unique_gift_backdrop.UniqueGiftBackdrop`](api/types/unique_gift_backdrop.html#aiogram.types.unique_gift_backdrop.UniqueGiftBackdrop "aiogram.types.unique_gift_backdrop.UniqueGiftBackdrop")
    to describe the properties of a unique gift.
  - Added the class [`aiogram.types.unique_gift.UniqueGift`](api/types/unique_gift.html#aiogram.types.unique_gift.UniqueGift "aiogram.types.unique_gift.UniqueGift") describing
    a gift that was upgraded to a unique one.
  - Added the class [`aiogram.types.accepted_gift_types.AcceptedGiftTypes`](api/types/accepted_gift_types.html#aiogram.types.accepted_gift_types.AcceptedGiftTypes "aiogram.types.accepted_gift_types.AcceptedGiftTypes")
    describing the types of gifts that are accepted by a user or a chat.
  - Replaced the field `can_send_gift` with the field `accepted_gift_types`
    of the type [`aiogram.types.accepted_gift_types.AcceptedGiftTypes`](api/types/accepted_gift_types.html#aiogram.types.accepted_gift_types.AcceptedGiftTypes "aiogram.types.accepted_gift_types.AcceptedGiftTypes")
    in the class [`aiogram.types.chat_full_info.ChatFullInfo`](api/types/chat_full_info.html#aiogram.types.chat_full_info.ChatFullInfo "aiogram.types.chat_full_info.ChatFullInfo").
  - Added the class [`aiogram.types.gift_info.GiftInfo`](api/types/gift_info.html#aiogram.types.gift_info.GiftInfo "aiogram.types.gift_info.GiftInfo") and the field `gift`
    to the class [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message"),
    describing a service message about a regular gift that was sent or received.
  - Added the class [`aiogram.types.unique_gift_info.UniqueGiftInfo`](api/types/unique_gift_info.html#aiogram.types.unique_gift_info.UniqueGiftInfo "aiogram.types.unique_gift_info.UniqueGiftInfo")
    and the field `unique_gift` to the class [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message"),
    describing a service message about a unique gift that was sent or received.

  **Telegram Premium**

  - Added the method [`aiogram.methods.gift_premium_subscription.GiftPremiumSubscription`](api/methods/gift_premium_subscription.html#aiogram.methods.gift_premium_subscription.GiftPremiumSubscription "aiogram.methods.gift_premium_subscription.GiftPremiumSubscription"),
    allowing bots to gift a user a Telegram Premium subscription paid in Telegram Stars.
  - Added the field `premium_subscription_duration` to the class
    [`aiogram.types.transaction_partner_user.TransactionPartnerUser`](api/types/transaction_partner_user.html#aiogram.types.transaction_partner_user.TransactionPartnerUser "aiogram.types.transaction_partner_user.TransactionPartnerUser")

  for transactions involving a Telegram Premium subscription purchased by the bot.
  - Added the field `transaction_type` to the class

  > [`aiogram.types.transaction_partner_user.TransactionPartnerUser`](api/types/transaction_partner_user.html#aiogram.types.transaction_partner_user.TransactionPartnerUser "aiogram.types.transaction_partner_user.TransactionPartnerUser"),
  > simplifying the differentiation and processing of all transaction types.

  **General**

  - Increased the maximum price for paid media to 10000 Telegram Stars.
  - Increased the maximum price for a subscription period to 10000 Telegram Stars.
  - Added the class [`aiogram.types.paid_message_price_changed.PaidMessagePriceChanged`](api/types/paid_message_price_changed.html#aiogram.types.paid_message_price_changed.PaidMessagePriceChanged "aiogram.types.paid_message_price_changed.PaidMessagePriceChanged")
    and the field `paid_message_price_changed` to the class
    [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message"), describing a service message about a price change
    for paid messages sent to the chat.
  - Added the field `paid_star_count` to the class [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message"),
    containing the number of Telegram Stars that were paid to send the message.

  [#1671](https://github.com/aiogram/aiogram/issues/1671)

### Bugfixes

- Fix memory exhaustion in polling mode with concurrent updates.

  Added a semaphore-based solution to limit the number of concurrent tasks when using `handle_as_tasks=True` in polling mode.
  This prevents Out of Memory (OOM) errors in memory-limited containers when there’s a large queue of updates to process.
  You can now control the maximum number of concurrent updates with the new `tasks_concurrency_limit`
  parameter in `start_polling()` and `run_polling()` methods.
  [#1658](https://github.com/aiogram/aiogram/issues/1658)
- Fix empty response into webhook.

  We need to return something “empty”, and “empty” form doesn’t work since
  it’s sending only “end” boundary w/o “start”.

  An empty formdata should look smth like this for Telegram to understand:

  ```
  --webhookBoundaryvsF_aMHhspPjfOq7O0JNRg
  --webhookBoundaryvsF_aMHhspPjfOq7O0JNRg--
  ```

  But aiohttp sends only the ending boundary:

  ```
  --webhookBoundaryvsF_aMHhspPjfOq7O0JNRg--
  ```

  Such response doesn’t suit Telegram servers.

  The fix replaces empty response with empty JSON response:

  ```
  {}
  ```

  [#1664](https://github.com/aiogram/aiogram/issues/1664)

### Improved Documentation

- Fixed broken code block formatting in `router.rst` caused by incorrect indentation of directive options.
  [#1666](https://github.com/aiogram/aiogram/issues/1666)

### Misc

- Bump pydantic upper bound from <2.11 to <2.12.
  Upgrading pydantic to version 2.11 significantly reduces resource consumption, more details on the [pydantic blog post](https://pydantic.dev/articles/pydantic-v2-11-release)
  [#1659](https://github.com/aiogram/aiogram/issues/1659)
- Replaced `` `loop.run_in_executor` `` with `` `asyncio.to_thread` `` for improved readability and consistency.
  [#1661](https://github.com/aiogram/aiogram/issues/1661)

## 3.19.0 (2025-03-19)

### Features

- Added TypedDict definitions for middleware context data to the dispatcher dependency injection docs.

  So, now you can use `aiogram.dispatcher.middleware.data.MiddlewareData` directly or
  extend it with your own data in the middlewares.
  [#1637](https://github.com/aiogram/aiogram/issues/1637)
- Added new method [`aiogram.utils.deep_linking.create_startapp_link()`](utils/deep_linking.html#aiogram.utils.deep_linking.create_startapp_link "aiogram.utils.deep_linking.create_startapp_link") to deep-linking module
  for creating “startapp” deep links.
  See also <https://core.telegram.org/api/links#main-mini-app-links> and <https://core.telegram.org/api/links#direct-mini-app-links>
  [#1648](https://github.com/aiogram/aiogram/issues/1648), [#1651](https://github.com/aiogram/aiogram/issues/1651)

### Bugfixes

- Fixed handling of default empty string (“”) in CallbackData filter
  [#1493](https://github.com/aiogram/aiogram/issues/1493)
- Resolved incorrect ordering of registered handlers in the [`aiogram.fsm.scene.Scene`](dispatcher/finite_state_machine/scene.html#aiogram.fsm.scene.Scene "aiogram.fsm.scene.Scene")
  object caused by `inspect.getmembers` returning sorted members.
  Handlers are now registered in the order of their definition within the class,
  ensuring proper execution sequence, especially when handling filters with different
  levels of specificity.

  For backward compatibility, the old behavior can be restored by setting the
  `attrs_resolver=inspect_members_resolver` parameter in the [`aiogram.fsm.scene.Scene`](dispatcher/finite_state_machine/scene.html#aiogram.fsm.scene.Scene "aiogram.fsm.scene.Scene"):

  ```
  from aiogram.utils.class_attrs_resolver import inspect_members_resolver

  class MyScene(Scene, attrs_resolver=inspect_members_resolver):
  ```

  In this case, the handlers will be registered in the order returned by `inspect.getmembers`.

  By default, the `attrs_resolver` parameter is set to `get_sorted_mro_attrs_resolver` now,
  so you **don’t need** to specify it explicitly.
  [#1641](https://github.com/aiogram/aiogram/issues/1641)

### Improved Documentation

- Updated 🇺🇦Ukrainian docs translation
  [#1650](https://github.com/aiogram/aiogram/issues/1650)

### Misc

- Introduce Union types for streamlined type handling.

  Implemented Union types across various modules to consolidate and simplify type annotations.
  This change replaces repetitive union declarations with reusable Union aliases,
  improving code readability and maintainability.
  [#1592](https://github.com/aiogram/aiogram/issues/1592)

## 3.18.0 (2025-02-16)

### Features

- Added full support for the [Bot API 8.3](https://core.telegram.org/bots/api-changelog#february-12-2025):

  - Added the parameter `chat_id` to the method [`aiogram.methods.send_gift.SendGift`](api/methods/send_gift.html#aiogram.methods.send_gift.SendGift "aiogram.methods.send_gift.SendGift"), allowing bots to send gifts to channel chats.
  - Added the field `can_send_gift` to the class [`aiogram.types.chat_full_info.ChatFullInfo`](api/types/chat_full_info.html#aiogram.types.chat_full_info.ChatFullInfo "aiogram.types.chat_full_info.ChatFullInfo").
  - Added the class [`aiogram.types.transaction_partner_chat.TransactionPartnerChat`](api/types/transaction_partner_chat.html#aiogram.types.transaction_partner_chat.TransactionPartnerChat "aiogram.types.transaction_partner_chat.TransactionPartnerChat") describing transactions with chats.
  - Added the fields `cover` and `start_timestamp` to the class [`aiogram.types.video.Video`](api/types/video.html#aiogram.types.video.Video "aiogram.types.video.Video"), containing a message-specific cover and a start timestamp for the video.
  - Added the parameters `cover` and `start_timestamp` to the method [`aiogram.methods.send_video.SendVideo`](api/methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo"), allowing bots to specify a cover and a start timestamp for the videos they send.
  - Added the fields `cover` and `start_timestamp` to the classes [`aiogram.types.input_media_video.InputMediaVideo`](api/types/input_media_video.html#aiogram.types.input_media_video.InputMediaVideo "aiogram.types.input_media_video.InputMediaVideo") and [`aiogram.types.input_paid_media_video.InputPaidMediaVideo`](api/types/input_paid_media_video.html#aiogram.types.input_paid_media_video.InputPaidMediaVideo "aiogram.types.input_paid_media_video.InputPaidMediaVideo"), allowing bots to edit video covers and start timestamps, and specify them for videos in albums and paid media.
  - Added the parameter `video_start_timestamp` to the methods [`aiogram.methods.forward_message.ForwardMessage`](api/methods/forward_message.html#aiogram.methods.forward_message.ForwardMessage "aiogram.methods.forward_message.ForwardMessage") and [`aiogram.methods.copy_message.CopyMessage`](api/methods/copy_message.html#aiogram.methods.copy_message.CopyMessage "aiogram.methods.copy_message.CopyMessage"), allowing bots to change the start timestamp for forwarded and copied videos.
  - Allowed adding reactions to most types of service messages.

  [#1638](https://github.com/aiogram/aiogram/issues/1638)

### Bugfixes

- Fixed endless loop while adding buttons to the `KeyboardBuilder`.
  [#1595](https://github.com/aiogram/aiogram/issues/1595)
- Change the `Downloadable` protocol to be non-writable to shut up type checking that checks code that uses the `bot.download(...)` method
  [#1628](https://github.com/aiogram/aiogram/issues/1628)
- Fix the regex pattern that finds the “bad characters” for deeplink payload.
  [#1630](https://github.com/aiogram/aiogram/issues/1630)

### Improved Documentation

- Update `data: Dict[Any, str]` to `data: Dict[str, Any]`
  [#1634](https://github.com/aiogram/aiogram/issues/1634)
- Fix small typo in the Scenes documentation
  [#1640](https://github.com/aiogram/aiogram/issues/1640)

### Misc

- Removed redundant `Path` to `str` convertion on file download.
  [#1612](https://github.com/aiogram/aiogram/issues/1612)
- Increased max `redis` version support from “<5.1.0” to “<5.3.0”
  [#1631](https://github.com/aiogram/aiogram/issues/1631)

## 3.17.0 (2025-01-02)

### Features

- Added full support of the [Bot API 8.2](https://core.telegram.org/bots/api-changelog#january-1-2025)

  - Added the methods [`aiogram.methods.verify_user.VerifyUser`](api/methods/verify_user.html#aiogram.methods.verify_user.VerifyUser "aiogram.methods.verify_user.VerifyUser"), [`aiogram.methods.verify_chat.VerifyChat`](api/methods/verify_chat.html#aiogram.methods.verify_chat.VerifyChat "aiogram.methods.verify_chat.VerifyChat"), [`aiogram.methods.remove_user_verification.RemoveUserVerification`](api/methods/remove_user_verification.html#aiogram.methods.remove_user_verification.RemoveUserVerification "aiogram.methods.remove_user_verification.RemoveUserVerification") and [`aiogram.methods.remove_chat_verification.RemoveChatVerification`](api/methods/remove_chat_verification.html#aiogram.methods.remove_chat_verification.RemoveChatVerification "aiogram.methods.remove_chat_verification.RemoveChatVerification"), allowing bots to manage verifications on behalf of an organization.
  - Added the field `upgrade_star_count` to the class [`aiogram.types.gift.Gift`](api/types/gift.html#aiogram.types.gift.Gift "aiogram.types.gift.Gift").
  - Added the parameter `pay_for_upgrade` to the method [`aiogram.methods.send_gift.SendGift`](api/methods/send_gift.html#aiogram.methods.send_gift.SendGift "aiogram.methods.send_gift.SendGift").
  - Removed the field `hide_url` from the class [`aiogram.types.inline_query_result_article.InlineQueryResultArticle`](api/types/inline_query_result_article.html#aiogram.types.inline_query_result_article.InlineQueryResultArticle "aiogram.types.inline_query_result_article.InlineQueryResultArticle"). Pass an empty string as `url` instead.

  [#1623](https://github.com/aiogram/aiogram/issues/1623)

## 3.16.0 (2024-12-21)

### Features

- Added full support of [Bot API 8.1](https://core.telegram.org/bots/api-changelog#december-4-2024):

  - Added the field `nanostar_amount` to the class [`aiogram.types.star_transaction.StarTransaction`](api/types/star_transaction.html#aiogram.types.star_transaction.StarTransaction "aiogram.types.star_transaction.StarTransaction").
  - Added the class [`aiogram.types.transaction_partner_affiliate_program.TransactionPartnerAffiliateProgram`](api/types/transaction_partner_affiliate_program.html#aiogram.types.transaction_partner_affiliate_program.TransactionPartnerAffiliateProgram "aiogram.types.transaction_partner_affiliate_program.TransactionPartnerAffiliateProgram") for transactions pertaining to incoming affiliate commissions.
  - Added the class [`aiogram.types.affiliate_info.AffiliateInfo`](api/types/affiliate_info.html#aiogram.types.affiliate_info.AffiliateInfo "aiogram.types.affiliate_info.AffiliateInfo") and the field `affiliate` to the class [`aiogram.types.transaction_partner_user.TransactionPartnerUser`](api/types/transaction_partner_user.html#aiogram.types.transaction_partner_user.TransactionPartnerUser "aiogram.types.transaction_partner_user.TransactionPartnerUser"), allowing bots to identify the relevant affiliate in transactions with an affiliate commission.

  [#1617](https://github.com/aiogram/aiogram/issues/1617)

### Bugfixes

- Corrected the exception text of aiogram.methods.base.TelegramMethod.__await__ method.
  [#1616](https://github.com/aiogram/aiogram/issues/1616)

### Misc

- Increased max `pydantic` version support from “<2.10” to “<2.11”
  [#1607](https://github.com/aiogram/aiogram/issues/1607)
- Fixed closing tag for `tg-emoji` in the `aiogram.utils.text_decoration.HtmlDecoration`: use the same constant as for tag opening
  [#1608](https://github.com/aiogram/aiogram/issues/1608)
- Increased max `aiohttp` version support from “<3.11” to “<3.12”
  [#1615](https://github.com/aiogram/aiogram/issues/1615)

## 3.15.0 (2024-11-17)

### Features

- Added full support for [Bot API 8.0](https://core.telegram.org/bots/api-changelog#november-17-2024)

  - Added the parameter `subscription_period` to the method
    [`aiogram.methods.create_invoice_link.CreateInvoiceLink`](api/methods/create_invoice_link.html#aiogram.methods.create_invoice_link.CreateInvoiceLink "aiogram.methods.create_invoice_link.CreateInvoiceLink")
    to support the creation of links that are billed periodically.
  - Added the parameter `business_connection_id` to the method
    [`aiogram.methods.create_invoice_link.CreateInvoiceLink`](api/methods/create_invoice_link.html#aiogram.methods.create_invoice_link.CreateInvoiceLink "aiogram.methods.create_invoice_link.CreateInvoiceLink")
    to support the creation of invoice links on behalf of business accounts.
  - Added the fields `subscription_expiration_date`,
    `is_recurring` and `is_first_recurring` to the class
    [`aiogram.types.successful_payment.SuccessfulPayment`](api/types/successful_payment.html#aiogram.types.successful_payment.SuccessfulPayment "aiogram.types.successful_payment.SuccessfulPayment").
  - Added the method [`aiogram.methods.edit_user_star_subscription.EditUserStarSubscription`](api/methods/edit_user_star_subscription.html#aiogram.methods.edit_user_star_subscription.EditUserStarSubscription "aiogram.methods.edit_user_star_subscription.EditUserStarSubscription").
  - Added the field `subscription_period` to the class
    [`aiogram.types.transaction_partner_user.TransactionPartnerUser`](api/types/transaction_partner_user.html#aiogram.types.transaction_partner_user.TransactionPartnerUser "aiogram.types.transaction_partner_user.TransactionPartnerUser").
  - Added the method [`aiogram.methods.set_user_emoji_status.SetUserEmojiStatus`](api/methods/set_user_emoji_status.html#aiogram.methods.set_user_emoji_status.SetUserEmojiStatus "aiogram.methods.set_user_emoji_status.SetUserEmojiStatus").
    The user must allow the bot to manage their emoji status.
  - Added the class [`aiogram.types.prepared_inline_message.PreparedInlineMessage`](api/types/prepared_inline_message.html#aiogram.types.prepared_inline_message.PreparedInlineMessage "aiogram.types.prepared_inline_message.PreparedInlineMessage")
    and the method [`aiogram.methods.save_prepared_inline_message.SavePreparedInlineMessage`](api/methods/save_prepared_inline_message.html#aiogram.methods.save_prepared_inline_message.SavePreparedInlineMessage "aiogram.methods.save_prepared_inline_message.SavePreparedInlineMessage"),
    allowing bots to suggest users send a specific message from a Mini App via the method
    `aiogram.methods.share_message.ShareMessage`.
  - Added the classes [`aiogram.types.gift.Gift`](api/types/gift.html#aiogram.types.gift.Gift "aiogram.types.gift.Gift") and [`aiogram.types.gifts.Gifts`](api/types/gifts.html#aiogram.types.gifts.Gifts "aiogram.types.gifts.Gifts")
    and the method [`aiogram.methods.get_available_gifts.GetAvailableGifts`](api/methods/get_available_gifts.html#aiogram.methods.get_available_gifts.GetAvailableGifts "aiogram.methods.get_available_gifts.GetAvailableGifts"),
    allowing bots to get all gifts available for sending.
  - Added the field `gift` to the class
    [`aiogram.types.transaction_partner_user.TransactionPartnerUser`](api/types/transaction_partner_user.html#aiogram.types.transaction_partner_user.TransactionPartnerUser "aiogram.types.transaction_partner_user.TransactionPartnerUser").

  [#1606](https://github.com/aiogram/aiogram/issues/1606)

## 3.14.0 (2024-11-02)

### Misc

- Checked compatibility with Python 3.13 (added to the CI/CD processes),
  so now aiogram is totally compatible with it.

  Dropped compatibility with Python 3.8 due to this version being [EOL](https://devguide.python.org/versions/).

  Warning

  In some cases you will need to have the installed compiler (Rust or C++)
  to install some of the dependencies to compile packages from source on pip install command.

  - If you are using Windows, you will need to have the [Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/) installed.
  - If you are using Linux, you will need to have the build-essential package installed.
  - If you are using macOS, you will need to have the [Xcode](https://developer.apple.com/xcode/) installed.

  When developers of this dependencies will release new versions with precompiled wheels for Windows, Linux and macOS,
  this action will not be necessary anymore until the next version of the Python interpreter.

  [#1589](https://github.com/aiogram/aiogram/issues/1589)
- Added business_connection_id to the [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") API methods shortcuts.

  Integrated the `business_connection_id` attribute into various message manipulation methods,
  ensuring consistent data handling. This update eliminates the need to pass the
  `business_connection_id` as a parameter,
  instead directly accessing it from the instance attributes.
  [#1586](https://github.com/aiogram/aiogram/issues/1586)

### Features

- Add function `get_value` to all built-in storage implementations, `FSMContext` and `SceneWizard`
  [#1431](https://github.com/aiogram/aiogram/issues/1431)
- Enhanced the inheritance of handlers and actions in [Scenes](dispatcher/finite_state_machine/scene.html#scenes).
  Refactored to eliminate the copying of previously connected handlers and actions from parent scenes.
  Now, handlers are dynamically rebuilt based on the current class, properly utilizing class inheritance and enabling handler overrides.

  That’s mean that you can now override handlers and actions in the child scene, instead of copying and duplicating them.
  [#1583](https://github.com/aiogram/aiogram/issues/1583)
- Added full support of [Bot API 7.11](https://core.telegram.org/bots/api-changelog#october-31-2024)

  - Added the class [`aiogram.types.copy_text_button.CopyTextButton`](api/types/copy_text_button.html#aiogram.types.copy_text_button.CopyTextButton "aiogram.types.copy_text_button.CopyTextButton")
    and the field `copy_text` in the class
    [`aiogram.types.inline_keyboard_button.InlineKeyboardButton`](api/types/inline_keyboard_button.html#aiogram.types.inline_keyboard_button.InlineKeyboardButton "aiogram.types.inline_keyboard_button.InlineKeyboardButton"),
    allowing bots to send and receive inline buttons that copy arbitrary text.
  - Added the parameter `allow_paid_broadcast` to the methods
    [`aiogram.methods.send_message.SendMessage`](api/methods/send_message.html#aiogram.methods.send_message.SendMessage "aiogram.methods.send_message.SendMessage"),
    [`aiogram.methods.send_photo.SendPhoto`](api/methods/send_photo.html#aiogram.methods.send_photo.SendPhoto "aiogram.methods.send_photo.SendPhoto"),
    [`aiogram.methods.send_video.SendVideo`](api/methods/send_video.html#aiogram.methods.send_video.SendVideo "aiogram.methods.send_video.SendVideo"),
    [`aiogram.methods.send_animation.SendAnimation`](api/methods/send_animation.html#aiogram.methods.send_animation.SendAnimation "aiogram.methods.send_animation.SendAnimation"),
    [`aiogram.methods.send_audio.SendAudio`](api/methods/send_audio.html#aiogram.methods.send_audio.SendAudio "aiogram.methods.send_audio.SendAudio"),
    [`aiogram.methods.send_document.SendDocument`](api/methods/send_document.html#aiogram.methods.send_document.SendDocument "aiogram.methods.send_document.SendDocument"),
    [`aiogram.methods.send_paid_media.SendPaidMedia`](api/methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia"),
    [`aiogram.methods.send_sticker.SendSticker`](api/methods/send_sticker.html#aiogram.methods.send_sticker.SendSticker "aiogram.methods.send_sticker.SendSticker"),
    [`aiogram.methods.send_video_note.SendVideoNote`](api/methods/send_video_note.html#aiogram.methods.send_video_note.SendVideoNote "aiogram.methods.send_video_note.SendVideoNote"),
    [`aiogram.methods.send_voice.SendVoice`](api/methods/send_voice.html#aiogram.methods.send_voice.SendVoice "aiogram.methods.send_voice.SendVoice"),
    [`aiogram.methods.send_location.SendLocation`](api/methods/send_location.html#aiogram.methods.send_location.SendLocation "aiogram.methods.send_location.SendLocation"),
    [`aiogram.methods.send_venue.SendVenue`](api/methods/send_venue.html#aiogram.methods.send_venue.SendVenue "aiogram.methods.send_venue.SendVenue"),
    [`aiogram.methods.send_contact.SendContact`](api/methods/send_contact.html#aiogram.methods.send_contact.SendContact "aiogram.methods.send_contact.SendContact"),
    [`aiogram.methods.send_poll.SendPoll`](api/methods/send_poll.html#aiogram.methods.send_poll.SendPoll "aiogram.methods.send_poll.SendPoll"),
    [`aiogram.methods.send_dice.SendDice`](api/methods/send_dice.html#aiogram.methods.send_dice.SendDice "aiogram.methods.send_dice.SendDice"),
    [`aiogram.methods.send_invoice.SendInvoice`](api/methods/send_invoice.html#aiogram.methods.send_invoice.SendInvoice "aiogram.methods.send_invoice.SendInvoice"),
    [`aiogram.methods.send_game.SendGame`](api/methods/send_game.html#aiogram.methods.send_game.SendGame "aiogram.methods.send_game.SendGame"),
    [`aiogram.methods.send_media_group.SendMediaGroup`](api/methods/send_media_group.html#aiogram.methods.send_media_group.SendMediaGroup "aiogram.methods.send_media_group.SendMediaGroup")
    and [`aiogram.methods.copy_message.CopyMessage`](api/methods/copy_message.html#aiogram.methods.copy_message.CopyMessage "aiogram.methods.copy_message.CopyMessage").
  - Added the class
    [`aiogram.types.transaction_partner_telegram_api.TransactionPartnerTelegramApi`](api/types/transaction_partner_telegram_api.html#aiogram.types.transaction_partner_telegram_api.TransactionPartnerTelegramApi "aiogram.types.transaction_partner_telegram_api.TransactionPartnerTelegramApi")
    for transactions related to paid broadcasted messages.
  - Introduced the ability to add media to existing text messages using the method
    [`aiogram.methods.edit_message_media.EditMessageMedia`](api/methods/edit_message_media.html#aiogram.methods.edit_message_media.EditMessageMedia "aiogram.methods.edit_message_media.EditMessageMedia").
  - Added support for hashtag and cashtag entities with a specified chat username
    that opens a search for the relevant tag within the specified chat.

  [#1601](https://github.com/aiogram/aiogram/issues/1601)

### Bugfixes

- Fix PytestDeprecationWarning thrown by pytest-asyncio when running the tests
  [#1584](https://github.com/aiogram/aiogram/issues/1584)
- Fixed customized serialization in the [`aiogram.filters.callback_data.CallbackData`](dispatcher/filters/callback_data.html#aiogram.filters.callback_data.CallbackData "aiogram.filters.callback_data.CallbackData") factory.

  From now UUID will have 32 bytes length instead of 36 bytes (with no - separators) in the callback data representation.
  [#1602](https://github.com/aiogram/aiogram/issues/1602)

### Improved Documentation

- Add missing closing tag for bold.
  [#1599](https://github.com/aiogram/aiogram/issues/1599)

## 3.13.1 (2024-09-18)

Warning

**Python 3.8 End of Life**: Python 3.8 will reach its end of life (EOL) soon and will no longer
be supported by aiogram in the next releases (1-2 months ETA).

Please upgrade to a newer version of Python to ensure compatibility and receive future updates.

### Misc

- Increase max pydantic version support “<2.9” -> “<2.10” (only For Python >=3.9)
  [#1576](https://github.com/aiogram/aiogram/issues/1576)
- Bump aiofiles version upper bound to <24.2
  [#1577](https://github.com/aiogram/aiogram/issues/1577)

### Bugfixes

- Fixed Default object annotation resolution using pydantic
  [#1579](https://github.com/aiogram/aiogram/issues/1579)

## 3.13.0 (2024-09-08)

### Features

- - Added updates about purchased paid media, represented by the class
    [`aiogram.types.paid_media_purchased.PaidMediaPurchased`](api/types/paid_media_purchased.html#aiogram.types.paid_media_purchased.PaidMediaPurchased "aiogram.types.paid_media_purchased.PaidMediaPurchased")
    and the field `purchased_paid_media` in the class
    [`aiogram.types.update.Update`](api/types/update.html#aiogram.types.update.Update "aiogram.types.update.Update").
  - Added the ability to specify a payload in
    [`aiogram.methods.send_paid_media.SendPaidMedia`](api/methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia") that is received back by the bot in
    [`aiogram.types.transaction_partner_user.TransactionPartnerUser`](api/types/transaction_partner_user.html#aiogram.types.transaction_partner_user.TransactionPartnerUser "aiogram.types.transaction_partner_user.TransactionPartnerUser")
    and `purchased_paid_media` updates.
  - Added the field `prize_star_count` to the classes
    [`aiogram.types.giveaway_created.GiveawayCreated`](api/types/giveaway_created.html#aiogram.types.giveaway_created.GiveawayCreated "aiogram.types.giveaway_created.GiveawayCreated"),
    [`aiogram.types.giveaway.Giveaway`](api/types/giveaway.html#aiogram.types.giveaway.Giveaway "aiogram.types.giveaway.Giveaway"),
    [`aiogram.types.giveaway_winners.GiveawayWinners`](api/types/giveaway_winners.html#aiogram.types.giveaway_winners.GiveawayWinners "aiogram.types.giveaway_winners.GiveawayWinners")
    and [`aiogram.types.chat_boost_source_giveaway.ChatBoostSourceGiveaway`](api/types/chat_boost_source_giveaway.html#aiogram.types.chat_boost_source_giveaway.ChatBoostSourceGiveaway "aiogram.types.chat_boost_source_giveaway.ChatBoostSourceGiveaway").
  - Added the field `is_star_giveaway` to the class
    [`aiogram.types.giveaway_completed.GiveawayCompleted`](api/types/giveaway_completed.html#aiogram.types.giveaway_completed.GiveawayCompleted "aiogram.types.giveaway_completed.GiveawayCompleted").

  [#1510](https://github.com/aiogram/aiogram/issues/1510)
- Added missing method aliases such as .answer(), .reply(), and others to InaccessibleMessage.
  This change ensures consistency and improves usability by aligning the functionality of InaccessibleMessage with the Message type.
  [#1574](https://github.com/aiogram/aiogram/issues/1574)

### Bugfixes

- Fixed link preview options to use global defaults in various types and methods
  to use global defaults for link_preview_options.
  This change ensures consistency and enhances flexibility in handling link preview options
  across different components.
  [#1543](https://github.com/aiogram/aiogram/issues/1543)

## 3.12.0 (2024-08-16)

### Features

- Added **message_thread_id** parameter to **message.get_url()**.
  [#1451](https://github.com/aiogram/aiogram/issues/1451)
- Added getting user from chat_boost with source ChatBoostSourcePremium in UserContextMiddleware for EventContext
  [#1474](https://github.com/aiogram/aiogram/issues/1474)
- Added full support of [Bot API 7.8](https://core.telegram.org/bots/api-changelog#august-14-2024)

  - Added the ability to send paid media to any chat.
  - Added the parameter `business_connection_id` to the method
    [`aiogram.methods.send_paid_media.SendPaidMedia`](api/methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia"),
    allowing bots to send paid media on behalf of a business account.
  - Added the field `paid_media` to the class
    [`aiogram.types.transaction_partner_user.TransactionPartnerUser`](api/types/transaction_partner_user.html#aiogram.types.transaction_partner_user.TransactionPartnerUser "aiogram.types.transaction_partner_user.TransactionPartnerUser")
    for transactions involving paid media.
  - Added the method
    [`aiogram.methods.create_chat_subscription_invite_link.CreateChatSubscriptionInviteLink`](api/methods/create_chat_subscription_invite_link.html#aiogram.methods.create_chat_subscription_invite_link.CreateChatSubscriptionInviteLink "aiogram.methods.create_chat_subscription_invite_link.CreateChatSubscriptionInviteLink"),
    allowing bots to create subscription invite links.
  - Added the method
    [`aiogram.methods.edit_chat_subscription_invite_link.EditChatSubscriptionInviteLink`](api/methods/edit_chat_subscription_invite_link.html#aiogram.methods.edit_chat_subscription_invite_link.EditChatSubscriptionInviteLink "aiogram.methods.edit_chat_subscription_invite_link.EditChatSubscriptionInviteLink"),
    allowing bots to edit the name of subscription invite links.
  - Added the field `until_date` to the class
    [`aiogram.types.chat_member_member.ChatMemberMember`](api/types/chat_member_member.html#aiogram.types.chat_member_member.ChatMemberMember "aiogram.types.chat_member_member.ChatMemberMember") for members with an active subscription.
  - Added support for paid reactions and the class
    [`aiogram.types.reaction_type_paid.ReactionTypePaid`](api/types/reaction_type_paid.html#aiogram.types.reaction_type_paid.ReactionTypePaid "aiogram.types.reaction_type_paid.ReactionTypePaid").

  [#1560](https://github.com/aiogram/aiogram/issues/1560)

### Misc

- Improved performance of StatesGroup
  [#1507](https://github.com/aiogram/aiogram/issues/1507)

## 3.11.0 (2024-08-09)

### Features

- Added full support of [Bot API 7.8](https://core.telegram.org/bots/api-changelog#july-31-2024)

  - Added the field `has_main_web_app` to the class [`aiogram.types.user.User`](api/types/user.html#aiogram.types.user.User "aiogram.types.user.User"),
    which is returned in the response to [`aiogram.methods.get_me.GetMe`](api/methods/get_me.html#aiogram.methods.get_me.GetMe "aiogram.methods.get_me.GetMe").
  - Added the parameter `business_connection_id` to the methods
    [`aiogram.methods.pin_chat_message.PinChatMessage`](api/methods/pin_chat_message.html#aiogram.methods.pin_chat_message.PinChatMessage "aiogram.methods.pin_chat_message.PinChatMessage")
    and [`aiogram.methods.unpin_chat_message.UnpinChatMessage`](api/methods/unpin_chat_message.html#aiogram.methods.unpin_chat_message.UnpinChatMessage "aiogram.methods.unpin_chat_message.UnpinChatMessage"),
    allowing bots to manage pinned messages on behalf of a business account.

  [#1551](https://github.com/aiogram/aiogram/issues/1551)

### Bugfixes

- Fixed URL path in the “Open” button at the “demo/sendMessage” endpoint in the web_app example.
  [#1546](https://github.com/aiogram/aiogram/issues/1546)

### Misc

- Added method [`aiogram.types.message.Message.as_reply_parameters()`](api/types/message.html#aiogram.types.message.Message.as_reply_parameters "aiogram.types.message.Message.as_reply_parameters").
  Replaced usage of the argument `reply_to_message_id` with `reply_parameters`
  in all Message reply methods.
  [#1538](https://github.com/aiogram/aiogram/issues/1538)
- Added [aiohttp v3.10](https://github.com/aio-libs/aiohttp/releases/tag/v3.10.0) ` support.
  [#1548](https://github.com/aiogram/aiogram/issues/1548)

## 3.10.0 (2024-07-07)

### Features

- Added full support of [Bot API 7.7](https://core.telegram.org/bots/api-changelog#july-7-2024)

  - Added the class [`aiogram.types.refunded_payment.RefundedPayment`](api/types/refunded_payment.html#aiogram.types.refunded_payment.RefundedPayment "aiogram.types.refunded_payment.RefundedPayment"),
    containing information about a refunded payment.
  - Added the field `refunded_payment` to the class
    [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message"),
    describing a service message about a refunded payment.

  [#1536](https://github.com/aiogram/aiogram/issues/1536)

## 3.9.0 (2024-07-06)

### Features

- Added ChatMember resolution tool and updated 2.x migration guide.
  [#1525](https://github.com/aiogram/aiogram/issues/1525)
- Added full support of [Bot API 7.6](https://core.telegram.org/bots/api-changelog#july-1-2024)

  - Added the classes [`aiogram.types.paid_media.PaidMedia`](api/types/paid_media.html#aiogram.types.paid_media.PaidMedia "aiogram.types.paid_media.PaidMedia"),
    :   [`aiogram.types.paid_media_info.PaidMediaInfo`](api/types/paid_media_info.html#aiogram.types.paid_media_info.PaidMediaInfo "aiogram.types.paid_media_info.PaidMediaInfo"),
        [`aiogram.types.paid_media_preview.PaidMediaPreview`](api/types/paid_media_preview.html#aiogram.types.paid_media_preview.PaidMediaPreview "aiogram.types.paid_media_preview.PaidMediaPreview"),
        [`aiogram.types.paid_media_photo.PaidMediaPhoto`](api/types/paid_media_photo.html#aiogram.types.paid_media_photo.PaidMediaPhoto "aiogram.types.paid_media_photo.PaidMediaPhoto")
        and [`aiogram.types.paid_media_video.PaidMediaVideo`](api/types/paid_media_video.html#aiogram.types.paid_media_video.PaidMediaVideo "aiogram.types.paid_media_video.PaidMediaVideo"),
        containing information about paid media.
  - Added the method [`aiogram.methods.send_paid_media.SendPaidMedia`](api/methods/send_paid_media.html#aiogram.methods.send_paid_media.SendPaidMedia "aiogram.methods.send_paid_media.SendPaidMedia")
    :   and the classes [`aiogram.types.input_paid_media.InputPaidMedia`](api/types/input_paid_media.html#aiogram.types.input_paid_media.InputPaidMedia "aiogram.types.input_paid_media.InputPaidMedia"),
        [`aiogram.types.input_paid_media_photo.InputPaidMediaPhoto`](api/types/input_paid_media_photo.html#aiogram.types.input_paid_media_photo.InputPaidMediaPhoto "aiogram.types.input_paid_media_photo.InputPaidMediaPhoto")
        and [`aiogram.types.input_paid_media_video.InputPaidMediaVideo`](api/types/input_paid_media_video.html#aiogram.types.input_paid_media_video.InputPaidMediaVideo "aiogram.types.input_paid_media_video.InputPaidMediaVideo"),
        to support sending paid media.
  - Documented that the methods [`aiogram.methods.copy_message.CopyMessage`](api/methods/copy_message.html#aiogram.methods.copy_message.CopyMessage "aiogram.methods.copy_message.CopyMessage")
    :   and [`aiogram.methods.copy_messages.CopyMessages`](api/methods/copy_messages.html#aiogram.methods.copy_messages.CopyMessages "aiogram.methods.copy_messages.CopyMessages") cannot be used to copy paid media.
  - Added the field `can_send_paid_media` to the class
    :   [`aiogram.types.chat_full_info.ChatFullInfo`](api/types/chat_full_info.html#aiogram.types.chat_full_info.ChatFullInfo "aiogram.types.chat_full_info.ChatFullInfo").
  - Added the field `paid_media` to the classes
    :   [`aiogram.types.message.Message`](api/types/message.html#aiogram.types.message.Message "aiogram.types.message.Message") and
        [`aiogram.types.external_reply_info.ExternalReplyInfo`](api/types/external_reply_info.html#aiogram.types.external_reply_info.ExternalReplyInfo "aiogram.types.external_reply_info.ExternalReplyInfo").
  - Added the class
    :   [`aiogram.types.transaction_partner_telegram_ads.TransactionPartnerTelegramAds`](api/types/transaction_partner_telegram_ads.html#aiogram.types.transaction_partner_telegram_ads.TransactionPartnerTelegramAds "aiogram.types.transaction_partner_telegram_ads.TransactionPartnerTelegramAds"),
        containing information about Telegram Star transactions involving the Telegram Ads Platform.
  - Added the field `invoice_payload` to the class
    :   [`aiogram.types.transaction_partner_user.TransactionPartnerUser`](api/types/transaction_partner_user.html#aiogram.types.transaction_partner_user.TransactionPartnerUser "aiogram.types.transaction_partner_user.TransactionPartnerUser"),
        containing the bot-specified invoice payload.
  - Changed the default opening mode for Direct Link Mini Apps.
  - Added support for launching Web Apps via t.me link in the class
    :   [`aiogram.types.menu_button_web_app.MenuButtonWebApp`](api/types/menu_button_web_app.html#aiogram.types.menu_button_web_app.MenuButtonWebApp "aiogram.types.menu_button_web_app.MenuButtonWebApp").
  - Added the field `section_separator_color` to the class `ThemeParams`.

  [#1533](https://github.com/aiogram/aiogram/issues/1533)

### Bugfixes

- Fixed event context resolving for the callback query that is coming from the business account
  [#1520](https://github.com/aiogram/aiogram/issues/1520)

## 3.8.0 (2024-06-19)

### Features

- Added utility to safely deserialize any Telegram object or method to a JSON-compatible object (dict).
  ([>> Read more](utils/serialization.html#serialization-tool))
  [#1450](https://github.com/aiogram/aiogram/issues/1450)
- Added full support of [Bot API 7.5](https://core.telegram.org/bots/api-changelog#june-18-2024)

  - Added the classes [`aiogram.types.star_transactions.StarTransactions`](api/types/star_transactions.html#aiogram.types.star_transactions.StarTransactions "aiogram.types.star_transactions.StarTransactions"),
    :   [`aiogram.types.star_transaction.StarTransaction`](api/types/star_transaction.html#aiogram.types.star_transaction.StarTransaction "aiogram.types.star_transaction.StarTransaction"),
        [`aiogram.types.transaction_partner.TransactionPartner`](api/types/transaction_partner.html#aiogram.types.transaction_partner.TransactionPartner "aiogram.types.transaction_partner.TransactionPartner")
        and [`aiogram.types.revenue_withdrawal_state.RevenueWithdrawalState`](api/types/revenue_withdrawal_state.html#aiogram.types.revenue_withdrawal_state.RevenueWithdrawalState "aiogram.types.revenue_withdrawal_state.RevenueWithdrawalState"),
        containing information about Telegram Star transactions involving the bot.
  - Added the method [`aiogram.methods.get_star_transactions.GetStarTransactions`](api/methods/get_star_transactions.html#aiogram.methods.get_star_transactions.GetStarTransactions "aiogram.methods.get_star_transactions.GetStarTransactions")
    :   that can be used to get the list of all Telegram Star transactions for the bot.
  - Added support for callback buttons in
    :   [`aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup`](api/types/inline_keyboard_markup.html#aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup "aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup")
        for messages sent on behalf of a business account.
  - Added support for callback queries originating from a message sent
    :   on behalf of a business account.
  - Added the parameter `business_connection_id` to the methods
    :   [`aiogram.methods.edit_message_text.EditMessageText`](api/methods/edit_message_text.html#aiogram.methods.edit_message_text.EditMessageText "aiogram.methods.edit_message_text.EditMessageText"),
        [`aiogram.methods.edit_message_media.EditMessageMedia`](api/methods/edit_message_media.html#aiogram.methods.edit_message_media.EditMessageMedia "aiogram.methods.edit_message_media.EditMessageMedia"),
        [`aiogram.methods.edit_message_caption.EditMessageCaption`](api/methods/edit_message_caption.html#aiogram.methods.edit_message_caption.EditMessageCaption "aiogram.methods.edit_message_caption.EditMessageCaption"),
        [`aiogram.methods.edit_message_live_location.EditMessageLiveLocation`](api/methods/edit_message_live_location.html#aiogram.methods.edit_message_live_location.EditMessageLiveLocation "aiogram.methods.edit_message_live_location.EditMessageLiveLocation"),
        [`aiogram.methods.stop_message_live_location.StopMessageLiveLocation`](api/methods/stop_message_live_location.html#aiogram.methods.stop_message_live_location.StopMessageLiveLocation "aiogram.methods.stop_message_live_location.StopMessageLiveLocation")
        and [`aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup`](api/methods/edit_message_reply_markup.html#aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup "aiogram.methods.edit_message_reply_markup.EditMessageReplyMarkup"),
        allowing the bot to edit business messages.
  - Added the parameter `business_connection_id` to the method
    :   [`aiogram.methods.stop_poll.StopPoll`](api/methods/stop_poll.html#aiogram.methods.stop_poll.StopPoll "aiogram.methods.stop_poll.StopPoll"),
        allowing the bot to stop polls it sent on behalf of a business account.

  [#1518](https://github.com/aiogram/aiogram/issues/1518)

### Bugfixes

- Increased DNS cache ttl setting to aiohttp session as a workaround for DNS resolution issues in aiohttp.
  [#1500](https://github.com/aiogram/aiogram/issues/1500)

### Improved Documentation

- Fixed MongoStorage section in the documentation by adding extra dependency to ReadTheDocs configuration.
  [#1501](https://github.com/aiogram/aiogram/issues/1501)
- Added information about dependency changes to the `2.x --> 3.x` migration guide.
  [#1504](https://github.com/aiogram/aiogram/issues/1504)

### Misc

- [Only for contributors] Fail redis and mongo tests if incorrect URI provided + some storages tests refactoring

  If incorrect URIs provided to “–redis” and/or “–mongo” options tests should fail with errors instead of skipping.
  Otherwise the next scenario is possible:

  > 1. developer breaks RedisStorage and/or MongoStorage code
  > 2. tests are run with incorrect redis and/or mongo URIsprovided by “–redis” and “–mongo” options (for example, wrong port specified)
  > 3. tests pass because skipping doesn’t fail tests run
  > 4. developer or reviewer doesn’t notice that redis and/or mongo tests were skipped
  > 5. broken code gets in codebase

  Also some refactorings done (related with storages and storages tests).
  [#1510](https://github.com/aiogram/aiogram/issues/1510)

## 3.7.0 (2024-05-31)

### Features

- Added new storage `aiogram.fsm.storage.MongoStorage` for Finite State Machine based on Mongo DB (using `motor` library)
  [#1434](https://github.com/aiogram/aiogram/issues/1434)
- Added full support of [Bot API 7.4](https://core.telegram.org/bots/api-changelog#may-28-2024)
  [#1498](https://github.com/aiogram/aiogram/issues/1498)

### Bugfixes

- Fixed wrong `MarkdownV2` custom emoji parsing in `aiogram.utils.text_decorations`
  [#1496](https://github.com/aiogram/aiogram/issues/1496)

### Deprecations and Removals

- Removed deprecated arguments from Bot class
  `parse_mode`, `disable_web_page_preview`, `protect_content` as previously announced in v3.4.0.
  [#1494](https://github.com/aiogram/aiogram/issues/1494)

### Misc

- Improved code consistency and readability in code examples by refactoring imports, adjusting the base webhook URL, modifying bot instance initialization to utilize DefaultBotProperties, and updating router message handlers.
  [#1482](https://github.com/aiogram/aiogram/issues/1482)

## 3.6.0 (2024-05-06)

### Features

- Added full support of [Bot API 7.3](https://core.telegram.org/bots/api-changelog#may-6-2024)
  [#1480](https://github.com/aiogram/aiogram/issues/1480)

### Improved Documentation

- Added telegram objects transformation block in 2.x -> 3.x migration guide
  [#1412](https://github.com/aiogram/aiogram/issues/1412)

## 3.5.0 (2024-04-23)

### Features

- Added **message_thread_id** parameter to **ChatActionSender** class methods.
  [#1437](https://github.com/aiogram/aiogram/issues/1437)
- Added context manager interface to Bot instance, from now you can use:

  ```
  async with Bot(...) as bot:
      ...
  ```

  instead of

  ```
  async with Bot(...).context() as bot:
      ...
  ```

  [#1468](https://github.com/aiogram/aiogram/issues/1468)

### Bugfixes

- - **WebAppUser Class Fields**: Added missing is_premium, added_to_attachment_menu, and allows_write_to_pm fields to WebAppUser class to align with the Telegram API.
  - **WebAppChat Class Implementation**: Introduced the WebAppChat class with all its fields (id, type, title, username, and photo_url) as specified in the Telegram API, which was previously missing from the library.
  - **WebAppInitData Class Fields**: Included previously omitted fields in the WebAppInitData class: chat, chat_type, chat_instance, to match the official documentation for a complete Telegram Web Apps support.

  [#1424](https://github.com/aiogram/aiogram/issues/1424)
- Fixed poll answer FSM context by handling `voter_chat` for `poll_answer` event
  [#1436](https://github.com/aiogram/aiogram/issues/1436)
- Added missing error handling to `_background_feed_update` (when in `handle_in_background=True` webhook mode)
  [#1458](https://github.com/aiogram/aiogram/issues/1458)

### Improved Documentation

- Added WebAppChat class to WebApp docs, updated uk_UA localisation of WebApp docs.
  [#1433](https://github.com/aiogram/aiogram/issues/1433)

### Misc

- Added full support of [Bot API 7.2](https://core.telegram.org/bots/api-changelog#march-31-2024)
  [#1444](https://github.com/aiogram/aiogram/issues/1444)
- Loosened pydantic version upper restriction from `<2.7` to `<2.8`
  [#1460](https://github.com/aiogram/aiogram/issues/1460)

## 3.4.1 (2024-02-17)

### Bugfixes

- Fixed JSON serialization of the `LinkPreviewOptions` class while it is passed
  as bot-wide default options.
  [#1418](https://github.com/aiogram/aiogram/issues/1418)

## 3.4.0 (2024-02-16)

### Features

- Reworked bot-wide globals like `parse_mode`, `disable_web_page_preview`, and others to be more flexible.

  Warning

  Note that the old way of setting these global bot properties is now deprecated and will be removed in the next major release.

  [#1392](https://github.com/aiogram/aiogram/issues/1392)
- A new enum `KeyboardButtonPollTypeType` for `KeyboardButtonPollTypeType.type` field has bed added.
  [#1398](https://github.com/aiogram/aiogram/issues/1398)
- Added full support of [Bot API 7.1](https://core.telegram.org/bots/api-changelog#february-16-2024)

  - Added support for the administrator rights `can_post_stories`, `can_edit_stories`, `can_delete_stories` in supergroups.
  - Added the class `ChatBoostAdded` and the field `boost_added` to the class `Message` for service messages about a user boosting a chat.
  - Added the field `sender_boost_count` to the class `Message`.
  - Added the field `reply_to_story` to the class `Message`.
  - Added the fields `chat` and `id` to the class `Story`.
  - Added the field `unrestrict_boost_count` to the class `Chat`.
  - Added the field `custom_emoji_sticker_set_name` to the class `Chat`.

  [#1417](https://github.com/aiogram/aiogram/issues/1417)

### Bugfixes

- Update KeyboardBuilder utility, fixed type-hints for button method, adjusted limits of the different markup types to real world values.
  [#1399](https://github.com/aiogram/aiogram/issues/1399)
- Added new `reply_parameters` param to `message.send_copy` because it hasn’t been added there
  [#1403](https://github.com/aiogram/aiogram/issues/1403)

### Improved Documentation

- Add notion “Working with plural forms” in documentation Utils -> Translation
  [#1395](https://github.com/aiogram/aiogram/issues/1395)

## 3.3.0 (2023-12-31)

### Features

- Added full support of [Bot API 7.0](https://core.telegram.org/bots/api-changelog#december-29-2023)

  - Reactions
  - Replies 2.0
  - Link Preview Customization
  - Block Quotation
  - Multiple Message Actions
  - Requests for multiple users
  - Chat Boosts
  - Giveaway
  - Other changes

  [#1387](https://github.com/aiogram/aiogram/issues/1387)

## 3.2.0 (2023-11-24)

### Features

- Introduced Scenes feature that helps you to simplify user interactions using Finite State Machine.
  Read more about 👉 [Scenes](dispatcher/finite_state_machine/scene.html#scenes).
  [#1280](https://github.com/aiogram/aiogram/issues/1280)
- Added the new FSM strategy `CHAT_TOPIC`, which sets the state for the entire topic in the chat, also works in private messages and regular groups without topics.
  [#1343](https://github.com/aiogram/aiogram/issues/1343)

### Bugfixes

- Fixed `parse_mode` argument in the in `Message.send_copy` shortcut. Disable by default.
  [#1332](https://github.com/aiogram/aiogram/issues/1332)
- Added ability to get handler flags from filters.
  [#1360](https://github.com/aiogram/aiogram/issues/1360)
- Fixed a situation where a `CallbackData` could not be parsed without a default value.
  [#1368](https://github.com/aiogram/aiogram/issues/1368)

### Improved Documentation

- Corrected grammatical errors, improved sentence structures, translation for migration 2.x-3.x
  [#1302](https://github.com/aiogram/aiogram/issues/1302)
- Minor typo correction, specifically in module naming + some grammar.
  [#1340](https://github.com/aiogram/aiogram/issues/1340)
- Added CITATION.cff file for automatic academic citation generation.
  Now you can copy citation from the GitHub page and paste it into your paper.
  [#1351](https://github.com/aiogram/aiogram/issues/1351)
- Minor typo correction in middleware docs.
  [#1353](https://github.com/aiogram/aiogram/issues/1353)

### Misc

- Fixed ResourceWarning in the tests, reworked `RedisEventsIsolation` fixture to use Redis connection from `RedisStorage`
  [#1320](https://github.com/aiogram/aiogram/issues/1320)
- Updated dependencies, bumped minimum required version:

  - `magic-filter` - fixed .resolve operation
  - `pydantic` - fixed compatibility (broken in 2.4)
  - `aiodns` - added new dependency to the `fast` extras (`pip install aiogram[fast]`)
  - *others…*

  [#1327](https://github.com/aiogram/aiogram/issues/1327)
- Prevent update handling task pointers from being garbage collected, backport from 2.x
  [#1331](https://github.com/aiogram/aiogram/issues/1331)
- Updated `typing-extensions` package version range in dependencies to fix compatibility with `FastAPI`
  [#1347](https://github.com/aiogram/aiogram/issues/1347)
- Introduce Python 3.12 support
  [#1354](https://github.com/aiogram/aiogram/issues/1354)
- Speeded up CallableMixin processing by caching references to nested objects and simplifying kwargs assembly.
  [#1357](https://github.com/aiogram/aiogram/issues/1357)
- Added `pydantic` v2.5 support.
  [#1361](https://github.com/aiogram/aiogram/issues/1361)
- Updated `thumbnail` fields type to `InputFile` only
  [#1372](https://github.com/aiogram/aiogram/issues/1372)

## 3.1.1 (2023-09-25)

### Bugfixes

- Fixed pydantic version <2.4, since 2.4 has breaking changes.
  [#1322](https://github.com/aiogram/aiogram/issues/1322)

## 3.1.0 (2023-09-22)

### Features

- Added support for custom encoders/decoders for payload (and also for deep-linking).
  [#1262](https://github.com/aiogram/aiogram/issues/1262)
- Added `aiogram.utils.input_media.MediaGroupBuilder` for media group construction.
  [#1293](https://github.com/aiogram/aiogram/issues/1293)
- Added full support of [Bot API 6.9](https://core.telegram.org/bots/api-changelog#september-22-2023)
  [#1319](https://github.com/aiogram/aiogram/issues/1319)

### Bugfixes

- Added actual param hints for InlineKeyboardBuilder and ReplyKeyboardBuilder.
  [#1303](https://github.com/aiogram/aiogram/issues/1303)
- Fixed priority of events isolation, now user state will be loaded only after lock is acquired
  [#1317](https://github.com/aiogram/aiogram/issues/1317)

## 3.0.0 (2023-09-01)

### Bugfixes

- Replaced `datetime.datetime` with DateTime type wrapper across types to make dumped JSONs object
  more compatible with data that is sent by Telegram.
  [#1277](https://github.com/aiogram/aiogram/issues/1277)
- Fixed magic `.as_(...)` operation for values that can be interpreted as False (e.g. 0).
  [#1281](https://github.com/aiogram/aiogram/issues/1281)
- Italic markdown from utils now uses correct decorators
  [#1282](https://github.com/aiogram/aiogram/issues/1282)
- Fixed method `Message.send_copy` for stickers.
  [#1284](https://github.com/aiogram/aiogram/issues/1284)
- Fixed `Message.send_copy` method, which was not working properly with stories, so not you can copy stories too (forwards messages).
  [#1286](https://github.com/aiogram/aiogram/issues/1286)
- Fixed error overlapping when validation error is caused by remove_unset root validator in base types and methods.
  [#1290](https://github.com/aiogram/aiogram/issues/1290)

## 3.0.0rc2 (2023-08-18)

### Bugfixes

- Fixed missing message content types (`ContentType.USER_SHARED`, `ContentType.CHAT_SHARED`)
  [#1252](https://github.com/aiogram/aiogram/issues/1252)
- Fixed nested hashtag, cashtag and email message entities not being parsed correctly when these entities are inside another entity.
  [#1259](https://github.com/aiogram/aiogram/issues/1259)
- Moved global filters check placement into router to add chance to pass context from global filters
  into handlers in the same way as it possible in other places
  [#1266](https://github.com/aiogram/aiogram/issues/1266)

### Improved Documentation

- Added error handling example examples/error_handling.py
  [#1099](https://github.com/aiogram/aiogram/issues/1099)
- Added a few words about skipping pending updates
  [#1251](https://github.com/aiogram/aiogram/issues/1251)
- Added a section on Dependency Injection technology
  [#1253](https://github.com/aiogram/aiogram/issues/1253)
- This update includes the addition of a multi-file bot example to the repository.
  [#1254](https://github.com/aiogram/aiogram/issues/1254)
- Refactored examples code to use aiogram enumerations and enhanced chat messages with markdown
  beautification’s for a more user-friendly display.
  [#1256](https://github.com/aiogram/aiogram/issues/1256)
- Supplemented “Finite State Machine” section in Migration FAQ
  [#1264](https://github.com/aiogram/aiogram/issues/1264)
- Removed extra param in docstring of TelegramEventObserver’s filter method
  and fixed typo in I18n documentation.
  [#1268](https://github.com/aiogram/aiogram/issues/1268)

### Misc

- Enhanced the warning message in dispatcher to include a JSON dump of the update when update type is not known.
  [#1269](https://github.com/aiogram/aiogram/issues/1269)
- Added support for [Bot API 6.8](https://core.telegram.org/bots/api-changelog#august-18-2023)
  [#1275](https://github.com/aiogram/aiogram/issues/1275)

## 3.0.0rc1 (2023-08-06)

### Features

- Added Currency enum.
  You can use it like this:

  ```
  from aiogram.enums import Currency

  await bot.send_invoice(
      ...,
      currency=Currency.USD,
      ...
  )
  ```

  [#1194](https://github.com/aiogram/aiogram/issues/1194)
- Updated keyboard builders with new methods for integrating buttons and keyboard creation more seamlessly.
  Added functionality to create buttons from existing markup and attach another builder.
  This improvement aims to make the keyboard building process more user-friendly and flexible.
  [#1236](https://github.com/aiogram/aiogram/issues/1236)
- Added support for message_thread_id in ChatActionSender
  [#1249](https://github.com/aiogram/aiogram/issues/1249)

### Bugfixes

- Fixed polling startup when “bot” key is passed manually into dispatcher workflow data
  [#1242](https://github.com/aiogram/aiogram/issues/1242)
- Added codegen configuration for lost shortcuts:

  - ShippingQuery.answer
  - PreCheckoutQuery.answer
  - Message.delete_reply_markup

  [#1244](https://github.com/aiogram/aiogram/issues/1244)

### Improved Documentation

- Added documentation for webhook and polling modes.
  [#1241](https://github.com/aiogram/aiogram/issues/1241)

### Misc

- Reworked InputFile reading, removed `__aiter__` method, added bot: Bot argument to
  the `.read(...)` method, so, from now URLInputFile can be used without specifying
  bot instance.
  [#1238](https://github.com/aiogram/aiogram/issues/1238)
- Code-generated `__init__` typehints in types and methods to make IDE happy without additional pydantic plugin
  [#1245](https://github.com/aiogram/aiogram/issues/1245)

## 3.0.0b9 (2023-07-30)

### Features

- Added new shortcuts for [`aiogram.types.chat_member_updated.ChatMemberUpdated`](api/types/chat_member_updated.html#aiogram.types.chat_member_updated.ChatMemberUpdated "aiogram.types.chat_member_updated.ChatMemberUpdated")
  to send message to chat that member joined/left.
  [#1234](https://github.com/aiogram/aiogram/issues/1234)
- Added new shortcuts for [`aiogram.types.chat_join_request.ChatJoinRequest`](api/types/chat_join_request.html#aiogram.types.chat_join_request.ChatJoinRequest "aiogram.types.chat_join_request.ChatJoinRequest")
  to make easier access to sending messages to users who wants to join to chat.
  [#1235](https://github.com/aiogram/aiogram/issues/1235)

### Bugfixes

- Fixed bot assignment in the `Message.send_copy` shortcut
  [#1232](https://github.com/aiogram/aiogram/issues/1232)
- Added model validation to remove UNSET before field validation.
  This change was necessary to correctly handle parse_mode where ‘UNSET’ is used as a sentinel value.
  Without the removal of ‘UNSET’, it would create issues when passed to model initialization from Bot.method_name.
  ‘UNSET’ was also added to typing.
  [#1233](https://github.com/aiogram/aiogram/issues/1233)
- Updated pydantic to 2.1 with few bugfixes

### Improved Documentation

- Improved docs, added basic migration guide (will be expanded later)
  [#1143](https://github.com/aiogram/aiogram/issues/1143)

### Deprecations and Removals

- Removed the use of the context instance (Bot.get_current) from all placements that were used previously.
  This is to avoid the use of the context instance in the wrong place.
  [#1230](https://github.com/aiogram/aiogram/issues/1230)

## 3.0.0b8 (2023-07-17)

### Features

- Added possibility to use custom events in routers (If router does not support custom event it does not break and passes it to included routers).
  [#1147](https://github.com/aiogram/aiogram/issues/1147)
- Added support for FSM in Forum topics.

  The strategy can be changed in dispatcher:

  ```
  from aiogram.fsm.strategy import FSMStrategy
  ...
  dispatcher = Dispatcher(
      fsm_strategy=FSMStrategy.USER_IN_TOPIC,
      storage=...,  # Any persistent storage
  )
  ```

  Note

  If you have implemented you own storages you should extend record key generation
  with new one attribute - `thread_id`

  [#1161](https://github.com/aiogram/aiogram/issues/1161)
- Improved CallbackData serialization.

  - Minimized UUID (hex without dashes)
  - Replaced bool values with int (true=1, false=0)

  [#1163](https://github.com/aiogram/aiogram/issues/1163)
- Added a tool to make text formatting flexible and easy.
  More details on the [corresponding documentation page](utils/formatting.html#formatting-tool)
  [#1172](https://github.com/aiogram/aiogram/issues/1172)
- Added `X-Telegram-Bot-Api-Secret-Token` header check
  [#1173](https://github.com/aiogram/aiogram/issues/1173)
- Made `allowed_updates` list to revolve automatically in start_polling method if not set explicitly.
  [#1178](https://github.com/aiogram/aiogram/issues/1178)
- Added possibility to pass custom headers to `URLInputFile` object
  [#1191](https://github.com/aiogram/aiogram/issues/1191)

### Bugfixes

- Change type of result in InlineQueryResult enum for `InlineQueryResultCachedMpeg4Gif`
  and `InlineQueryResultMpeg4Gif` to more correct according to documentation.

  Change regexp for entities parsing to more correct (`InlineQueryResultType.yml`).
  [#1146](https://github.com/aiogram/aiogram/issues/1146)
- Fixed signature of startup/shutdown events to include the `**dispatcher.workflow_data` as the handler arguments.
  [#1155](https://github.com/aiogram/aiogram/issues/1155)
- Added missing `FORUM_TOPIC_EDITED` value to content_type property
  [#1160](https://github.com/aiogram/aiogram/issues/1160)
- Fixed compatibility with Python 3.8-3.9 (from previous release)
  [#1162](https://github.com/aiogram/aiogram/issues/1162)
- Fixed the markdown spoiler parser.
  [#1176](https://github.com/aiogram/aiogram/issues/1176)
- Fixed workflow data propagation
  [#1196](https://github.com/aiogram/aiogram/issues/1196)
- Fixed the serialization error associated with nested subtypes
  like InputMedia, ChatMember, etc.

  The previously generated code resulted in an invalid schema under pydantic v2,
  which has stricter type parsing.
  Hence, subtypes without the specification of all subtype unions were generating
  an empty object. This has been rectified now.
  [#1213](https://github.com/aiogram/aiogram/issues/1213)

### Improved Documentation

- Changed small grammar typos for `upload_file`
  [#1133](https://github.com/aiogram/aiogram/issues/1133)

### Deprecations and Removals

- Removed text filter in due to is planned to remove this filter few versions ago.

  Use `F.text` instead
  [#1170](https://github.com/aiogram/aiogram/issues/1170)

### Misc

- Added full support of [Bot API 6.6](https://core.telegram.org/bots/api-changelog#march-9-2023)

  Danger

  Note that this issue has breaking changes described in the Bot API changelog,
  this changes is not breaking in the API but breaking inside aiogram because
  Beta stage is not finished.

  [#1139](https://github.com/aiogram/aiogram/issues/1139)
- Added full support of [Bot API 6.7](https://core.telegram.org/bots/api-changelog#april-21-2023)

  Warning

  Note that arguments *switch_pm_parameter* and *switch_pm_text* was deprecated
  and should be changed to *button* argument as described in API docs.

  [#1168](https://github.com/aiogram/aiogram/issues/1168)
- Updated [Pydantic to V2](https://docs.pydantic.dev/2.0/migration/)

  Warning

  Be careful, not all libraries is already updated to using V2

  [#1202](https://github.com/aiogram/aiogram/issues/1202)
- Added global defaults `disable_web_page_preview` and `protect_content` in addition to `parse_mode` to the Bot instance,
  reworked internal request builder mechanism.
  [#1142](https://github.com/aiogram/aiogram/issues/1142)
- Removed bot parameters from storages
  [#1144](https://github.com/aiogram/aiogram/issues/1144)
- Replaced ContextVar’s with a new feature called [Validation Context](https://docs.pydantic.dev/latest/usage/validators/#validation-context)
  in Pydantic to improve the clarity, usability, and versatility of handling the Bot instance within method shortcuts.

  Danger

  **Breaking**: The ‘bot’ argument now is required in URLInputFile

  [#1210](https://github.com/aiogram/aiogram/issues/1210)
- Updated magic-filter with new features

  - Added hint for `len(F)` error
  - Added not in operation

  [#1221](https://github.com/aiogram/aiogram/issues/1221)

## 3.0.0b7 (2023-02-18)

Warning

Note that this version has incompatibility with Python 3.8-3.9 in case when you create an instance of Dispatcher outside of the any coroutine.

Sorry for the inconvenience, it will be fixed in the next version.

This code will not work:

```
dp = Dispatcher()

def main():
    ...
    dp.run_polling(...)

main()
```

But if you change it like this it should works as well:

```
router = Router()

async def main():
    dp = Dispatcher()
    dp.include_router(router)
    ...
    dp.start_polling(...)

asyncio.run(main())
```

### Features

- Added missing shortcuts, new enums, reworked old stuff

  **Breaking**
  All previously added enums is re-generated in new place - aiogram.enums instead of aiogram.types

  **Added enums:** [`aiogram.enums.bot_command_scope_type.BotCommandScopeType`](api/enums/bot_command_scope_type.html#aiogram.enums.bot_command_scope_type.BotCommandScopeType "aiogram.enums.bot_command_scope_type.BotCommandScopeType"),
  :   [`aiogram.enums.chat_action.ChatAction`](api/enums/chat_action.html#aiogram.enums.chat_action.ChatAction "aiogram.enums.chat_action.ChatAction"),
      [`aiogram.enums.chat_member_status.ChatMemberStatus`](api/enums/chat_member_status.html#aiogram.enums.chat_member_status.ChatMemberStatus "aiogram.enums.chat_member_status.ChatMemberStatus"),
      [`aiogram.enums.chat_type.ChatType`](api/enums/chat_type.html#aiogram.enums.chat_type.ChatType "aiogram.enums.chat_type.ChatType"),
      [`aiogram.enums.content_type.ContentType`](api/enums/content_type.html#aiogram.enums.content_type.ContentType "aiogram.enums.content_type.ContentType"),
      [`aiogram.enums.dice_emoji.DiceEmoji`](api/enums/dice_emoji.html#aiogram.enums.dice_emoji.DiceEmoji "aiogram.enums.dice_emoji.DiceEmoji"),
      [`aiogram.enums.inline_query_result_type.InlineQueryResultType`](api/enums/inline_query_result_type.html#aiogram.enums.inline_query_result_type.InlineQueryResultType "aiogram.enums.inline_query_result_type.InlineQueryResultType"),
      [`aiogram.enums.input_media_type.InputMediaType`](api/enums/input_media_type.html#aiogram.enums.input_media_type.InputMediaType "aiogram.enums.input_media_type.InputMediaType"),
      [`aiogram.enums.mask_position_point.MaskPositionPoint`](api/enums/mask_position_point.html#aiogram.enums.mask_position_point.MaskPositionPoint "aiogram.enums.mask_position_point.MaskPositionPoint"),
      [`aiogram.enums.menu_button_type.MenuButtonType`](api/enums/menu_button_type.html#aiogram.enums.menu_button_type.MenuButtonType "aiogram.enums.menu_button_type.MenuButtonType"),
      [`aiogram.enums.message_entity_type.MessageEntityType`](api/enums/message_entity_type.html#aiogram.enums.message_entity_type.MessageEntityType "aiogram.enums.message_entity_type.MessageEntityType"),
      [`aiogram.enums.parse_mode.ParseMode`](api/enums/parse_mode.html#aiogram.enums.parse_mode.ParseMode "aiogram.enums.parse_mode.ParseMode"),
      [`aiogram.enums.poll_type.PollType`](api/enums/poll_type.html#aiogram.enums.poll_type.PollType "aiogram.enums.poll_type.PollType"),
      [`aiogram.enums.sticker_type.StickerType`](api/enums/sticker_type.html#aiogram.enums.sticker_type.StickerType "aiogram.enums.sticker_type.StickerType"),
      [`aiogram.enums.topic_icon_color.TopicIconColor`](api/enums/topic_icon_color.html#aiogram.enums.topic_icon_color.TopicIconColor "aiogram.enums.topic_icon_color.TopicIconColor"),
      [`aiogram.enums.update_type.UpdateType`](api/enums/update_type.html#aiogram.enums.update_type.UpdateType "aiogram.enums.update_type.UpdateType"),

  **Added shortcuts**:

  - *Chat* [`aiogram.types.chat.Chat.get_administrators()`](api/types/chat.html#aiogram.types.chat.Chat.get_administrators "aiogram.types.chat.Chat.get_administrators"),
    :   [`aiogram.types.chat.Chat.delete_message()`](api/types/chat.html#aiogram.types.chat.Chat.delete_message "aiogram.types.chat.Chat.delete_message"),
        [`aiogram.types.chat.Chat.revoke_invite_link()`](api/types/chat.html#aiogram.types.chat.Chat.revoke_invite_link "aiogram.types.chat.Chat.revoke_invite_link"),
        [`aiogram.types.chat.Chat.edit_invite_link()`](api/types/chat.html#aiogram.types.chat.Chat.edit_invite_link "aiogram.types.chat.Chat.edit_invite_link"),
        [`aiogram.types.chat.Chat.create_invite_link()`](api/types/chat.html#aiogram.types.chat.Chat.create_invite_link "aiogram.types.chat.Chat.create_invite_link"),
        [`aiogram.types.chat.Chat.export_invite_link()`](api/types/chat.html#aiogram.types.chat.Chat.export_invite_link "aiogram.types.chat.Chat.export_invite_link"),
        [`aiogram.types.chat.Chat.do()`](api/types/chat.html#aiogram.types.chat.Chat.do "aiogram.types.chat.Chat.do"),
        [`aiogram.types.chat.Chat.delete_sticker_set()`](api/types/chat.html#aiogram.types.chat.Chat.delete_sticker_set "aiogram.types.chat.Chat.delete_sticker_set"),
        [`aiogram.types.chat.Chat.set_sticker_set()`](api/types/chat.html#aiogram.types.chat.Chat.set_sticker_set "aiogram.types.chat.Chat.set_sticker_set"),
        [`aiogram.types.chat.Chat.get_member()`](api/types/chat.html#aiogram.types.chat.Chat.get_member "aiogram.types.chat.Chat.get_member"),
        [`aiogram.types.chat.Chat.get_member_count()`](api/types/chat.html#aiogram.types.chat.Chat.get_member_count "aiogram.types.chat.Chat.get_member_count"),
        [`aiogram.types.chat.Chat.leave()`](api/types/chat.html#aiogram.types.chat.Chat.leave "aiogram.types.chat.Chat.leave"),
        [`aiogram.types.chat.Chat.unpin_all_messages()`](api/types/chat.html#aiogram.types.chat.Chat.unpin_all_messages "aiogram.types.chat.Chat.unpin_all_messages"),
        [`aiogram.types.chat.Chat.unpin_message()`](api/types/chat.html#aiogram.types.chat.Chat.unpin_message "aiogram.types.chat.Chat.unpin_message"),
        [`aiogram.types.chat.Chat.pin_message()`](api/types/chat.html#aiogram.types.chat.Chat.pin_message "aiogram.types.chat.Chat.pin_message"),
        [`aiogram.types.chat.Chat.set_administrator_custom_title()`](api/types/chat.html#aiogram.types.chat.Chat.set_administrator_custom_title "aiogram.types.chat.Chat.set_administrator_custom_title"),
        [`aiogram.types.chat.Chat.set_permissions()`](api/types/chat.html#aiogram.types.chat.Chat.set_permissions "aiogram.types.chat.Chat.set_permissions"),
        [`aiogram.types.chat.Chat.promote()`](api/types/chat.html#aiogram.types.chat.Chat.promote "aiogram.types.chat.Chat.promote"),
        [`aiogram.types.chat.Chat.restrict()`](api/types/chat.html#aiogram.types.chat.Chat.restrict "aiogram.types.chat.Chat.restrict"),
        [`aiogram.types.chat.Chat.unban()`](api/types/chat.html#aiogram.types.chat.Chat.unban "aiogram.types.chat.Chat.unban"),
        [`aiogram.types.chat.Chat.ban()`](api/types/chat.html#aiogram.types.chat.Chat.ban "aiogram.types.chat.Chat.ban"),
        [`aiogram.types.chat.Chat.set_description()`](api/types/chat.html#aiogram.types.chat.Chat.set_description "aiogram.types.chat.Chat.set_description"),
        [`aiogram.types.chat.Chat.set_title()`](api/types/chat.html#aiogram.types.chat.Chat.set_title "aiogram.types.chat.Chat.set_title"),
        [`aiogram.types.chat.Chat.delete_photo()`](api/types/chat.html#aiogram.types.chat.Chat.delete_photo "aiogram.types.chat.Chat.delete_photo"),
        [`aiogram.types.chat.Chat.set_photo()`](api/types/chat.html#aiogram.types.chat.Chat.set_photo "aiogram.types.chat.Chat.set_photo"),
  - *Sticker*: [`aiogram.types.sticker.Sticker.set_position_in_set()`](api/types/sticker.html#aiogram.types.sticker.Sticker.set_position_in_set "aiogram.types.sticker.Sticker.set_position_in_set"),
    :   [`aiogram.types.sticker.Sticker.delete_from_set()`](api/types/sticker.html#aiogram.types.sticker.Sticker.delete_from_set "aiogram.types.sticker.Sticker.delete_from_set"),
  - *User*: [`aiogram.types.user.User.get_profile_photos()`](api/types/user.html#aiogram.types.user.User.get_profile_photos "aiogram.types.user.User.get_profile_photos")

  [#952](https://github.com/aiogram/aiogram/issues/952)
- Added [callback answer](utils/callback_answer.html#callback-answer-util) feature
  [#1091](https://github.com/aiogram/aiogram/issues/1091)
- Added a method that allows you to compactly register routers
  [#1117](https://github.com/aiogram/aiogram/issues/1117)

### Bugfixes

- Check status code when downloading file
  [#816](https://github.com/aiogram/aiogram/issues/816)
- Fixed ignore_case parameter in [`aiogram.filters.command.Command`](dispatcher/filters/command.html#aiogram.filters.command.Command "aiogram.filters.command.Command") filter
  [#1106](https://github.com/aiogram/aiogram/issues/1106)

### Misc

- Added integration with new code-generator named [Butcher](https://github.com/aiogram/butcher)
  [#1069](https://github.com/aiogram/aiogram/issues/1069)
- Added full support of [Bot API 6.4](https://core.telegram.org/bots/api-changelog#december-30-2022)
  [#1088](https://github.com/aiogram/aiogram/issues/1088)
- Updated package metadata, moved build internals from Poetry to Hatch, added contributing guides.
  [#1095](https://github.com/aiogram/aiogram/issues/1095)
- Added full support of [Bot API 6.5](https://core.telegram.org/bots/api-changelog#february-3-2023)

  Danger

  Note that [`aiogram.types.chat_permissions.ChatPermissions`](api/types/chat_permissions.html#aiogram.types.chat_permissions.ChatPermissions "aiogram.types.chat_permissions.ChatPermissions") is updated without
  backward compatibility, so now this object has no `can_send_media_messages` attribute

  [#1112](https://github.com/aiogram/aiogram/issues/1112)
- Replaced error `TypeError: TelegramEventObserver.__call__() got an unexpected keyword argument '<name>'`
  with a more understandable one for developers and with a link to the documentation.
  [#1114](https://github.com/aiogram/aiogram/issues/1114)
- Added possibility to reply into webhook with files
  [#1120](https://github.com/aiogram/aiogram/issues/1120)
- Reworked graceful shutdown. Added method to stop polling.
  Now polling started from dispatcher can be stopped by signals gracefully without errors (on Linux and Mac).
  [#1124](https://github.com/aiogram/aiogram/issues/1124)

## 3.0.0b6 (2022-11-18)

### Features

- (again) Added possibility to combine filters with an *and*/*or* operations.

  Read more in “[Combining filters](dispatcher/filters/index.html#combining-filters)” documentation section
  [#1018](https://github.com/aiogram/aiogram/issues/1018)
- Added following methods to `Message` class:

  - `Message.forward(...)`
  - `Message.edit_media(...)`
  - `Message.edit_live_location(...)`
  - `Message.stop_live_location(...)`
  - `Message.pin(...)`
  - `Message.unpin()`

  [#1030](https://github.com/aiogram/aiogram/issues/1030)
- Added following methods to `User` class:

  - `User.mention_markdown(...)`
  - `User.mention_html(...)`

  [#1049](https://github.com/aiogram/aiogram/issues/1049)
- Added full support of [Bot API 6.3](https://core.telegram.org/bots/api-changelog#november-5-2022)
  [#1057](https://github.com/aiogram/aiogram/issues/1057)

### Bugfixes

- Fixed `Message.send_invoice` and `Message.reply_invoice`, added missing arguments
  [#1047](https://github.com/aiogram/aiogram/issues/1047)
- Fixed copy and forward in:

  - `Message.answer(...)`
  - `Message.copy_to(...)`

  [#1064](https://github.com/aiogram/aiogram/issues/1064)

### Improved Documentation

- Fixed UA translations in index.po
  [#1017](https://github.com/aiogram/aiogram/issues/1017)
- Fix typehints for `Message`, `reply_media_group` and `answer_media_group` methods
  [#1029](https://github.com/aiogram/aiogram/issues/1029)
- Removed an old now non-working feature
  [#1060](https://github.com/aiogram/aiogram/issues/1060)

### Misc

- Enabled testing on Python 3.11
  [#1044](https://github.com/aiogram/aiogram/issues/1044)
- Added a mandatory dependency `certifi` in due to in some cases on systems that doesn’t have updated ca-certificates the requests to Bot API fails with reason `[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain`
  [#1066](https://github.com/aiogram/aiogram/issues/1066)

## 3.0.0b5 (2022-10-02)

### Features

- Add PyPy support and run tests under PyPy
  [#985](https://github.com/aiogram/aiogram/issues/985)
- Added message text to aiogram exceptions representation
  [#988](https://github.com/aiogram/aiogram/issues/988)
- Added warning about using magic filter from magic_filter instead of aiogram’s ones.
  Is recommended to use from aiogram import F instead of from magic_filter import F
  [#990](https://github.com/aiogram/aiogram/issues/990)
- Added more detailed error when server response can’t be deserialized. This feature will help to debug unexpected responses from the Server
  [#1014](https://github.com/aiogram/aiogram/issues/1014)

### Bugfixes

- Reworked error event, introduced [`aiogram.types.error_event.ErrorEvent`](dispatcher/errors.html#aiogram.types.error_event.ErrorEvent "aiogram.types.error_event.ErrorEvent") object.
  [#898](https://github.com/aiogram/aiogram/issues/898)
- Fixed escaping markdown in aiogram.utils.markdown module
  [#903](https://github.com/aiogram/aiogram/issues/903)
- Fixed polling crash when Telegram Bot API raises HTTP 429 status-code.
  [#995](https://github.com/aiogram/aiogram/issues/995)
- Fixed empty mention in command parsing, now it will be None instead of an empty string
  [#1013](https://github.com/aiogram/aiogram/issues/1013)

### Improved Documentation

- Initialized Docs translation (added Ukrainian language)
  [#925](https://github.com/aiogram/aiogram/issues/925)

### Deprecations and Removals

- Removed filters factory as described in corresponding issue.
  [#942](https://github.com/aiogram/aiogram/issues/942)

### Misc

- Now Router/Dispatcher accepts only keyword arguments.
  [#982](https://github.com/aiogram/aiogram/issues/982)

## 3.0.0b4 (2022-08-14)

### Features

- Add class helper ChatAction for constants that Telegram BotAPI uses in sendChatAction request.
  In my opinion, this will help users and will also improve compatibility with 2.x version
  where similar class was called “ChatActions”.
  [#803](https://github.com/aiogram/aiogram/issues/803)
- Added possibility to combine filters or invert result

  Example:

  ```
  Text(text="demo") | Command(commands=["demo"])
  MyFilter() & AnotherFilter()
  ~StateFilter(state='my-state')
  ```

  [#894](https://github.com/aiogram/aiogram/issues/894)
- Fixed type hints for redis TTL params.
  [#922](https://github.com/aiogram/aiogram/issues/922)
- Added full_name shortcut for Chat object
  [#929](https://github.com/aiogram/aiogram/issues/929)

### Bugfixes

- Fixed false-positive coercing of Union types in API methods
  [#901](https://github.com/aiogram/aiogram/issues/901)
- Added 3 missing content types:

  - proximity_alert_triggered
  - supergroup_chat_created
  - channel_chat_created

  [#906](https://github.com/aiogram/aiogram/issues/906)
- Fixed the ability to compare the state, now comparison to copy of the state will return True.
  [#927](https://github.com/aiogram/aiogram/issues/927)
- Fixed default lock kwargs in RedisEventIsolation.
  [#972](https://github.com/aiogram/aiogram/issues/972)

### Misc

- Restrict including routers with strings
  [#896](https://github.com/aiogram/aiogram/issues/896)
- Changed CommandPatterType to CommandPatternType in aiogram/dispatcher/filters/command.py
  [#907](https://github.com/aiogram/aiogram/issues/907)
- Added full support of [Bot API 6.1](https://core.telegram.org/bots/api-changelog#june-20-2022)
  [#936](https://github.com/aiogram/aiogram/issues/936)
- **Breaking!** More flat project structure

  These packages was moved, imports in your code should be fixed:

  - `aiogram.dispatcher.filters` -> `aiogram.filters`
  - `aiogram.dispatcher.fsm` -> `aiogram.fsm`
  - `aiogram.dispatcher.handler` -> `aiogram.handler`
  - `aiogram.dispatcher.webhook` -> `aiogram.webhook`
  - `aiogram.dispatcher.flags/*` -> `aiogram.dispatcher.flags` (single module instead of package)

  [#938](https://github.com/aiogram/aiogram/issues/938)
- Removed deprecated `router.<event>_handler` and `router.register_<event>_handler` methods.
  [#941](https://github.com/aiogram/aiogram/issues/941)
- Deprecated filters factory. It will be removed in next Beta (3.0b5)
  [#942](https://github.com/aiogram/aiogram/issues/942)
- MessageEntity method get_text was removed and extract was renamed to extract_from
  [#944](https://github.com/aiogram/aiogram/issues/944)
- Added full support of [Bot API 6.2](https://core.telegram.org/bots/api-changelog#august-12-2022)
  [#975](https://github.com/aiogram/aiogram/issues/975)

## 3.0.0b3 (2022-04-19)

### Features

- Added possibility to get command magic result as handler argument
  [#889](https://github.com/aiogram/aiogram/issues/889)
- Added full support of [Telegram Bot API 6.0](https://core.telegram.org/bots/api-changelog#april-16-2022)
  [#890](https://github.com/aiogram/aiogram/issues/890)

### Bugfixes

- Fixed I18n lazy-proxy. Disabled caching.
  [#839](https://github.com/aiogram/aiogram/issues/839)
- Added parsing of spoiler message entity
  [#865](https://github.com/aiogram/aiogram/issues/865)
- Fixed default parse_mode for Message.copy_to() method.
  [#876](https://github.com/aiogram/aiogram/issues/876)
- Fixed CallbackData factory parsing IntEnum’s
  [#885](https://github.com/aiogram/aiogram/issues/885)

### Misc

- Added automated check that pull-request adds a changes description to **CHANGES** directory
  [#873](https://github.com/aiogram/aiogram/issues/873)
- Changed `Message.html_text` and `Message.md_text` attributes behaviour when message has no text.
  The empty string will be used instead of raising error.
  [#874](https://github.com/aiogram/aiogram/issues/874)
- Used redis-py instead of aioredis package in due to this packages was merged into single one
  [#882](https://github.com/aiogram/aiogram/issues/882)
- Solved common naming problem with middlewares that confusing too much developers
  - now you can’t see the middleware and middlewares attributes at the same point
  because this functionality encapsulated to special interface.
  [#883](https://github.com/aiogram/aiogram/issues/883)

## 3.0.0b2 (2022-02-19)

### Features

- Added possibility to pass additional arguments into the aiohttp webhook handler to use this
  arguments inside handlers as the same as it possible in polling mode.
  [#785](https://github.com/aiogram/aiogram/issues/785)
- Added possibility to add handler flags via decorator (like pytest.mark decorator but aiogram.flags)
  [#836](https://github.com/aiogram/aiogram/issues/836)
- Added `ChatActionSender` utility to automatically sends chat action while long process is running.

  It also can be used as message middleware and can be customized via `chat_action` flag.
  [#837](https://github.com/aiogram/aiogram/issues/837)

### Bugfixes

- Fixed unexpected behavior of sequences in the StateFilter.
  [#791](https://github.com/aiogram/aiogram/issues/791)
- Fixed exceptions filters
  [#827](https://github.com/aiogram/aiogram/issues/827)

### Misc

- Logger name for processing events is changed to `aiogram.events`.
  [#830](https://github.com/aiogram/aiogram/issues/830)
- Added full support of Telegram Bot API 5.6 and 5.7
  [#835](https://github.com/aiogram/aiogram/issues/835)
- **BREAKING**
  Events isolation mechanism is moved from FSM storages to standalone managers
  [#838](https://github.com/aiogram/aiogram/issues/838)

## 3.0.0b1 (2021-12-12)

### Features

- Added new custom operation for MagicFilter named `as_`

  Now you can use it to get magic filter result as handler argument

  ```
  from aiogram import F

  ...

  @router.message(F.text.regexp(r"^(\d+)$").as_("digits"))
  async def any_digits_handler(message: Message, digits: Match[str]):
      await message.answer(html.quote(str(digits)))

  @router.message(F.photo[-1].as_("photo"))
  async def download_photos_handler(message: Message, photo: PhotoSize, bot: Bot):
      content = await bot.download(photo)
  ```

  [#759](https://github.com/aiogram/aiogram/issues/759)

### Bugfixes

- Fixed: Missing `ChatMemberHandler` import in `aiogram/dispatcher/handler`
  [#751](https://github.com/aiogram/aiogram/issues/751)

### Misc

- Check `destiny` in case of no `with_destiny` enabled in RedisStorage key builder
  [#776](https://github.com/aiogram/aiogram/issues/776)
- Added full support of [Bot API 5.5](https://core.telegram.org/bots/api-changelog#december-7-2021)
  [#777](https://github.com/aiogram/aiogram/issues/777)
- Stop using feature from #336. From now settings of client-session should be placed as initializer arguments instead of changing instance attributes.
  [#778](https://github.com/aiogram/aiogram/issues/778)
- Make TelegramAPIServer files wrapper in local mode bi-directional (server-client, client-server)
  Now you can convert local path to server path and server path to local path.
  [#779](https://github.com/aiogram/aiogram/issues/779)

## 3.0.0a18 (2021-11-10)

### Features

- Breaking: Changed the signature of the session middlewares
  Breaking: Renamed AiohttpSession.make_request method parameter from call to method to match the naming in the base class
  Added middleware for logging outgoing requests
  [#716](https://github.com/aiogram/aiogram/issues/716)
- Improved description of filters resolving error.
  For example when you try to pass wrong type of argument to the filter but don’t know why filter is not resolved now you can get error like this:

  ```
  aiogram.exceptions.FiltersResolveError: Unknown keyword filters: {'content_types'}
    Possible cases:
    - 1 validation error for ContentTypesFilter
      content_types
        Invalid content types {'42'} is not allowed here (type=value_error)
  ```

  [#717](https://github.com/aiogram/aiogram/issues/717)
- **Breaking internal API change**
  Reworked FSM Storage record keys propagation
  [#723](https://github.com/aiogram/aiogram/issues/723)
- Implemented new filter named `MagicData(magic_data)` that helps to filter event by data from middlewares or other filters

  For example your bot is running with argument named `config` that contains the application config then you can filter event by value from this config:

  ```
  @router.message(magic_data=F.event.from_user.id == F.config.admin_id)
  ...
  ```

  [#724](https://github.com/aiogram/aiogram/issues/724)

### Bugfixes

- Fixed I18n context inside error handlers
  [#726](https://github.com/aiogram/aiogram/issues/726)
- Fixed bot session closing before emit shutdown
  [#734](https://github.com/aiogram/aiogram/issues/734)
- Fixed: bound filter resolving does not require children routers
  [#736](https://github.com/aiogram/aiogram/issues/736)

### Misc

- Enabled testing on Python 3.10
  Removed async_lru dependency (is incompatible with Python 3.10) and replaced usage with protected property
  [#719](https://github.com/aiogram/aiogram/issues/719)
- Converted README.md to README.rst and use it as base file for docs
  [#725](https://github.com/aiogram/aiogram/issues/725)
- Rework filters resolving:

  - Automatically apply Bound Filters with default values to handlers
  - Fix data transfer from parent to included routers filters

  [#727](https://github.com/aiogram/aiogram/issues/727)
- Added full support of Bot API 5.4
  <https://core.telegram.org/bots/api-changelog#november-5-2021>
  [#744](https://github.com/aiogram/aiogram/issues/744)

## 3.0.0a17 (2021-09-24)

### Misc

- Added `html_text` and `md_text` to Message object
  [#708](https://github.com/aiogram/aiogram/issues/708)
- Refactored I18n, added context managers for I18n engine and current locale
  [#709](https://github.com/aiogram/aiogram/issues/709)

## 3.0.0a16 (2021-09-22)

### Features

- Added support of local Bot API server files downloading

  When Local API is enabled files can be downloaded via bot.download/bot.download_file methods.
  [#698](https://github.com/aiogram/aiogram/issues/698)
- Implemented I18n & L10n support
  [#701](https://github.com/aiogram/aiogram/issues/701)

### Misc

- Covered by tests and docs KeyboardBuilder util
  [#699](https://github.com/aiogram/aiogram/issues/699)
- **Breaking!!!**. Refactored and renamed exceptions.

  - Exceptions module was moved from `aiogram.utils.exceptions` to `aiogram.exceptions`
  - Added prefix Telegram for all error classes

  [#700](https://github.com/aiogram/aiogram/issues/700)
- Replaced all `pragma: no cover` marks via global `.coveragerc` config
  [#702](https://github.com/aiogram/aiogram/issues/702)
- Updated dependencies.

  **Breaking for framework developers**
  Now all optional dependencies should be installed as extra: poetry install -E fast -E redis -E proxy -E i18n -E docs
  [#703](https://github.com/aiogram/aiogram/issues/703)

## 3.0.0a15 (2021-09-10)

### Features

- Ability to iterate over all states in StatesGroup.
  Aiogram already had in check for states group so this is relative feature.
  [#666](https://github.com/aiogram/aiogram/issues/666)

### Bugfixes

- Fixed incorrect type checking in the `aiogram.utils.keyboard.KeyboardBuilder`
  [#674](https://github.com/aiogram/aiogram/issues/674)

### Misc

- Disable ContentType filter by default
  [#668](https://github.com/aiogram/aiogram/issues/668)
- Moved update type detection from Dispatcher to Update object
  [#669](https://github.com/aiogram/aiogram/issues/669)
- Updated **pre-commit** config
  [#681](https://github.com/aiogram/aiogram/issues/681)
- Reworked **handlers_in_use** util. Function moved to Router as method **.resolve_used_update_types()**
  [#682](https://github.com/aiogram/aiogram/issues/682)

## 3.0.0a14 (2021-08-17)

### Features

- add aliases for edit/delete reply markup to Message
  [#662](https://github.com/aiogram/aiogram/issues/662)
- Reworked outer middleware chain. Prevent to call many times the outer middleware for each nested router
  [#664](https://github.com/aiogram/aiogram/issues/664)

### Bugfixes

- Prepare parse mode for InputMessageContent in AnswerInlineQuery method
  [#660](https://github.com/aiogram/aiogram/issues/660)

### Improved Documentation

- Added integration with `towncrier`
  [#602](https://github.com/aiogram/aiogram/issues/602)

### Misc

- Added .editorconfig
  [#650](https://github.com/aiogram/aiogram/issues/650)
- Redis storage speedup globals
  [#651](https://github.com/aiogram/aiogram/issues/651)
- add allow_sending_without_reply param to Message reply aliases
  [#663](https://github.com/aiogram/aiogram/issues/663)

## 2.14.3 (2021-07-21)

- Fixed `ChatMember` type detection via adding customizable object serialization mechanism ([#624](https://github.com/aiogram/aiogram/issues/624), [#623](https://github.com/aiogram/aiogram/issues/623))

## 2.14.2 (2021-07-26)

- Fixed `MemoryStorage` cleaner ([#619](https://github.com/aiogram/aiogram/issues/619))
- Fixed unused default locale in `I18nMiddleware` ([#562](https://github.com/aiogram/aiogram/issues/562), [#563](https://github.com/aiogram/aiogram/issues/563))

## 2.14 (2021-07-27)

- Full support of Bot API 5.3 ([#610](https://github.com/aiogram/aiogram/issues/610), [#614](https://github.com/aiogram/aiogram/issues/614))
- Fixed `Message.send_copy` method for polls ([#603](https://github.com/aiogram/aiogram/issues/603))
- Updated pattern for `GroupDeactivated` exception ([#549](https://github.com/aiogram/aiogram/issues/549)
- Added `caption_entities` field in `InputMedia` base class ([#583](https://github.com/aiogram/aiogram/issues/583))
- Fixed HTML text decorations for tag `pre` ([#597](https://github.com/aiogram/aiogram/issues/597) fixes issues [#596](https://github.com/aiogram/aiogram/issues/596) and [#481](https://github.com/aiogram/aiogram/issues/481))
- Fixed `Message.get_full_command` method for messages with caption ([#576](https://github.com/aiogram/aiogram/issues/576))
- Improved `MongoStorage`: remove documents with empty data from `aiogram_data` collection to save memory. ([#609](https://github.com/aiogram/aiogram/issues/609))

## 2.13 (2021-04-28)

- Added full support of Bot API 5.2 ([#572](https://github.com/aiogram/aiogram/issues/572))
- Fixed usage of `provider_data` argument in `sendInvoice` method call
- Fixed builtin command filter args ([#556](https://github.com/aiogram/aiogram/issues/556)) ([#558](https://github.com/aiogram/aiogram/issues/558))
- Allowed to use State instances FSM storage directly ([#542](https://github.com/aiogram/aiogram/issues/542))
- Added possibility to get i18n locale without User instance ([#546](https://github.com/aiogram/aiogram/issues/546))
- Fixed returning type of `Bot.*_chat_invite_link()` methods [#548](https://github.com/aiogram/aiogram/issues/548) ([#549](https://github.com/aiogram/aiogram/issues/549))
- Fixed deep-linking util ([#569](https://github.com/aiogram/aiogram/issues/569))
- Small changes in documentation - describe limits in docstrings corresponding to the current limit. ([#565](https://github.com/aiogram/aiogram/issues/565))
- Fixed internal call to deprecated ‘is_private’ method ([#553](https://github.com/aiogram/aiogram/issues/553))
- Added possibility to use `allowed_updates` argument in Polling mode ([#564](https://github.com/aiogram/aiogram/issues/564))

## 2.12.1 (2021-03-22)

- Fixed `TypeError: Value should be instance of 'User' not 'NoneType'` ([#527](https://github.com/aiogram/aiogram/issues/527))
- Added missing `Chat.message_auto_delete_time` field ([#535](https://github.com/aiogram/aiogram/issues/535))
- Added `MediaGroup` filter ([#528](https://github.com/aiogram/aiogram/issues/528))
- Added `Chat.delete_message` shortcut ([#526](https://github.com/aiogram/aiogram/issues/526))
- Added mime types parsing for `aiogram.types.Document` ([#431](https://github.com/aiogram/aiogram/issues/431))
- Added warning in `TelegramObject.__setitem__` when Telegram adds a new field ([#532](https://github.com/aiogram/aiogram/issues/532))
- Fixed `examples/chat_type_filter.py` ([#533](https://github.com/aiogram/aiogram/issues/533))
- Removed redundant definitions in framework code ([#531](https://github.com/aiogram/aiogram/issues/531))

## 2.12 (2021-03-14)

- Full support for Telegram Bot API 5.1 ([#519](https://github.com/aiogram/aiogram/issues/519))
- Fixed sending playlist of audio files and documents ([#465](https://github.com/aiogram/aiogram/issues/465), [#468](https://github.com/aiogram/aiogram/issues/468))
- Fixed `FSMContextProxy.setdefault` method ([#491](https://github.com/aiogram/aiogram/issues/491))
- Fixed `Message.answer_location` and `Message.reply_location` unable to send live location ([#497](https://github.com/aiogram/aiogram/issues/497))
- Fixed `user_id` and `chat_id` getters from the context at Dispatcher `check_key`, `release_key` and `throttle` methods ([#520](https://github.com/aiogram/aiogram/issues/520))
- Fixed `Chat.update_chat` method and all similar situations ([#516](https://github.com/aiogram/aiogram/issues/516))
- Fixed `MediaGroup` attach methods ([#514](https://github.com/aiogram/aiogram/issues/514))
- Fixed state filter for inline keyboard query callback in groups ([#508](https://github.com/aiogram/aiogram/issues/508), [#510](https://github.com/aiogram/aiogram/issues/510))
- Added missing `ContentTypes.DICE` ([#466](https://github.com/aiogram/aiogram/issues/466))
- Added missing vcard argument to `InputContactMessageContent` constructor ([#473](https://github.com/aiogram/aiogram/issues/473))
- Add missing exceptions: `MessageIdInvalid`, `CantRestrictChatOwner` and `UserIsAnAdministratorOfTheChat` ([#474](https://github.com/aiogram/aiogram/issues/474), [#512](https://github.com/aiogram/aiogram/issues/512))
- Added `answer_chat_action` to the `Message` object ([#501](https://github.com/aiogram/aiogram/issues/501))
- Added dice to `message.send_copy` method ([#511](https://github.com/aiogram/aiogram/issues/511))
- Removed deprecation warning from `Message.send_copy`
- Added an example of integration between externally created aiohttp Application and aiogram ([#433](https://github.com/aiogram/aiogram/issues/433))
- Added `split_separator` argument to `safe_split_text` ([#515](https://github.com/aiogram/aiogram/issues/515))
- Fixed some typos in docs and examples ([#489](https://github.com/aiogram/aiogram/issues/489), [#490](https://github.com/aiogram/aiogram/issues/490), [#498](https://github.com/aiogram/aiogram/issues/498), [#504](https://github.com/aiogram/aiogram/issues/504), [#514](https://github.com/aiogram/aiogram/issues/514))

## 2.11.2 (2021-11-10)

- Fixed default parse mode
- Added missing “supports_streaming” argument to answer_video method [#462](https://github.com/aiogram/aiogram/issues/462)

## 2.11.1 (2021-11-10)

- Fixed files URL template
- Fix MessageEntity serialization for API calls [#457](https://github.com/aiogram/aiogram/issues/457)
- When entities are set, default parse_mode become disabled ([#461](https://github.com/aiogram/aiogram/issues/461))
- Added parameter supports_streaming to reply_video, remove redundant docstrings ([#459](https://github.com/aiogram/aiogram/issues/459))
- Added missing parameter to promoteChatMember alias ([#458](https://github.com/aiogram/aiogram/issues/458))

## 2.11 (2021-11-08)

- Added full support of Telegram Bot API 5.0 ([#454](https://github.com/aiogram/aiogram/issues/454))
- Added possibility to more easy specify custom API Server (example)
  :   - WARNING: API method `close` was named in Bot class as close_bot in due to Bot instance already has method with the same name. It will be changed in `aiogram 3.0`
- Added alias to Message object `Message.copy_to` with deprecation of `Message.send_copy`
- `ChatType.SUPER_GROUP` renamed to `ChatType.SUPERGROUP` ([#438](https://github.com/aiogram/aiogram/issues/438))

## 2.10.1 (2021-09-14)

- Fixed critical bug with getting asyncio event loop in executor. ([#424](https://github.com/aiogram/aiogram/issues/424)) `AttributeError: 'NoneType' object has no attribute 'run_until_complete'`

## 2.10 (2021-09-13)

- Breaking change: Stop using _MainThread event loop in bot/dispatcher instances ([#397](https://github.com/aiogram/aiogram/issues/397))
- Breaking change: Replaced aiomongo with motor ([#368](https://github.com/aiogram/aiogram/issues/368), [#380](https://github.com/aiogram/aiogram/issues/380))
- Fixed: TelegramObject’s aren’t destroyed after update handling [#307](https://github.com/aiogram/aiogram/issues/307) ([#371](https://github.com/aiogram/aiogram/issues/371))
- Add setting current context of Telegram types ([#369](https://github.com/aiogram/aiogram/issues/369))
- Fixed markdown escaping issues ([#363](https://github.com/aiogram/aiogram/issues/363))
- Fixed HTML characters escaping ([#409](https://github.com/aiogram/aiogram/issues/409))
- Fixed italic and underline decorations when parse entities to Markdown
- Fixed [#413](https://github.com/aiogram/aiogram/issues/413): parse entities positioning ([#414](https://github.com/aiogram/aiogram/issues/414))
- Added missing thumb parameter ([#362](https://github.com/aiogram/aiogram/issues/362))
- Added public methods to register filters and middlewares ([#370](https://github.com/aiogram/aiogram/issues/370))
- Added ChatType builtin filter ([#356](https://github.com/aiogram/aiogram/issues/356))
- Fixed IDFilter checking message from channel ([#376](https://github.com/aiogram/aiogram/issues/376))
- Added missed answer_poll and reply_poll ([#384](https://github.com/aiogram/aiogram/issues/384))
- Added possibility to ignore message caption in commands filter ([#383](https://github.com/aiogram/aiogram/issues/383))
- Fixed addStickerToSet method
- Added preparing thumb in send_document method ([#391](https://github.com/aiogram/aiogram/issues/391))
- Added exception MessageToPinNotFound ([#404](https://github.com/aiogram/aiogram/issues/404))
- Fixed handlers parameter-spec solving ([#408](https://github.com/aiogram/aiogram/issues/408))
- Fixed CallbackQuery.answer() returns nothing ([#420](https://github.com/aiogram/aiogram/issues/420))
- CHOSEN_INLINE_RESULT is a correct API-term ([#415](https://github.com/aiogram/aiogram/issues/415))
- Fixed missing attributes for Animation class ([#422](https://github.com/aiogram/aiogram/issues/422))
- Added missed emoji argument to reply_dice ([#395](https://github.com/aiogram/aiogram/issues/395))
- Added is_chat_creator method to ChatMemberStatus ([#394](https://github.com/aiogram/aiogram/issues/394))
- Added missed ChatPermissions to __all__ ([#393](https://github.com/aiogram/aiogram/issues/393))
- Added is_forward method to Message ([#390](https://github.com/aiogram/aiogram/issues/390))
- Fixed usage of deprecated is_private function ([#421](https://github.com/aiogram/aiogram/issues/421))

and many others documentation and examples changes:

- Updated docstring of RedisStorage2 ([#423](https://github.com/aiogram/aiogram/issues/423))
- Updated I18n example (added docs and fixed typos) ([#419](https://github.com/aiogram/aiogram/issues/419))
- A little documentation revision ([#381](https://github.com/aiogram/aiogram/issues/381))
- Added comments about correct errors_handlers usage ([#398](https://github.com/aiogram/aiogram/issues/398))
- Fixed typo rexex -> regex ([#386](https://github.com/aiogram/aiogram/issues/386))
- Fixed docs Quick start page code blocks ([#417](https://github.com/aiogram/aiogram/issues/417))
- fixed type hints of callback_data ([#400](https://github.com/aiogram/aiogram/issues/400))
- Prettify readme, update downloads stats badge ([#406](https://github.com/aiogram/aiogram/issues/406))

## 2.9.2 (2021-06-13)

- Fixed `Message.get_full_command()` [#352](https://github.com/aiogram/aiogram/issues/352)
- Fixed markdown util [#353](https://github.com/aiogram/aiogram/issues/353)

## 2.9 (2021-06-08)

- Added full support of Telegram Bot API 4.9
- Fixed user context at poll_answer update ([#322](https://github.com/aiogram/aiogram/issues/322))
- Fix Chat.set_description ([#325](https://github.com/aiogram/aiogram/issues/325))
- Add lazy session generator ([#326](https://github.com/aiogram/aiogram/issues/326))
- Fix text decorations ([#315](https://github.com/aiogram/aiogram/issues/315), [#316](https://github.com/aiogram/aiogram/issues/316), [#328](https://github.com/aiogram/aiogram/issues/328))
- Fix missing `InlineQueryResultPhoto` `parse_mode` field ([#331](https://github.com/aiogram/aiogram/issues/331))
- Fix fields from parent object in `KeyboardButton` ([#344](https://github.com/aiogram/aiogram/issues/344) fixes [#343](https://github.com/aiogram/aiogram/issues/343))
- Add possibility to get bot id without calling `get_me` ([#296](https://github.com/aiogram/aiogram/issues/296))

## 2.8 (2021-04-26)

- Added full support of Bot API 4.8
- Added `Message.answer_dice` and `Message.reply_dice` methods ([#306](https://github.com/aiogram/aiogram/issues/306))

## 2.7 (2021-04-07)

- Added full support of Bot API 4.7 ([#294](https://github.com/aiogram/aiogram/issues/294) [#289](https://github.com/aiogram/aiogram/issues/289))
- Added default parse mode for send_animation method ([#293](https://github.com/aiogram/aiogram/issues/293) [#292](https://github.com/aiogram/aiogram/issues/292))
- Added new API exception when poll requested in public chats ([#270](https://github.com/aiogram/aiogram/issues/270))
- Make correct User and Chat get_mention methods ([#277](https://github.com/aiogram/aiogram/issues/277))
- Small changes and other minor improvements

## 2.6.1 (2021-01-25)

- Fixed reply `KeyboardButton` initializer with `request_poll` argument ([#266](https://github.com/aiogram/aiogram/issues/266))
- Added helper for poll types (`aiogram.types.PollType`)
- Changed behavior of Telegram_object `.as_*` and `.to_*` methods. It will no more mutate the object. ([#247](https://github.com/aiogram/aiogram/issues/247))

## 2.6 (2021-01-23)

- Full support of Telegram Bot API v4.6 (Polls 2.0) [#265](https://github.com/aiogram/aiogram/issues/265)
- Aded new filter - IsContactSender (commit)
- Fixed proxy extra dependencies version [#262](https://github.com/aiogram/aiogram/issues/262)

## 2.5.3 (2021-01-05)

- [#255](https://github.com/aiogram/aiogram/issues/255) Updated CallbackData factory validity check. More correct for non-latin symbols
- [#256](https://github.com/aiogram/aiogram/issues/256) Fixed `renamed_argument` decorator error
- [#257](https://github.com/aiogram/aiogram/issues/257) One more fix of CommandStart filter

## 2.5.2 (2021-01-01)

- Get back `quote_html` and `escape_md` functions

## 2.5.1 (2021-01-01)

- Hot-fix of `CommandStart` filter

## 2.5 (2021-01-01)

- Added full support of Telegram Bot API 4.5 ([#250](https://github.com/aiogram/aiogram/issues/250), [#251](https://github.com/aiogram/aiogram/issues/251))
- [#239](https://github.com/aiogram/aiogram/issues/239) Fixed `check_token` method
- [#238](https://github.com/aiogram/aiogram/issues/238), [#241](https://github.com/aiogram/aiogram/issues/241): Added deep-linking utils
- [#248](https://github.com/aiogram/aiogram/issues/248) Fixed support of aiohttp-socks
- Updated setup.py. No more use of internal pip API
- Updated links to documentations (<https://docs.aiogram.dev>)
- Other small changes and minor improvements ([#223](https://github.com/aiogram/aiogram/issues/223) and others…)

## 2.4 (2021-10-29)

- Added Message.send_copy method (forward message without forwarding)
- Safe close of aiohttp client session (no more exception when application is shutdown)
- No more “adWanced” words in project [#209](https://github.com/aiogram/aiogram/issues/209)
- Arguments user and chat is renamed to user_id and chat_id in Dispatcher.throttle method [#196](https://github.com/aiogram/aiogram/issues/196)
- Fixed set_chat_permissions [#198](https://github.com/aiogram/aiogram/issues/198)
- Fixed Dispatcher polling task does not process cancellation [#199](https://github.com/aiogram/aiogram/issues/199), [#201](https://github.com/aiogram/aiogram/issues/201)
- Fixed compatibility with latest asyncio version [#200](https://github.com/aiogram/aiogram/issues/200)
- Disabled caching by default for lazy_gettext method of I18nMiddleware [#203](https://github.com/aiogram/aiogram/issues/203)
- Fixed HTML user mention parser [#205](https://github.com/aiogram/aiogram/issues/205)
- Added IsReplyFilter [#210](https://github.com/aiogram/aiogram/issues/210)
- Fixed send_poll method arguments [#211](https://github.com/aiogram/aiogram/issues/211)
- Added OrderedHelper [#215](https://github.com/aiogram/aiogram/issues/215)
- Fix incorrect completion order. [#217](https://github.com/aiogram/aiogram/issues/217)

## 2.3 (2021-08-16)

- Full support of Telegram Bot API 4.4
- Fixed [#143](https://github.com/aiogram/aiogram/issues/143)
- Added new filters from issue [#151](https://github.com/aiogram/aiogram/issues/151): [#172](https://github.com/aiogram/aiogram/issues/172), [#176](https://github.com/aiogram/aiogram/issues/176), [#182](https://github.com/aiogram/aiogram/issues/182)
- Added expire argument to RedisStorage2 and other storage fixes [#145](https://github.com/aiogram/aiogram/issues/145)
- Fixed JSON and Pickle storages [#138](https://github.com/aiogram/aiogram/issues/138)
- Implemented MongoStorage [#153](https://github.com/aiogram/aiogram/issues/153) based on aiomongo (soon motor will be also added)
- Improved tests
- Updated examples
- Warning: Updated auth widget util. [#190](https://github.com/aiogram/aiogram/issues/190)
- Implemented throttle decorator [#181](https://github.com/aiogram/aiogram/issues/181)

## 2.2 (2021-06-09)

- Provides latest Telegram Bot API (4.3)
- Updated docs for filters
- Added opportunity to use different bot tokens from single bot instance (via context manager, [#100](https://github.com/aiogram/aiogram/issues/100))
- IMPORTANT: Fixed Typo: `data` -> `bucket` in `update_bucket` for RedisStorage2 ([#132](https://github.com/aiogram/aiogram/issues/132))

## 2.1 (2021-04-18)

- Implemented all new features from Telegram Bot API 4.2
- `is_member` and `is_admin` methods of `ChatMember` and `ChatMemberStatus` was renamed to `is_chat_member` and `is_chat_admin`
- Remover func filter
- Added some useful Message edit functions (`Message.edit_caption`, `Message.edit_media`, `Message.edit_reply_markup`) ([#121](https://github.com/aiogram/aiogram/issues/121), [#103](https://github.com/aiogram/aiogram/issues/103), [#104](https://github.com/aiogram/aiogram/issues/104), [#112](https://github.com/aiogram/aiogram/issues/112))
- Added requests timeout for all methods ([#110](https://github.com/aiogram/aiogram/issues/110))
- Added `answer*` methods to `Message` object ([#112](https://github.com/aiogram/aiogram/issues/112))
- Maked some improvements of `CallbackData` factory
- Added deep-linking parameter filter to `CommandStart` filter
- Implemented opportunity to use DNS over socks ([#97](https://github.com/aiogram/aiogram/issues/97) -> [#98](https://github.com/aiogram/aiogram/issues/98))
- Implemented logging filter for extending LogRecord attributes (Will be usefull with external logs collector utils like GrayLog, Kibana and etc.)
- Updated `requirements.txt` and `dev_requirements.txt` files
- Other small changes and minor improvements

## 2.0.1 (2021-12-31)

- Implemented CallbackData factory ([example](https://github.com/aiogram/aiogram/blob/master/examples/callback_data_factory.py))
- Implemented methods for answering to inline query from context and reply with animation to the messages. [#85](https://github.com/aiogram/aiogram/issues/85)
- Fixed installation from tar.gz [#84](https://github.com/aiogram/aiogram/issues/84)
- More exceptions (`ChatIdIsEmpty` and `NotEnoughRightsToRestrict`)

## 2.0 (2021-10-28)

This update will break backward compability with Python 3.6 and works only with Python 3.7+:
- contextvars (PEP-567);
- New syntax for annotations (PEP-563).

Changes:
- Used contextvars instead of `aiogram.utils.context`;
- Implemented filters factory;
- Implemented new filters mechanism;
- Allowed to customize command prefix in CommandsFilter;
- Implemented mechanism of passing results from filters (as dicts) as kwargs in handlers (like fixtures in pytest);
- Implemented states group feature;
- Implemented FSM storage’s proxy;
- Changed files uploading mechanism;
- Implemented pipe for uploading files from URL;
- Implemented I18n Middleware;
- Errors handlers now should accept only two arguments (current update and exception);
- Used `aiohttp_socks` instead of `aiosocksy` for Socks4/5 proxy;
- types.ContentType was divided to `types.ContentType` and `types.ContentTypes`;
- Allowed to use rapidjson instead of ujson/json;
- `.current()` method in bot and dispatcher objects was renamed to `get_current()`;

Full changelog
- You can read more details about this release in migration FAQ: <https://aiogram.readthedocs.io/en/latest/migration_1_to_2.html>

## 1.4 (2021-08-03)

- Bot API 4.0 ([#57](https://github.com/aiogram/aiogram/issues/57))

## 1.3.3 (2021-07-16)

- Fixed markup-entities parsing;
- Added more API exceptions;
- Now InlineQueryResultLocation has live_period;
- Added more message content types;
- Other small changes and minor improvements.

## 1.3.2 (2021-05-27)

- Fixed crashing of polling process. (i think)
- Added parse_mode field into input query results according to Bot API Docs.
- Added new methods for Chat object. ([#42](https://github.com/aiogram/aiogram/issues/42), [#43](https://github.com/aiogram/aiogram/issues/43))
- **Warning**: disabled connections limit for bot aiohttp session.
- **Warning**: Destroyed “temp sessions” mechanism.
- Added new error types.
- Refactored detection of error type.
- Small fixes of executor util.
- Fixed RethinkDBStorage

## 1.3.1 (2018-05-27)

## 1.3 (2021-04-22)

- Allow to use Socks5 proxy (need manually install `aiosocksy`).
- Refactored `aiogram.utils.executor` module.
- **[Warning]** Updated requirements list.

## 1.2.3 (2018-04-14)

- Fixed API errors detection
- Fixed compability of `setup.py` with pip 10.0.0

## 1.2.2 (2018-04-08)

- Added more error types.
- Implemented method `InputFile.from_url(url: str)` for downloading files.
- Implemented big part of API method tests.
- Other small changes and mminor improvements.

## 1.2.1 (2018-03-25)

- Fixed handling Venue’s [[#27](https://github.com/aiogram/aiogram/issues/27), [#26](https://github.com/aiogram/aiogram/issues/26)]
- Added parse_mode to all medias (Bot API 3.6 support) [[#23](https://github.com/aiogram/aiogram/issues/23)]
- Now regexp filter can be used with callback query data [[#19](https://github.com/aiogram/aiogram/issues/19)]
- Improvements in `InlineKeyboardMarkup` & `ReplyKeyboardMarkup` objects [[#21](https://github.com/aiogram/aiogram/issues/21)]
- Other bug & typo fixes and minor improvements.

## 1.2 (2018-02-23)

- Full provide Telegram Bot API 3.6
- Fixed critical error: `Fatal Python error: PyImport_GetModuleDict: no module dictionary!`
- Implemented connection pool in RethinkDB driver
- Typo fixes of documentstion
- Other bug fixes and minor improvements.

## 1.1 (2018-01-27)

- Added more methods for data types (like `message.reply_sticker(...)` or `file.download(...)`
- Typo fixes of documentstion
- Allow to set default parse mode for messages (`Bot( ... , parse_mode='HTML')`)
- Allowed to cancel event from the `Middleware.on_pre_process_<event type>`
- Fixed sending files with correct names.
- Fixed MediaGroup
- Added RethinkDB storage for FSM (`aiogram.contrib.fsm_storage.rethinkdb`)

## 1.0.4 (2018-01-10)

## 1.0.3 (2018-01-07)

- Added middlewares mechanism.
- Added example for middlewares and throttling manager.
- Added logging middleware (`aiogram.contrib.middlewares.logging.LoggingMiddleware`)
- Fixed handling errors in async tasks (marked as ‘async_task’)
- Small fixes and other minor improvements.

## 1.0.2 (2017-11-29)

## 1.0.1 (2017-11-21)

- Implemented `types.InputFile` for more easy sending local files
- **Danger!** Fixed typo in word pooling. Now whatever all methods with that word marked as deprecated and original methods is renamed to polling. Check it in you’r code before updating!
- Fixed helper for chat actions (`types.ChatActions`)
- Added [example](https://github.com/aiogram/aiogram/blob/master/examples/media_group.py) for media group.

## 1.0 (2017-11-19)

- Remaked data types serialozation/deserialization mechanism (Speed up).
- Fully rewrited all Telegram data types.
- Bot object was fully rewritted (regenerated).
- Full provide Telegram Bot API 3.4+ (with sendMediaGroup)
- Warning: Now `BaseStorage.close()` is awaitable! (FSM)
- Fixed compability with uvloop.
- More employments for `aiogram.utils.context`.
- Allowed to disable `ujson`.
- Other bug fixes and minor improvements.
- Migrated from Bitbucket to Github.

## 0.4.1 (2017-08-03)

## 0.4 (2017-08-05)

## 0.3.4 (2017-08-04)

## 0.3.3 (2017-07-05)

## 0.3.2 (2017-07-04)

## 0.3.1 (2017-07-04)

## 0.2b1 (2017-06-00)

## 0.1 (2017-06-03)
