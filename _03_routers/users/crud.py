"""
Create
Read
Update
Delete
"""
from _03_routers.users.schemas import CreateUser

def create_user(user_in: CreateUser) -> dict:
    user = user_in.model_dump()  # /в pydantic_v1 был метод .dict/ Делаем словарь из JSON-данных
    return {
        "success": True,
        "user": user,
    }
