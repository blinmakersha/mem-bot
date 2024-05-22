from aiogram import types


def get_keyboard() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text="Подобрать мем")],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb)
