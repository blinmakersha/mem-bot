from typing import ParamSpec

from aiogram import types

CREATE_MEM = 'Создать мем 📝'
MY_MEMES = 'Мои мемы 🗂️'
RANDOM_MEM = 'Случайный мем 🔀'
ALL_MEMES = 'Посмотреть доступные мемы 🗞️'
TRENDY_MEM = 'Популярный мем 📊'


P = ParamSpec('P')


def get_keyboard(has_already_liked: bool, **kwargs) -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=CREATE_MEM), types.KeyboardButton(text=MY_MEMES)],
        [types.KeyboardButton(text=RANDOM_MEM), types.KeyboardButton(text=ALL_MEMES)],
        [types.KeyboardButton(text=TRENDY_MEM)],
    ]

    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
