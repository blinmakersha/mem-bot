import asyncio

from aiogram import types
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext

from src.handlers.login.router import login_router
from src.logger import logger
from src.state.login import LoginState


@login_router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    username = message.from_user.username
    user_id = message.from_user.id
    logger.info('User: %s, %s start bot', username, user_id)

    await message.answer('🙋🏽 Привет! Для того чтобы начать пользоваться ботом, нужно ввести уникальный код.')
    await asyncio.sleep(0.6)
    await message.answer('Если мы не найдем совпадений, то создадим новую учетную запись.')
    await asyncio.sleep(0.6)
    await state.set_state(LoginState.enter_code)

    return await message.answer('Ваш уникальный код: ')
