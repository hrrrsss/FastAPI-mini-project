from fastapi import FastAPI
from fastapi.responses import Response # Формирует ответ

# Инициализация FastAPI приложения
app = FastAPI()


@app.get("/health")
def health_check():
    return Response(status_code=200)