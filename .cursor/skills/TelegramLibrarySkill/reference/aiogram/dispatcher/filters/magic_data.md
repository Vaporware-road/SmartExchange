# MagicData

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/filters/magic_data.html](https://docs.aiogram.dev/en/latest/dispatcher/filters/magic_data.html)

## Usage

1. `MagicData(F.event.from_user.id == F.config.admin_id)` (Note that `config` should be passed from middleware)

## Explanation

*class* aiogram.filters.magic_data.MagicData(*magic_data: MagicFilter*)
:   This filter helps to filter event with contextual data

    magic_data

Can be imported:

- `from aiogram.filters import MagicData`

## Allowed handlers

Allowed update types for this filter:

- `message`
- `edited_message`
- `channel_post`
- `edited_channel_post`
- `inline_query`
- `chosen_inline_result`
- `callback_query`
- `shipping_query`
- `pre_checkout_query`
- `poll`
- `poll_answer`
- `my_chat_member`
- `chat_member`
- `chat_join_request`
- `error`
