from pydantic import BaseModel
import databases
import sqlalchemy


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

# Создаем таблицы
metadata.create_all(engine)


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
