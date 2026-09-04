# BusinessBotRights

> Source: [https://docs.aiogram.dev/en/latest/api/types/business_bot_rights.html](https://docs.aiogram.dev/en/latest/api/types/business_bot_rights.html)

*class* aiogram.types.business_bot_rights.BusinessBotRights(*\**, *can_reply: bool | None = None*, *can_read_messages: bool | None = None*, *can_delete_sent_messages: bool | None = None*, *can_delete_all_messages: bool | None = None*, *can_edit_name: bool | None = None*, *can_edit_bio: bool | None = None*, *can_edit_profile_photo: bool | None = None*, *can_edit_username: bool | None = None*, *can_change_gift_settings: bool | None = None*, *can_view_gifts_and_stars: bool | None = None*, *can_convert_gifts_to_stars: bool | None = None*, *can_transfer_and_upgrade_gifts: bool | None = None*, *can_transfer_stars: bool | None = None*, *can_manage_stories: bool | None = None*, *can_delete_outgoing_messages: bool | None = None*, *\*\*extra_data: Any*)
:   Represents the rights of a business bot.

    Source: <https://core.telegram.org/bots/api#businessbotrights>

    can_reply*: bool | None*
    :   *Optional*. `True`, if the bot can send and edit messages in the private chats that had incoming messages in the last 24 hours

    can_read_messages*: bool | None*
    :   *Optional*. `True`, if the bot can mark incoming private messages as read

    can_delete_sent_messages*: bool | None*
    :   *Optional*. `True`, if the bot can delete messages sent by the bot

    can_delete_all_messages*: bool | None*
    :   *Optional*. `True`, if the bot can delete all private messages in managed chats

    can_edit_name*: bool | None*
    :   *Optional*. `True`, if the bot can edit the first and last name of the business account

    can_edit_bio*: bool | None*
    :   *Optional*. `True`, if the bot can edit the bio of the business account

    can_edit_profile_photo*: bool | None*
    :   *Optional*. `True`, if the bot can edit the profile photo of the business account

    can_edit_username*: bool | None*
    :   *Optional*. `True`, if the bot can edit the username of the business account

    can_change_gift_settings*: bool | None*
    :   *Optional*. `True`, if the bot can change the privacy settings pertaining to gifts for the business account

    can_view_gifts_and_stars*: bool | None*
    :   *Optional*. `True`, if the bot can view gifts and the amount of Telegram Stars owned by the business account

    can_convert_gifts_to_stars*: bool | None*
    :   *Optional*. `True`, if the bot can convert regular gifts owned by the business account to Telegram Stars

    can_transfer_and_upgrade_gifts*: bool | None*
    :   *Optional*. `True`, if the bot can transfer and upgrade gifts owned by the business account

    can_transfer_stars*: bool | None*
    :   *Optional*. `True`, if the bot can transfer Telegram Stars received by the business account to its own account, or use them to upgrade and transfer gifts

    can_manage_stories*: bool | None*
    :   *Optional*. `True`, if the bot can post, edit and delete stories on behalf of the business account

    can_delete_outgoing_messages*: bool | None*
    :   *Optional*. True, if the bot can delete messages sent by the bot

        Deprecated since version API:9.1: <https://core.telegram.org/bots/api-changelog#july-3-2025>
