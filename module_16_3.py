from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
# python -m uvicorn module_16_3:app

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                  example='UrbanUser')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(min_length=1, max_length=3, regex="^[0-9]",
                                                   description='Enter id', example='2')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                  example='UrbanUser')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='25')]) -> str:
    for user_key in users.keys():
        if user_key == user_id:
            users[user_id] = f"Имя: {username}, возраст: {age}"
            return f"The user {user_id} is updated"
    return f"User with {user_id} not found"

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(min_length=1, max_length=3, regex="^[0-9]",
                                                   description='Enter id', example='2')]) -> str:
    for user_key in users.keys():
        if user_key == user_id:
            users.pop(user_id)
            return f'{user_id} deleted'
    return f"User with {user_id} not found"



