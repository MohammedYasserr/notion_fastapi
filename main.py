from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

class RequestHandler(BaseModel):
    task : str

class User(BaseModel):
    email : str


@app.get("/")
async def root():
    return {"message": "Hello World"}