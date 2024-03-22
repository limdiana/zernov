from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 3, "name": "Mary"}
]

logedin_user = 1

@app.get('/')
async def root():
    return {"message": "hello world"}

@app.get('/users')
async def get_users():
    """
    get the list of users
    """
    return {"users": users}

@app.get('/users/me')
async def get_users_me():
    for u in users:
        if u['id'] == logedin_user:
            return u

@app.get('/users/{user_id}')
async def get_user_by_id(user_id: int):
    for u in users:
        if u['id'] == user_id:
            return u
        

@app.get('/calc')
async def calc(op1: float = None, op2: float = None, meaning: str = None):
    result = 0

    if (meaning == '/' and op2 == 0) or (op1 is None) or (op2 is None) or (meaning is None):
        return {'ошибка': 'введите верное значение'}
  
    if meaning == '+':
        result = op1 + op2
    elif meaning == '-':
        result = op1 - op2
    elif meaning == '*':
        result = op1 * op2
    elif meaning == '/':
        result = op1 / op2
    
    return {'ответ': result}



