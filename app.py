from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"result": "hello fastapi"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param:str=None):
    return {"item_id": item_id, "query_param": query_param}
