from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery, FSInputFile

from tg_bot.keyboards.inline.inline_back_to_main import back_to_main_inline

router: Router = Router()


# главное меню раздела english_platform
@router.callback_query(F.data == 'english_platform')
async def process_button_faq_press(callback: CallbackQuery):
    await callback.message.answer(
        text='Lim English – это набор курсов для обучения английскому языку. '
             'Все курсы делятся по уровню сложности и тематике. '
             'Каждый урок может содержать в себе видео, аудирование, словарь, диктант и перевод.\n'
             'Для наших резидентов платформа доступна в виде приятного бонуса!\n'
             'Ниже инструкцию по работе и доступом.\n'
             'P.S. ОЧЕНЬ ПРОСИМ ВАС НЕ ИЗМЕНЯТЬ ПАРОЛЬ И ИСПОЛЬЗОВАТЬ ТОЛЬКО ТОТ, КОТОРЫЙ ПРЕДОСТАВЛЕН В ИНСТРУКЦИИ!!! 🤗\n'
        )
    document = FSInputFile(path='files/Lim_English.pdf', filename='LimEnglish.pdf')
    await callback.message.answer_document(document=document, caption='Инструкция по работе с платформой',
                                           reply_markup=back_to_main_inline)
    await callback.message.delete()
    await callback.answer()
