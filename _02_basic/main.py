from fastapi import FastAPI

app = FastAPI()

def hello_index():
    return {
        "message": "hello index",
    }