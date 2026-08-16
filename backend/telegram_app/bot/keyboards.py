"""Reply-keyboard helpers for customer bot handlers."""

from __future__ import annotations

from typing import Any, Iterable, List, Mapping, Union

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from telegram_app.services.conversation import MAIN_MENU_BUTTONS, MAIN_MENU_TEXT

__all__ = ["MAIN_MENU_BUTTONS", "MAIN_MENU_TEXT", "as_reply_markup"]


def as_reply_markup(
    buttons: Iterable[Iterable[Mapping[str, Any] | str]] | None,
    *,
    remove_keyboard: bool = False,
) -> Union[ReplyKeyboardMarkup, ReplyKeyboardRemove, None]:
    if remove_keyboard and not buttons:
        return ReplyKeyboardRemove()
    if not buttons:
        return None
    keyboard: List[List[KeyboardButton]] = []
    for row in buttons:
        if isinstance(row, Mapping):
            row = [row]
        elif isinstance(row, str):
            row = [row]
        button_row: List[KeyboardButton] = []
        for button in row:
            if isinstance(button, str):
                text = button
            elif isinstance(button, Mapping):
                text = button.get("text")
            else:
                continue
            if not text:
                continue
            button_row.append(KeyboardButton(text=str(text)))
        if button_row:
            keyboard.append(button_row)
    if not keyboard:
        return ReplyKeyboardRemove() if remove_keyboard else None
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        is_persistent=True,
    )
