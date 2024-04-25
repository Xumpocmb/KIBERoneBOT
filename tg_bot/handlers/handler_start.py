from time import sleep
from aiogram import Router
from aiogram.filters import Command
from tg_bot.filters.filter_admin import AdminFilter
from aiogram.types import Message


from tg_bot.keyboards.inline.inline_main import main_inline

router: Router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f'Hello, {message.from_user.username}!', reply_markup=main_inline)
    await message.delete()


@router.message()
async def echo(message: Message):
    await message.answer(f'echo: {message.text}')

