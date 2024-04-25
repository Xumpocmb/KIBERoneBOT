from pydantic import BaseModel
import databases
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Настройки базы данных
DATABASE_URL = "sqlite:///DB_KIBERoneBOT.sqlite3"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создаем таблицы
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("tg_id", sqlalchemy.String(128)),
    sqlalchemy.Column("f_name", sqlalchemy.String(128)),
    sqlalchemy.Column("l_name", sqlalchemy.String(128)),
    sqlalchemy.Column("phone", sqlalchemy.String(128)),
    sqlalchemy.Column("username", sqlalchemy.String(128)),
)

FAQ = sqlalchemy.Table(
    "FAQ",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("question", sqlalchemy.String(128)),
    sqlalchemy.Column("answer", sqlalchemy.String(1280)),
)

Promotion = sqlalchemy.Table(
    "Promotion",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("question", sqlalchemy.String(128)),
    sqlalchemy.Column("answer", sqlalchemy.String(1280)),
)

Partner = sqlalchemy.Table(
    "Partner",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("partner", sqlalchemy.String(128)),
    sqlalchemy.Column("description", sqlalchemy.String(1280)),
)


Contact = sqlalchemy.Table(
    "Contact",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("Contact", sqlalchemy.String(128)),
    sqlalchemy.Column("Contact_link", sqlalchemy.String(1280)),
)

Link = sqlalchemy.Table(
    "Link",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("link_name", sqlalchemy.String(128)),
    sqlalchemy.Column("link_url", sqlalchemy.String(1280)),
)


Manager = sqlalchemy.Table(
    "Manager",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("city", sqlalchemy.String(128)),
    sqlalchemy.Column("location", sqlalchemy.String(1280)),
    sqlalchemy.Column("manager", sqlalchemy.String(1280)),
    sqlalchemy.Column("link", sqlalchemy.String(1280)),
)


Group = sqlalchemy.Table(
    "groups",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("FIO", sqlalchemy.String(128)),
    sqlalchemy.Column("city", sqlalchemy.String(1280)),
    sqlalchemy.Column("group", sqlalchemy.String(1280)),
    sqlalchemy.Column("location", sqlalchemy.String(1280)),
)


# Создаем таблицы
metadata.create_all(engine)


# Модели
class UserModel(BaseModel):
    """модель нужна для создания пользователя"""
    tg_id: str
    f_name: str
    l_name: str
    phone: str
    username: str


class User(BaseModel):
    """модель нужна для возврата данных о пользователе из БД клиенту"""
    id: int
    tg_id: str
    f_name: str
    l_name: str
    phone: str
    username: str
