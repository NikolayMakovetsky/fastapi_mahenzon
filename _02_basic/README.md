## Fastapi lesson 1 (basic)

В этом уроке:

- Рассмотрим основы fastapi
- Научимся создавать простое web-приложение
- Найчимся работать с документацией fastapi

### Факты о fastapi

1. Выдаёт ответы в JSON-формате
2. Активно использует аннотации типов Python
3. При создании приложения необходимо сразу определиться какой тип слэша использовать у эндпоинтов(открытый или
   закрытый). Если у вас есть ручка ```"/items/"```, но user отправит запрос на ```"/items"```, Fastapi автоматически
   доставит ```"/"``` в конце и откроет доступ к ручке.
4. ВАЖНО использовать порядок регистрации путей от частного к общему (чтобы ручки не конфликтовали друг с другом)

### Передача параметров

#### Передача параметров в адресной строке (PATH parameter)
```http://127.0.0.1:8000/items/latest/```
#### Передача параметров в строке параметров (через '?') // Query string parameters
```http://127.0.0.1:8000/items/latest/?name=foobar```
#### Передача параметров в теле запроса
```
from fastapi import Body

@app.post("/users/")
def create_user(email: EmailStr = Body()):
...
```
Именно ```Body()```, а не декоратор ```@app.post``` даст понять Fastapi, что мы хотим передавать параметр ```email``` в теле запроса. 

Для этой же цели вместо ```Body()``` можно использовать пользовательский класс, наследуемый от ```BaseModel```

### Как получать email В ТЕЛЕ не в виде строки, а в виде JSON-объекта?
Для этого необходимо использовать pydantic-объекты, созданные от дочернего BaseModel классу
```
from pydantic import BaseModel

class CreateUser(BaseModel):
    email: EmailStr

@app.post("/users2/")
def create_user(user: CreateUser):
```

### Команды

#### Запуск приложения fastapi в терминале

```uvicorn main:app```

```INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)```

#### Открыть панель разработчика в Chrome и проанализировать запрос

```F12 или RightMouseClick -> Inspect -> Network```

```commandline
Request URL: http://127.0.0.1:8000/
Request Method: GET
Status Code: 200 OK
Remote Address: 127.0.0.1:8000
Referrer Policy: strict-origin-when-cross-origin
content-length: 25
content-type: application/json
date: Wed, 02 Oct 2024 08:02:10 GMT
server: uvicorn
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
accept-encoding: gzip, deflate, br, zstd
accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
connection: keep-alive
host: 127.0.0.1:8000
sec-ch-ua: "Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36
```

```commandline
Request URL: http://127.0.0.1:8000/hello
Request Method: GET
Status Code: 404 Not Found
Remote Address: 127.0.0.1:8000
Referrer Policy: strict-origin-when-cross-origin
content-length: 22
content-type: application/json !!! JSON !!!
...
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36
```

#### Открыть автоматическую документацию fastapi

```http://127.0.0.1:8000/redoc```

#### Открыть интерактивную документацию fastapi (SWAGGER)

```http://127.0.0.1:8000/docs```

#### Как запустить приложение без терминала

```
import uvicorn

if __name__ == '__main__':
    uvicorn.run(app)
```

#### Как запустить приложение с автоматическим перезапуском

(Решил отказаться от этого способа, т.к. на моей машине перезапуск происходит достаточно долго)

```
import uvicorn

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
```

```commandline
INFO:     Will watch for changes in these directories: ['C:\\DISK_D\\_19_fastapi_mahenzon\\_02_basic']
```

#### Как в обход SWAGGER-а проверить, что ручка "падает" ?

Отправить запрос в обычной адресной строке браузера. Мы получаем ответ с подробным описанием ошибки, и даже со ссылкой
на документацию

```http://127.0.0.1:8000/items/qwerty/```

```commandline
{"detail":
    [
        {
        "type":"int_parsing",
        "loc":["path","item_id"],
        "msg":"Input should be a valid integer, unable to parse string as an integer",
        "input":"qwerty",
        "url":"https://errors.pydantic.dev/2.0.3/v/int_parsing"
        }
    ]
}
```

```commandline
Request URL: http://127.0.0.1:8000/items/qwerty/
Request Method: GET
Status Code: 422 Unprocessable Entity (НЕВОЗМОЖНО ОБРАБОТАТЬ ПЕРЕДАННЫЙ ПАРАМЕТР)
...
```
#### Как подключить валидацию EmailStr от pydantic?
```
pip install pydantic
pip install "pydantic[email]"
```

#### Как в Pycharm подключить плагин для подсказок при работе с pydantic?
```
Double Shift -> Search:Plugins -> Pydantic -> Install
OR
File -> Settings -> Plugins -> Pydantic -> Install
```




### Vocab

Required field is not provided / Требуемое поле не заполнено