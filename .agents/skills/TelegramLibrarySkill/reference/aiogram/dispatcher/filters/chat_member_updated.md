# ChatMemberUpdated

> Source: [https://docs.aiogram.dev/en/latest/dispatcher/filters/chat_member_updated.html](https://docs.aiogram.dev/en/latest/dispatcher/filters/chat_member_updated.html)

## Usage

Handle user leave or join events

```
from aiogram.filters import IS_MEMBER, IS_NOT_MEMBER

@router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
async def on_user_leave(event: ChatMemberUpdated): ...

@router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def on_user_join(event: ChatMemberUpdated): ...
```

Or construct your own terms via using pre-defined set of statuses and transitions.

## Explanation

*class* aiogram.filters.chat_member_updated.ChatMemberUpdatedFilter(*member_status_changed: _MemberStatusMarker | _MemberStatusGroupMarker | _MemberStatusTransition*)
:   member_status_changed

You can import from `aiogram.filters` all available
variants of [statuses](#statuses), [status groups](#status-groups) or [transitions](#transitions):

## Statuses

| name | Description |
| --- | --- |
| `CREATOR` | Chat owner |
| `ADMINISTRATOR` | Chat administrator |
| `MEMBER` | Member of the chat |
| `RESTRICTED` | Restricted user (can be not member) |
| `LEFT` | Isn’t member of the chat |
| `KICKED` | Kicked member by administrators |

Statuses can be extended with is_member flag by prefixing with
`+` (for `is_member == True)` or `-` (for `is_member == False`) symbol,
like `+RESTRICTED` or `-RESTRICTED`

## Status groups

The particular statuses can be combined via bitwise `or` operator, like `CREATOR | ADMINISTRATOR`

| name | Description |
| --- | --- |
| `IS_MEMBER` | Combination of `(CREATOR | ADMINISTRATOR | MEMBER | +RESTRICTED)` statuses. |
| `IS_ADMIN` | Combination of `(CREATOR | ADMINISTRATOR)` statuses. |
| `IS_NOT_MEMBER` | Combination of `(LEFT | KICKED | -RESTRICTED)` statuses. |

## Transitions

Transitions can be defined via bitwise shift operators `>>` and `<<`.
Old chat member status should be defined in the left side for `>>` operator (right side for `<<`)
and new status should be specified on the right side for `>>` operator (left side for `<<`)

The direction of transition can be changed via bitwise inversion operator: `~JOIN_TRANSITION`
will produce swap of old and new statuses.

| name | Description |
| --- | --- |
| `JOIN_TRANSITION` | Means status changed from `IS_NOT_MEMBER` to `IS_MEMBER` (`IS_NOT_MEMBER >> IS_MEMBER`) |
| `LEAVE_TRANSITION` | Means status changed from `IS_MEMBER` to `IS_NOT_MEMBER` (`~JOIN_TRANSITION`) |
| `PROMOTED_TRANSITION` | Means status changed from `(MEMBER | RESTRICTED | LEFT | KICKED) >> ADMINISTRATOR` (`(MEMBER | RESTRICTED | LEFT | KICKED) >> ADMINISTRATOR`) |

Note

Note that if you define the status unions (via `|`) you will need to add brackets for the statement
before use shift operator in due to operator priorities.

## Allowed handlers

Allowed update types for this filter:

- my_chat_member
- chat_member
