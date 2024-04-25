from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery

from tg_bot.bot_logger import logger
from tg_bot.keyboards.inline.inline_main import main_inline

router: Router = Router()


# присылает главное inline меню
@router.callback_query(F.data == 'inline_main')
async def process_button_inline_back_to_main(callback: CallbackQuery):
    await callback.message.answer(text='Выберите действие..',
                                  reply_markup=main_inline)
    await callback.message.delete()
    await callback.answer()


# отвечает на любой call-back для теста
@router.callback_query()
async def process_button_any_faq_question_press(callback: CallbackQuery):
    logger.info(f'Callback: {callback.data}')
    await callback.message.delete()
    await callback.answer()
