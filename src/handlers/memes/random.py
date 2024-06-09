from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiohttp import ClientResponseError

from src.buttons.help.getter import RANDOM_MEM
from src.buttons.memes.inline_buttons import get_buttons
from src.handlers.memes.router import memes_router
from src.logger import logger
from src.requests.get import fetch_mem
from src.state.mem import update_state_with_mem_info
from src.template.render import render

from conf.config import settings


@memes_router.message(F.text == RANDOM_MEM)
async def get_random_mem(message: types.Message, state: FSMContext) -> None:
    try:
        data = await fetch_mem('/mem/random')
    except ClientResponseError:
        logger.exception('Error fetching random mem')
        await message.answer('Что-то пошло не так 🫣')
    if mem_info := data:
        if 'message' not in data:
            image_url = f'{settings.MEM_BACKEND_HOST}/mem/download/{mem_info["id"]}'
            await update_state_with_mem_info(state, [mem_info], navigation=False, add=True)
            await message.answer_photo(
                photo=image_url,
                caption=render('memes/card.jinja2', mem_info=data),
                reply_markup=get_buttons(mem_info['likes'], mem_info['dislikes'], navigation=False, add=True),
            )
        else:
            await message.answer('Ничего нет')
