from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery, FSInputFile
from tg_bot.bot_db import engine, Group
from tg_bot.bot_logger import logger
from tg_bot.keyboards.inline.inline_resident import make_inline_resident_city_kb, make_inline_resident_location_kb, \
    make_inline_resident_group_kb
from tg_bot.keyboards.inline.inline_main import main_inline
from tg_bot.keyboards.inline.inline_back_to_main import back_to_main_inline
from sqlalchemy.orm import Session

router: Router = Router()


# главное меню раздела Contact - присылаем города
@router.callback_query(F.data == 'resident')
async def process_button_resident_press(callback: CallbackQuery):
    logger.info(f'process_button_resident_press:{callback.data}')
    await callback.message.answer(text='Выберите город:',
                                  reply_markup=make_inline_resident_city_kb())
    await callback.message.delete()
    await callback.answer()


# выбираем город - присылаем локации
@router.callback_query(F.data.startswith('resident-city-'))
async def process_button_resident_city_press(callback: CallbackQuery):
    logger.info(f'process_button_resident_city_press:{callback.data}')
    with Session(autoflush=False, bind=engine) as session:
        found_city = session.query(Group).where(Group.c.id == callback.data.split('-')[2]).first()
    await callback.message.answer(text='Выберите локацию:',
                                  reply_markup=make_inline_resident_location_kb(found_city))
    await callback.message.delete()
    await callback.answer()


# выбираем локацию - присылаем список групп
@router.callback_query(F.data.startswith('resident-location-'))
async def process_button_resident_location_press(callback: CallbackQuery):
    logger.info(f'process_button_resident_location_press:{callback.data}')
    with Session(autoflush=False, bind=engine) as session:
        found_location = session.query(Group).where(Group.c.id == callback.data.split('-')[2]).first()
    await callback.message.answer(text=f'Локация: {found_location.location}\nВыберите группу:',
                                  reply_markup=make_inline_resident_group_kb(found_location))
    await callback.answer()
    await callback.message.delete()


# выбираем группу - присылаем список резидентов resident-group-
@router.callback_query(F.data.startswith('resident-group-'))
async def process_button_resident_group_press(callback: CallbackQuery):
    logger.info(f'process_button_resident_group_press:{callback.data}')
    with Session(autoflush=False, bind=engine) as session:
        found_group = session.query(Group).where(Group.c.id == callback.data.split('-')[2]).first()
        result = session.query(Group).where(Group.c.group == found_group.group).all()

    resident_list = ''
    for item in result:
        resident_list += f'{item.FIO}\n'
    await callback.message.answer(text=f'Группа: {found_group.group}\nСписок резидентов:'
                                       f'{resident_list}',
                                  reply_markup=back_to_main_inline)
    await callback.answer()
    await callback.message.delete()
