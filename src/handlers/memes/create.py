from io import BytesIO

from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiohttp import ClientResponseError, FormData

from src.buttons.help.getter import CREATE_MEM
from src.buttons.memes.inline_buttons import get_buttons, get_cancel_button
from src.handlers.memes.router import memes_router
from src.logger import logger
from src.state.mem import CreateMemState, update_state_with_mem_info
from src.template.render import render
from src.utils.request import do_request

from conf.config import settings


@memes_router.message(F.text == CREATE_MEM)
async def form_create(message: types.Message, state: FSMContext) -> None:
    await state.set_state(CreateMemState.text)
    await message.answer('Введите текст для мема ✍🏽', reply_markup=get_cancel_button())


@memes_router.message(CreateMemState.text)
async def form_text(message: Message, state: FSMContext):
    if message.text:
        await state.update_data(text=message.text)
        await state.set_state(CreateMemState.photo)
        await message.answer('Добавьте фото 🖼️', reply_markup=get_cancel_button())
    else:
        await message.delete()


@memes_router.message(CreateMemState.photo, F.photo)
async def form_photo(message: types.Message, state: FSMContext) -> None:
    if message.photo:
        file_id = message.photo[-1].file_id
        file_info = await message.bot.get_file(file_id)
        file_name = file_info.file_path.split('/')[-1]
        data = await state.get_data()
        file_bytes = await message.bot.download_file(file_info.file_path)

        form = FormData()
        form.add_field('file', file_bytes, filename=file_name, content_type='multipart/form-data')

        try:
            create_mem = await do_request(
                url=f'{settings.MEM_BACKEND_HOST}/mem/upload', data=form, params={'text': data['text']}
            )
            new_mem = await do_request(
                f'{settings.MEM_BACKEND_HOST}/mem/{create_mem["id"]}',
                method='GET',
            )
            photo_url = f'{settings.MEM_BACKEND_HOST}/mem/download/{new_mem["id"]}'

            if mem_info := new_mem:
                access_token = data['access_token']
                await state.clear()
                await state.update_data(access_token=access_token)
                await update_state_with_mem_info(state, [mem_info], navigation=False, add=True)
                await message.answer_photo(
                    photo=photo_url,
                    caption=render('memes/card.jinja2', mem_info=mem_info),
                    reply_markup=get_buttons(mem_info['likes'], mem_info['dislikes'], navigation=False, add=True),
                )
                return
        except ClientResponseError as e:
            logger.error('Ошибка загрузки файла: %s', e)
            await message.answer('Что-то пошло не так 🫣', reply_markup=get_cancel_button())
    else:
        await message.answer('Загрузите фото 🖼️ для продолжения', reply_markup=get_cancel_button())
