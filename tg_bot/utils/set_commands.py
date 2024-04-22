from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Начало работы/Перезапуск'),
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи')]

    await bot.set_my_commands(main_menu_commands)
