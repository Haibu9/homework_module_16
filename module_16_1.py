from fastapi import FastAPI

app = FastAPI()
# python -m uvicorn module_16_1:app

@app.get("/")
async def main_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_entry():
    return "Вы вошли как администратор"

@app.get("/user")
async def id_paginator(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get("/user/{user_id}")
async def id_entry(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"



