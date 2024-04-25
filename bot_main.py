import os
from contextlib import asynccontextmanager

import uvicorn
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from fastapi import FastAPI

from tg_bot.bot_db import database
from tg_bot.bot_logger import logger
from tg_bot.handlers import handler_start, handler_faq, handler_inline_main, handler_promo, handler_partner, \
    handler_link, handler_contact, handler_english_platform, handler_admin, handler_excel_file, handler_resident
from tg_bot.utils.set_commands import set_main_menu

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
DEBUG = os.getenv("DEBUG")
NGROK = os.getenv("NGROK")
DOMAIN = os.getenv("DOMAIN")

WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
if DEBUG:
    WEBHOOK_URL = f"{NGROK}{WEBHOOK_PATH}"
else:
    WEBHOOK_URL = f"{DOMAIN}{WEBHOOK_PATH}"


@asynccontextmanager
async def lifespan(application: FastAPI):
    await database.connect()
    logger.info("Database connection established.")
    load_handlers()
    await bot.delete_webhook(drop_pending_updates=True)
    if DEBUG:
        await dp.start_polling(bot)
    else:
        await bot.set_webhook(WEBHOOK_URL)
    try:
        yield
    finally:
        await database.disconnect()
        logger.info("Database connection closed.")
        await bot.session.close()


app = FastAPI(lifespan=lifespan)
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


def load_handlers() -> None:
    dp.include_routers(
        # пункты меню
        handler_faq.router,
        handler_promo.router,
        handler_partner.router,
        handler_link.router,
        handler_contact.router,
        handler_english_platform.router,
        handler_resident.router,
        # обработка файла
        handler_excel_file.router,
        # обработка админки
        handler_admin.router,
        # обработка старт и др. пользовательских приколов
        handler_start.router,
        # этот хендлер должен быть самым последним иначе последующие хендлеры не сработают
        handler_inline_main.router,
    )
    dp.startup.register(set_main_menu)


@app.get("/")
async def root():
    return "KIBERone"


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)


if __name__ == "__main__":
    if DEBUG == "True":
        uvicorn.run('bot_main:app', host="127.0.0.1", port=8000, reload=True, log_level="debug")
    else:
        uvicorn.run('bot_main:app', host='0.0.0.0', port=8000, log_level="debug")
