from aiogram import F, types
from aiogram.fsm.context import FSMContext

from src.buttons.memes.inline_buttons import get_buttons
from src.handlers.memes.router import memes_router
from src.template.render import render

from conf.config import settings


@memes_router.callback_query(F.data == 'prev')
async def previous_mem(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    nav = data['navigation']
    add = data['add']
    current_index = data['current_index']

    if current_index > 0:
        current_index -= 1
    else:
        current_index = len(data['memes']) - 1

    mem = data['memes'][current_index]
    image_url = f'{settings.MEM_BACKEND_HOST}/mem/download/{mem["id"]}'

    await state.update_data(current_index=current_index)

    new_markup = get_buttons(mem['likes'], mem['dislikes'], nav, add)

    if callback.message.reply_markup != new_markup:
        await callback.message.edit_media(
            media=types.InputMediaPhoto(media=image_url, caption=render('memes/card.jinja2', mem_info=mem)),
            reply_markup=new_markup,
        )
    await callback.answer()


@memes_router.callback_query(F.data == 'next')
async def next_mem(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    nav = data['navigation']
    add = data['add']
    current_index = data['current_index']
    if current_index < len(data['memes']) - 1:
        current_index += 1
    else:
        current_index = 0

    mem = data['memes'][current_index]
    image_url = f'{settings.MEM_BACKEND_HOST}/mem/download/{mem["id"]}'

    await state.update_data(current_index=current_index)

    new_markup = get_buttons(mem['likes'], mem['dislikes'], nav, add)

    if callback.message.reply_markup != new_markup:
        await callback.message.edit_media(
            media=types.InputMediaPhoto(media=image_url, caption=render('memes/card.jinja2', mem_info=mem)),
            reply_markup=new_markup,
        )
    await callback.answer()
