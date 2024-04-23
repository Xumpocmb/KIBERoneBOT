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
    """
    Process the callback query for the 'promo' button.

    This function is an asynchronous callback handler for the 'promo' button in a Telegram bot. It is triggered when the user clicks the 'promo' button in the inline keyboard.

    Parameters:
        callback (CallbackQuery): The callback query object representing the user's interaction with the button.

    Returns:
        None

    This function sends a message to the user with the text 'Наши акции:' and displays an inline keyboard with promotions. It then deletes the original message and sends an empty answer to acknowledge the callback query.
    """
    await callback.message.answer(text='Наши акции:',
                                  reply_markup=make_inline_promo_kb())
    await callback.message.delete()
    await callback.answer()


# пункт раздела наши акции
@router.callback_query(F.data.startswith('promo-'))
async def process_button_faq_question_press(callback: CallbackQuery):
    """
    Process the button press for the FAQ questions.

    Parameters:
        callback (CallbackQuery): The callback query object representing the user's interaction with the button.

    Returns:
        None
    """
    with Session(autoflush=False, bind=engine) as session:
        results = session.query(Promotion).filter(Promotion.c.id == int(callback.data.split('-')[1])).first()
    await callback.message.answer(text=results[2],
                                  reply_markup=make_inline_promo_kb())
    await callback.message.delete()
    await callback.answer()


