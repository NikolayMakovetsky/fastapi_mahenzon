# from sqlalchemy import create_engine  # это обычный синхронный движок
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from _04_sqlalchemy.core.settings import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        """
        Переедаем параметры в __init__, чтобы можно было подключаться к разным БД,
        либо к одной БД, но с разным логином и паролем
        Теперь важно при создании экземпляра DatabaseHelper передать нужные параметры!
        """
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        #  сессия будет создаваться "на ходу"
        self.session_factory = async_sessionmaker(
            bind=self.engine,  #  An optional Engine or Connection to which this Session should be bound.
            autoflush=False,  # When True, all query operations will issue a Session.flush() call to this Session before proceeding
            autocommit=False,  # the “autocommit” keyword is present for backwards compatibility but must remain at its default value of False.
            expire_on_commit=False,  # Defaults to True. When True, all instances will be fully expired after each commit()
        )


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo
)
