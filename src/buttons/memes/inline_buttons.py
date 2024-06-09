from aiogram import types
from aiogram.types import InlineKeyboardMarkup

from src.buttons.memes.builder import create_inline_keyboard


def get_cancel_button() -> InlineKeyboardMarkup:
    buttons = [
        types.InlineKeyboardButton(
            text='Отменить 🗑️',
            callback_data='cancel_creation',
        ),
    ]
    return create_inline_keyboard(buttons)


def get_buttons(likes: int, dislikes: int, navigation: bool = False, add: bool = False) -> InlineKeyboardMarkup:
    buttons = [
        types.InlineKeyboardButton(
            text=f'🩷 {likes}',
            callback_data='like',
        ),
        types.InlineKeyboardButton(
            text=f'👎 {dislikes}',
            callback_data='dislike',
        ),
    ]
    if navigation:
        buttons.append(
            types.InlineKeyboardButton(
                text='◀️',
                callback_data='prev',
            )
        )
        buttons.append(
            types.InlineKeyboardButton(
                text='▶️',
                callback_data='next',
            )
        )
    if add:
        buttons.append(
            types.InlineKeyboardButton(
                text='🗂️',
                callback_data='add',
            )
        )
    return create_inline_keyboard(buttons)
