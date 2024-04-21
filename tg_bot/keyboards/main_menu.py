from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Кнопка 🦮')
button_2: KeyboardButton = KeyboardButton(text='Кнопка 🥒')
button_3: KeyboardButton = KeyboardButton(text='Кнопка ⛅️')
button_4: KeyboardButton = KeyboardButton(text='Кнопка 💰')
button_5: KeyboardButton = KeyboardButton(text='Кнопка 👤')
button_6: KeyboardButton = KeyboardButton(text='Кнопка 6')
button_7: KeyboardButton = KeyboardButton(text='Кнопка 7')
button_8: KeyboardButton = KeyboardButton(text='Кнопка 8')
button_9: KeyboardButton = KeyboardButton(text='/menu_inline')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[
        [
            button_1, button_2, button_3
        ],
        [
            button_4, button_5, button_6
        ],
        [
            button_7, button_8, button_9
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие..'
    # one_time_keyboard=True - свернет клавиатуру после использования
)
