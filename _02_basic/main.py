from enum import Enum

import uvicorn
from fastapi import FastAPI, Body
from pydantic import EmailStr, BaseModel

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


class CalcBody(BaseModel):
    comment: str = "text by default"


class Sign(str, Enum):
    plus = "+"
    minus = "-"
    multiply = "*"
    divide = "/"


@app.get("/")
def hello_index():
    return {
        "message": "hello index",
    }


@app.get("/hello/")
def hello(name: str = "world"):  # важно указать значение по умолчанию для Query String Parameter
    name = name.strip().title()
    return {"message": f"Hello, {name}!"}


@app.post("/users/")
def create_user(email: EmailStr = Body()):
    # используем специальную аннотацию pydantic.EmailStr, чтобы проверять email на валидность
    # используем значение по-умолчанию fastapi.Body(), чтобы явно указать, что параметр необходимо
    # передавать именно в теле запроса (иначе email будет передаваться как Query String Parameter)
    return {
        "message": "success",
        "email": email,
        "None_str": None,
    }


@app.post("/users2/")
def create_user(user: CreateUser):
    # используем class CreateUser(BaseModel) вместо Body(), что решает задачу более элегантно
    return {
        "message": "success",
        "email": user.email,
        "None_str": None,
    }


# Пример запроса, включающего: Path parameter, Query parameter and Body parameter
# Path-параметр имеет ограничение, благодаря совместной работе Enum и FastApi
@app.post("/calc1/{sign}/")
def get_result(a: int, b: int, sign: Sign, comment: str = Body()):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    return {
        "a": a,
        "b": b,
        "res": operations.get(sign)(a, b),
        "comment": comment,
    }


# Пример запроса, включающего: Path parameter, Query parameter and Body parameter
# Использование class CalcBody(BaseModel) позволяет задать значение 'comment' по-умолчанию
@app.post("/calc2/{sign}/")
def get_result(a: int, b: int, sign: Sign, calc_body: CalcBody):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    return {
        "a": a,
        "b": b,
        "res": operations.get(sign)(a, b),
        "comment": calc_body.comment,
    }


@app.get("/items/")
def list_items():
    return {
        "item_901",
        "item_902",
        "item_903",
    }


@app.get("/items/latest/")  # частный случай {item_id} важно располагать ВЫШЕ по коду
def get_latest_item():
    return {"item": {"id": 0, "name": "latest"}}


@app.get("/items/{item_id}/")  # общий случай {item_id} важно располагать НИЖЕ по коду
def get_item_by_id(item_id: int):
    return {
        "id": item_id
    }


if __name__ == '__main__':
    uvicorn.run(app)
