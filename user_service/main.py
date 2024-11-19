from fastapi import FastAPI, HTTPException

app = FastAPI()

# "эмулируем" базу данных
users_db = {
    1: {"id": 1, "name": "Alice"},
    2: {"id": 2, "name": "Bob"},
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users_db.get(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")