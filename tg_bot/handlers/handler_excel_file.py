import os

import pandas as pd
from aiogram import F
from aiogram import Router
from aiogram.types import Message
from sqlalchemy.orm import Session

from bot_main import bot
from tg_bot.bot_db import engine, Group
from tg_bot.bot_logger import logger
from tg_bot.filters.filter_admin import AdminFilter

router: Router = Router()


@router.message(AdminFilter(admin=True), F.document)
async def get_file_from_user(message: Message):
    logger.info('Получен файл')
    try:
        await message.answer(f'Файл получен. Начинаю обработку!')
        if message.document:
            file_id = message.document.file_id
            file = await bot.get_file(file_id)
            file_path = file.file_path
            await bot.download_file(file_path, 'files/' + message.document.file_name)
            downloaded_file = f'files/{message.document.file_name}'
            if downloaded_file.split('.')[-1] != 'xlsx':
                logger.error('Файл не был принят')
                await message.answer('Файл не был принят! Неверное расширение файла.')
                return
            df = pd.read_excel(downloaded_file)
            print('Начало работы с БД')
            with Session(bind=engine) as session:
                session.execute(Group.delete())
                session.commit()
                session.close()

            with Session(bind=engine) as session:
                for index, row in df.iterrows():
                    group_data = Group.insert().values(
                        FIO=row['ФИО'],
                        city=row['Город'],
                        group=row['Активные группы'],
                        location=row['Локация']
                    )
                    print(f"Row inserted: {index}")
                    session.execute(group_data)
                session.commit()
            os.remove(downloaded_file)
            logger.info('Завершение работы с БД')
            await message.answer('Файл был успешно обработан!')
        else:
            logger.error('Файл не был принят')
        await message.delete()
    except Exception as e:
        logger.error(f'Error processing file: {e}')
