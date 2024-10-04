"""
РАБОТА С ПЕРЕМЕННЫМИ ОКРУЖЕНИЯ
Используй Pydantic Settings
(Fastapi -> Advanced User Guide -> Settings and Environment Variables)

In many cases your application could need some external settings or configurations,
for example secret keys, database credentials, credentials for email services, etc.

Most of these settings are variable (can change), like database URLs.
And many could be sensitive, like secrets.

For this reason it's common to provide them in environment variables that are read by the application.
"""
from pydantic_settings import BaseSettings
from pathlib import Path  # pathlib - работа с путями ОС как с объектами классов

# Базовая директория, в которой находится наш проект
BASE_DIR = Path(__file__).parent.parent  # _04_sqlalchemy

class Settings(BaseSettings):
    """
    Данный класс мы будем использовать для считывания переменных окружения,
    либо для чтения файла .env, в котором будет хранится список таких переменных
    """
    # db_url: str = "sqlite+aiosqlite:///./db.sqlite3"  # относительный путь
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/minishop.db"  # абсолютный путь
    db_echo: bool = True  # только для отладки
    # db_echo: bool = False  # для продакшена

settings = Settings()
