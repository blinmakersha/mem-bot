from typing import List

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_inline_keyboard(buttons: List[types.InlineKeyboardButton], row_width: int = 2) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in range(0, len(buttons), row_width):
        builder.row(*buttons[i : i + row_width])
    return builder.as_markup()
