from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiohttp import ClientResponseError

from src.handlers.memes.router import memes_router
from src.utils.request import do_request

from conf.config import settings


@memes_router.callback_query(F.data == 'add')
async def add_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    current_index = data['current_index']
    mem = data['memes'][current_index]

    try:
        await do_request(
            f'{settings.MEM_BACKEND_HOST}/mem/add-to-cart/{mem["id"]}',
            method='GET',
        )
        await callback.answer('Запись добавлена в избранное!')
    except ClientResponseError:
        await callback.answer('Произошла ошибка при добавлении в избранное.')
