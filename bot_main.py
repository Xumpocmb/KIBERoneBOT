import os
from contextlib import asynccontextmanager

import uvicorn
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from fastapi import FastAPI

from tg_bot.bot_db import database
from tg_bot.bot_logger import logger
from tg_bot.handlers import handler_start, handler_faq, handler_inline_main, handler_promo, handler_partner, \
    handler_link, handler_contact
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
    dp.include_router(handler_start.router)
    dp.include_router(handler_faq.router)
    dp.include_router(handler_promo.router)
    dp.include_router(handler_partner.router)
    dp.include_router(handler_link.router)
    dp.include_router(handler_contact.router)
    dp.include_router(handler_inline_main.router)
    dp.startup.register(set_main_menu)
    await bot.delete_webhook(drop_pending_updates=True)
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
