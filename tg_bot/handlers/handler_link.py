from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery
from sqlalchemy.orm import Session

from tg_bot.bot_db import engine, Partner
from tg_bot.keyboards.inline.inline_link import make_inline_link_kb

router: Router = Router()


# главное меню раздела Link


@router.callback_query(F.data == 'link')
async def process_button_link_press(callback: CallbackQuery):
    await callback.message.answer(text='Ссылки на наши социальные сети:',
                                  reply_markup=make_inline_link_kb())
    await callback.message.delete()
    await callback.answer()












