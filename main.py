import asyncio
import logging
import random

import orjson
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis
from aiogram.fsm.state import StatesGroup, State

from os import getenv
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=getenv('token_tg'))

redis = Redis(
    host='localhost',
    port=6379,
    db=1,
)

storage = RedisStorage(redis)
dp = Dispatcher(storage=storage)


class SaveCommon(StatesGroup):
    first_state = State()
    second_state = State()


@dp.message(SaveCommon.first_state)
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(SaveCommon.second_state)

    print(await state.get_state())

    await message.answer("Hello first state!")


@dp.message(SaveCommon.second_state)
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(SaveCommon.first_state)
    await message.answer("Hello second state!")


@dp.message(Command("start",))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(SaveCommon.first_state)
    await message.answer("Hello without state!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())