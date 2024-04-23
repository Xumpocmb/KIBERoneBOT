from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery
from sqlalchemy.orm import Session

from tg_bot.bot_db import engine, Partner
from tg_bot.keyboards.inline.inline_partner import make_inline_partner_kb

router: Router = Router()


# главное меню раздела Partner
@router.callback_query(F.data == 'partner')
async def process_button_faq_press(callback: CallbackQuery):
    await callback.message.answer(text='Наши партнеры:',
                                  reply_markup=make_inline_partner_kb())
    await callback.message.delete()
    await callback.answer()


# пункт раздела наши партнеры
@router.callback_query(F.data.startswith('partner-'))
async def process_button_faq_question_press(callback: CallbackQuery):
    """
    Process the button press for the FAQ questions.

    Parameters:
        callback (CallbackQuery): The callback query object representing the user's interaction with the button.

    Returns:
        None
    """
    with Session(autoflush=False, bind=engine) as session:
        results = session.query(Partner).filter(Partner.c.id == int(callback.data.split('-')[1])).first()
    await callback.message.answer(text=results[2],
                                  reply_markup=make_inline_partner_kb())
    await callback.message.delete()
    await callback.answer()
