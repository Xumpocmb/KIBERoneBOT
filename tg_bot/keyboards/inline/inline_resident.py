from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from sqlalchemy.orm import Session
from tg_bot.bot_db import engine, Group


def make_inline_resident_city_kb() -> InlineKeyboardMarkup:
    buttons = []
    with Session(autoflush=False, bind=engine) as session:
        results = session.query(Group).group_by(Group.c.city)
        for item in results:
            buttons.append(InlineKeyboardButton(text=item[2], callback_data=f'resident-city-{str(item[0])}'))
    buttons.append(InlineKeyboardButton(text='<< Назад', callback_data='inline_main'))
    buttons = [[button] for button in buttons]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                    input_field_placeholder="Выберите действие..")
    return keyboard


def make_inline_resident_location_kb(found_city) -> InlineKeyboardMarkup:
    buttons = []
    with Session(autoflush=False, bind=engine) as session:
        results = session.query(Group).where(Group.c.city == found_city.city).group_by(Group.c.location)
    for item in results:
        buttons.append(InlineKeyboardButton(text=item[4], callback_data=f'resident-location-{str(item[0])}'))
    buttons.append(InlineKeyboardButton(text='<< Назад', callback_data='inline_main'))
    buttons = [[button] for button in buttons]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                    input_field_placeholder="Выберите действие..")
    return keyboard


def make_inline_resident_group_kb(found_location) -> InlineKeyboardMarkup:
    print(found_location.id)
    buttons = []
    with Session(autoflush=False, bind=engine) as session:
        results = session.query(Group).where(Group.c.location == found_location.location).group_by(Group.c.group)
    for item in results:
        buttons.append(InlineKeyboardButton(text=str(item[3]).strip(), callback_data=f'resident-group-{str(item[0])}-{found_location.id}'))
    buttons.append(InlineKeyboardButton(text='<< Назад', callback_data='inline_main'))
    buttons = [[button] for button in buttons]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                    input_field_placeholder="Выберите действие..")
    return keyboard
