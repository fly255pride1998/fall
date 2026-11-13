from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Подключаем текущую папку, чтобы сервер мог отдавать клиенту HTML и картинки
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def read_index():
    # При заходе на сайт сервер отправляет твой index.html
    return FileResponse("index.html")

@app.get("/api/status")
def get_status():
    # Пример тестового API-запроса от игры к серверу
    return {"status": "online", "message": "Сервер Madness RPG работает!"}