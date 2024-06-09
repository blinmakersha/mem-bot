from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiohttp import ClientResponseError

from src.buttons.memes.inline_buttons import get_buttons
from src.handlers.memes.router import memes_router
from src.logger import logger
from src.utils.request import do_request

from conf.config import settings


@memes_router.callback_query(F.data == 'like')
async def like_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    nav = data['navigation']
    add = data['add']
    current_index = data['current_index']
    mem = data['memes'][current_index]

    data = await send_feedback(mem['id'], 'like')

    if data:
        current_likes = mem.get('likes', 0)
        current_dislikes = mem.get('dislikes', 0)

        if data['likes'] != current_likes or data['dislikes'] != current_dislikes:
            memes = (await state.get_data())['memes']
            memes[current_index]['likes'] = data['likes']
            memes[current_index]['dislikes'] = data['dislikes']

            await state.update_data(memes=memes)

            await callback.message.edit_reply_markup(
                reply_markup=get_buttons(data['likes'], data['dislikes'], nav, add)
            )

        await callback.answer()
    else:
        await callback.answer()


@memes_router.callback_query(F.data == 'dislike')
async def dislike_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    nav = data['navigation']
    add = data['add']
    current_index = data['current_index']
    mem = data['memes'][current_index]
    print(mem)

    data = await send_feedback(mem['id'], 'dislike')

    print(data)
    if data:
        current_likes = mem.get('likes', 0)
        current_dislikes = mem.get('dislikes', 0)

        if data['likes'] != current_likes or data['dislikes'] != current_dislikes:
            memes = (await state.get_data())['memes']
            memes[current_index]['likes'] = data['likes']
            memes[current_index]['dislikes'] = data['dislikes']
            print(memes)

            await state.update_data(memes=memes)

            await callback.message.edit_reply_markup(
                reply_markup=get_buttons(data['likes'], data['dislikes'], nav, add)
            )

        await callback.answer()
    else:
        await callback.answer()


async def send_feedback(mem_id: int, mark: str) -> dict:
    try:
        return await do_request(
            f'{settings.MEM_BACKEND_HOST}/mem/mark/{mem_id}?mark={mark}',
            method='GET',
        )
    except ClientResponseError:
        logger.exception('Ошибка')
