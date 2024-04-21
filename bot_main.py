import os
from contextlib import asynccontextmanager, contextmanager
from fastapi import FastAPI
import uvicorn
from tg_bot.bot_db import database
from tg_bot.bot_logger import logger
from dotenv import load_dotenv


load_dotenv()


@asynccontextmanager
async def lifespan(application: FastAPI):
    await database.connect()
    logger.info("Database connection established.")
    try:
        yield
    finally:
        await database.disconnect()
        logger.info("Database connection closed.")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return "KIBERone"


if __name__ == "__main__":
    try:
        if os.getenv("DEBUG") == "True":
            logger.info("Running in debug mode.")
            uvicorn.run("bot_main:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")
        else:
            uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
    except (KeyboardInterrupt, SystemExit):
        logger.info("Shutting down...")
