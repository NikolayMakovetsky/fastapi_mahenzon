from .base import Base
from sqlalchemy.orm import Mapped


class Product(Base):
    # __tablename__ = "products"  # в Base описали функцию def __tablename__(cls) -> str:

    name: Mapped[str]  # Mapped обозначает что это колонка
    description: Mapped[str]
    price: Mapped[int]
