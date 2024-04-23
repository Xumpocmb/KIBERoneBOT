from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery
from sqlalchemy.orm import Session

from tg_bot.bot_db import engine, Manager
from tg_bot.keyboards.inline.inline_contact import make_inline_contact_city_kb, make_inline_contact_location_kb
from tg_bot.keyboards.inline.inline_back_to_main import back_to_main_inline

router: Router = Router()


# главное меню раздела Contact - присылаем города
@router.callback_query(F.data == 'contact')
async def process_button_faq_press(callback: CallbackQuery):
    await callback.message.answer(text='Выберите город:',
                                  reply_markup=make_inline_contact_city_kb())
    await callback.message.delete()
    await callback.answer()


# выбираем город - присылаем локации
@router.callback_query(F.data.startswith('contact-city-'))
async def process_button_faq_question_press(callback: CallbackQuery):
    with Session(autoflush=False, bind=engine) as session:
        found_city = session.query(Manager).where(Manager.c.id == callback.data.split('-')[2]).first()
    await callback.message.answer(text='Выберите локацию:',
                                  reply_markup=make_inline_contact_location_kb(found_city))
    await callback.message.delete()
    await callback.answer()


# выбираем локацию - присылаем контакт
@router.callback_query(F.data.startswith('contact-location-'))
async def process_button_faq_question_press(callback: CallbackQuery):
    with Session(autoflush=False, bind=engine) as session:
        result = session.query(Manager).where(Manager.c.id == callback.data.split('-')[2]).first()
    await callback.message.answer(text=f'{result[3]}\n{result[4]}', reply_markup=back_to_main_inline)
    await callback.message.delete()
    await callback.answer()




