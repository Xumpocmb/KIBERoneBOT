from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery
from tg_bot.bot_db import engine, FAQ
from tg_bot.keyboards.inline.inline_faq import make_inline_faq_kb
from tg_bot.keyboards.inline.inline_main import main_inline
from sqlalchemy.orm import Session


router: Router = Router()


# главное меню раздела FAQ
@router.callback_query(F.data == 'FAQ')
async def process_button_faq_press(callback: CallbackQuery):
    await callback.message.answer(text='Часто задаваемые вопросы:',
                                  reply_markup=make_inline_faq_kb())
    await callback.message.delete()
    await callback.answer()


# пункт раздела FAQ
@router.callback_query(F.data.startswith('faq-'))
async def process_button_faq_question_press(callback: CallbackQuery):
    with Session(autoflush=False, bind=engine) as session:
        results = session.query(FAQ).filter(FAQ.c.id == int(callback.data.split('-')[1])).first()
    await callback.message.answer(text=results[2],
                                  reply_markup=make_inline_faq_kb())
    await callback.message.delete()
    await callback.answer()


