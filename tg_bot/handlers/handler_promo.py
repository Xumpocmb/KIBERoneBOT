from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery
from sqlalchemy.orm import Session

from tg_bot.bot_db import engine, Promotion
from tg_bot.keyboards.inline.inline_promo import make_inline_promo_kb

router: Router = Router()


# главное меню раздела Promo
@router.callback_query(F.data == 'promo')
async def process_button_faq_press(callback: CallbackQuery):
    await callback.message.answer(text='Наши акции:',
                                  reply_markup=make_inline_promo_kb())
    await callback.message.delete()
    await callback.answer()


# пункт раздела наши акции
@router.callback_query(F.data.startswith('promo-'))
async def process_button_faq_question_press(callback: CallbackQuery):
    with Session(autoflush=False, bind=engine) as session:
        results = session.query(Promotion).filter(Promotion.c.id == int(callback.data.split('-')[1])).first()
    await callback.message.answer(text=results[2],
                                  reply_markup=make_inline_promo_kb())
    await callback.message.delete()
    await callback.answer()


