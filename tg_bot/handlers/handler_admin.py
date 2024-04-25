from time import sleep
from aiogram import Router
from aiogram.filters import Command
from tg_bot.filters.filter_admin import AdminFilter
from aiogram.types import Message
import os
from tg_bot.bot_logger import logger
import pandas as pd
from aiogram import F
from aiogram import Router
from aiogram.types import Message
from sqlalchemy.orm import Session
from tg_bot.bot_db import engine, Group
from tg_bot.filters.filter_admin import AdminFilter


from tg_bot.keyboards.inline.inline_main import main_inline

router: Router = Router()


@router.message(AdminFilter(admin=True), Command("start"))
async def cmd_start(message: Message):
    logger.info('команда старт админ хендлер')
    await message.answer(f'Hello admin, {message.from_user.username}!', reply_markup=main_inline)
    await message.delete()



