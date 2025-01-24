from fastapi import FastAPI, Path, HTTPException, Body
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()
# python -m uvicorn module_16_3:app

# users = {'1': 'Имя: Example, возраст: 18'}

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get('/users')
async def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                  example='UrbanUser')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> User:
    if len(users):
        max_id = 1
        for user in users:
            if user.id > max_id:
                max_id = user.id
        user_id = max_id + 1
    else:
        user_id = 1
    new_user = User(username=username, age=age, id=user_id)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(min_length=1, max_length=3, regex="^[0-9]",
                                                   description='Enter id', example='2')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                  example='UrbanUser')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='25')]) -> User:
    for user in users:
        if user.id == int(user_id):
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(min_length=1, max_length=3, regex="^[0-9]",
                                                   description='Enter id', example='2')]) -> User:
    for user in users:
        if user.id == int(user_id):
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")



