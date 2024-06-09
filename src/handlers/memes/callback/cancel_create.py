from aiogram import F, types
from aiogram.fsm.context import FSMContext

from src.handlers.memes.router import memes_router


@memes_router.callback_query(F.data == 'cancel_creation')
async def cancel_creation_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    current_data = await state.get_data()
    access_token = current_data.get('access_token')

    if access_token:
        current_data['access_token'] = access_token

    await state.update_data(**current_data)
    await state.clear()
    await state.update_data(access_token=access_token)

    await callback.message.edit_text('Создание мема отменено ❌')
    await callback.answer()
