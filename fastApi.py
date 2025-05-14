from fastapi import FastAPI

app = FastAPI()

username = "Matoki!"
item_id = "1"
v = "bla"
@app.get("/items/{item_id}")
def read_user(item: str):
    return {"item": item, "message": "Hello from FastAPI!"}


@app.get("/user/{{username}}")
def read_user(username: str):
    return {"username": username, "message": "Hello from FastAPI!"}


@app.get("f'/{v}/api/create'")
def create():
    pass


@app.post(f"/items/{{item_id}}")
def add_item():
    pass


MY_CONST = "/api/v1"
@app.post(f'{MY_CONST}/items/{{item_id}}')
def create_item():
    pass



