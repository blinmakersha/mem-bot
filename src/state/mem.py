from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class CreateMemState(StatesGroup):
    text = State()
    photo = State()


class MemesState(StatesGroup):
    mem = State()


async def update_state_with_mem_info(state: FSMContext, mem_info: dict, navigation: bool, add: bool) -> None:
    await state.update_data(
        memes=mem_info,
        current_index=0,
        navigation=navigation,
        add=add,
    )
