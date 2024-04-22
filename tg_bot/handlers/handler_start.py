from time import sleep
from aiogram import Router
from aiogram.filters import Command
from tg_bot.filters.filter_admin import AdminFilter
from aiogram.types import Message

from tg_bot.keyboards import main_menu

router: Router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f'Hello admin, {message.from_user.username}!', reply_markup=main_menu.keyboard)


@router.message(Command("start"))
@router.message(AdminFilter)
async def cmd_start(message: Message):
    await message.answer(f'Hello, {message.from_user.username}!', reply_markup=main_menu.keyboard)


@router.message()
async def echo(message: Message):
    await message.answer(f'Hello')

