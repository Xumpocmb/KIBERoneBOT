from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
)
from sqlalchemy.orm import Session
from tg_bot.bot_db import engine, Partner


def make_inline_partner_kb() -> InlineKeyboardMarkup:
    buttons = []
    with Session(autoflush=False, bind=engine) as session:
        results = session.query(Partner).all()
        for item in results:
            buttons.append(InlineKeyboardButton(text=item[1], callback_data=f'partner-{str(item[0])}'))
    buttons.append(InlineKeyboardButton(text='<< Назад', callback_data='inline_main'))
    buttons = [[button] for button in buttons]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True,
                                    input_field_placeholder="Выберите действие..")
    return keyboard


