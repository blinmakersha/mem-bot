from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiohttp import ClientResponseError

from src.buttons.help.getter import ALL_MEMES
from src.buttons.memes.inline_buttons import get_buttons
from src.handlers.memes.router import memes_router
from src.state.mem import update_state_with_mem_info
from src.template.render import render
from src.utils.request import do_request

from conf.config import settings


@memes_router.message(F.text == ALL_MEMES)
async def get_memes(message: types.Message, state: FSMContext) -> None:
    try:
        data = await do_request(f'{settings.MEM_BACKEND_HOST}/mem/', params={'cart_type': 'general'}, method='GET')
        mem = data[0]
        image_url = f'{settings.MEM_BACKEND_HOST}/mem/download/{mem["id"]}'

        await update_state_with_mem_info(state, data, navigation=True, add=True)
        await message.answer_photo(
            photo=image_url,
            caption=render('memes/card.jinja2', mem_info=mem),
            reply_markup=get_buttons(mem['likes'], mem['dislikes'], navigation=True, add=True),
        )
    except KeyError:
        await message.answer('Что-то пошло не так 🫣')
        return
