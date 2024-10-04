from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from _04_sqlalchemy.core.models import Base, db_helper

from items_views import router as items_router
from _03_routers.users.views import router as users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Создание новой БД
    async with db_helper.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)  # без скобок (!)
        # function create_all() Create all tables stored in this metadata.
        # Conditional by default, will not attempt to recreate tables
        # already present in the target database.
    yield
    # Здесь мб описать действия для закрытия БД


app = FastAPI(lifespan=lifespan)

# Регистрация роутеров:
app.include_router(items_router)  # prefix="/items-views" - здесь можно добавить еще один префикс
app.include_router(users_router)

# Запускаем создание БД если у нас её еще нет (Fastapi Lifespan events)


@app.get("/")
def hello_index():
    return {
        "message": "hello index",
    }


@app.get("/hello/")
def hello(name: str = "world"):
    name = name.strip().title()
    return {"message": f"Hello, {name}!"}


if __name__ == '__main__':
    uvicorn.run(app)
