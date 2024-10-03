"""
Schemas выносятся в отдельный модуль, т.к. их мы используем в нескольких местах (views.py, crud.py)
"""
from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    # username: str = Field(..., min_length=3, max_length=20)  # старый стиль
    username: Annotated[str, MinLen(3), MaxLen(20)]  # статич. анализатор Mypy способен проверять эти типы
    email: EmailStr
