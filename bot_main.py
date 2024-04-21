import os
from contextlib import asynccontextmanager, contextmanager
from fastapi import FastAPI
import uvicorn
from tg_bot.bot_db import database
from tg_bot.bot_logger import logger
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from tg_bot.handlers import handler_start
from tg_bot.utils.set_commands import set_main_menu


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
DEBUG = os.getenv("DEBUG")
NGROK = os.getenv("NGROK")
DOMAIN = os.getenv("DOMAIN")


@asynccontextmanager
async def lifespan(application: FastAPI):
    await database.connect()
    logger.info("Database connection established.")
    dp.include_router(handler_start.router)
    dp.startup.register(set_main_menu)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
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


if __name__ == "__main__":
    if DEBUG == "True":
        uvicorn.run('bot_main:app', host="127.0.0.1", port=8000, reload=True, log_level="debug")
    else:
        uvicorn.run('bot_main:app', host='0.0.0.0', port=8000, log_level="debug")

