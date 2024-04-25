from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from sqlalchemy.orm import Session
from tg_bot.bot_db import engine, Manager


# присылаем города
def make_inline_contact_city_kb() -> InlineKeyboardMarkup:
    buttons = []
    with Session(autoflush=False, bind=engine) as session:
        results = session.query(Manager).group_by(Manager.c.city)
        for item in results:
            buttons.append(InlineKeyboardButton(text=item[1], callback_data=f'contact-city-{str(item[0])}'))
    buttons.append(InlineKeyboardButton(text='<< Назад', callback_data='inline_main'))
    buttons = [[button] for button in buttons]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                    input_field_placeholder="Выберите действие..")
    return keyboard


# присылаем локации
def make_inline_contact_location_kb(found_city) -> InlineKeyboardMarkup:
    buttons = []
    with Session(autoflush=False, bind=engine) as session:
        results = session.query(Manager).where(Manager.c.city == found_city.city)
    for item in results:
        buttons.append(InlineKeyboardButton(text=item[2], callback_data=f'contact-location-{str(item[0])}'))
    buttons.append(InlineKeyboardButton(text='<< Назад', callback_data='inline_main'))
    buttons = [[button] for button in buttons]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                    input_field_placeholder="Выберите действие..")
    return keyboard
