from fastapi import FastAPI
import sys
from Validations import schema

app = FastAPI()


@app.get("/tasks/" , response_model=list[schema.Task])
async def read_tasks(ski):
    return {"items": "These are the items"}
