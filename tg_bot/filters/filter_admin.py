import os
from aiogram import Router
from aiogram.filters import Filter
from aiogram.types import Message
from dotenv import load_dotenv


load_dotenv()
router = Router()


admins_list = [int(admin_id) for admin_id in os.getenv("ADMINS").split(",")]


class AdminFilter(Filter):
    def __init__(self, admin: bool) -> None:
        self.admin = admin

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in admins_list


router.message.filter(AdminFilter)
