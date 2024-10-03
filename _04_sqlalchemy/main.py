import uvicorn
from fastapi import FastAPI  # Path необходим, чтобы дополнять параметры пути

from items_views import router as items_router
from _03_routers.users.views import router as users_router

app = FastAPI()

# Регистрация роутеров:
app.include_router(items_router)  # prefix="/items-views" - здесь можно добавить еще один префикс
app.include_router(users_router)


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
