from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True  # атрибут указывает, что для данной модели не будут создаваться таблицы

    # declared_attr - свойство, которое будет на уровне класса выполняться как Property
    @declared_attr
    def __tablename__(cls) -> str:
        """Имя таблицы будет создаваться на основе имени класса"""
        return f"{cls.__name__.lower()}s"  # 's' на конце добавляется

    id: Mapped[int] = mapped_column(primary_key=True)  # однотипный id передается в дочерние объекты
