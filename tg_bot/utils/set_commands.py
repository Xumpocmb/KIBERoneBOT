from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Начало работы/Перезапуск'),
        BotCommand(command='/help',
                   description='Справка по работе бота'),]
    await bot.set_my_commands(main_menu_commands, scope=BotCommandScopeDefault())
