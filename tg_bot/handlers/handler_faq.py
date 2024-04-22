from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery
from tg_bot.bot_db import engine, FAQ
from tg_bot.keyboards.inline.inline_faq import make_inline_faq_kb
from tg_bot.keyboards.inline.inline_main import main_inline
from sqlalchemy.orm import Session


router: Router = Router()


@router.callback_query(F.data == 'inline_main')
async def process_button_inline_back_to_main(callback: CallbackQuery):
    await callback.message.answer(text='Выберите действие..',
                                  reply_markup=main_inline)
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data == 'FAQ')
async def process_button_faq_press(callback: CallbackQuery):
    await callback.message.answer(text='Часто задаваемые вопросы:',
                                  reply_markup=make_inline_faq_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(F.data.startswith('faq-'))
async def process_button_faq_question_press(callback: CallbackQuery):
    with Session(autoflush=False, bind=engine) as session:
        results = session.query(FAQ).filter(FAQ.c.id == int(callback.data.split('-')[1])).first()
    await callback.message.answer(text=results[2],
                                  reply_markup=make_inline_faq_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query()
async def process_button_any_faq_question_press(callback: CallbackQuery):
    print(callback.data)
    await callback.message.delete()
    await callback.answer()

