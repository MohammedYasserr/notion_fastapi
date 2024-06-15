from fastapi import FastAPI


app = FastAPI()


@app.get("/items/{item_id}")
async def root():
    return {"items": "These are the items"}
