from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Часто задаваемые вопросы',
    callback_data='FAQ')

button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Состав групп',
    callback_data='button_2_pressed')

button_3: InlineKeyboardButton = InlineKeyboardButton(
    text='Назначить отработку',
    callback_data='button_3_pressed')

button_4: InlineKeyboardButton = InlineKeyboardButton(
    text='Платформа английского Lim English',
    callback_data='button_4_pressed')

button_5: InlineKeyboardButton = InlineKeyboardButton(
    text='Наши Акции',
    callback_data='button_4_pressed')

button_6: InlineKeyboardButton = InlineKeyboardButton(
    text='Наши Партнёры',
    callback_data='button_4_pressed')

button_7: InlineKeyboardButton = InlineKeyboardButton(
    text='Контакты',
    callback_data='button_4_pressed')

button_8: InlineKeyboardButton = InlineKeyboardButton(
    text='Социальные сети',
    callback_data='button_4_pressed')

# Создаем объект inline-клавиатуры
main_inline: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            button_1
        ],
        [
            button_2
        ],
        [
            button_3
        ],
        [
            button_4
        ],
    ]
)
