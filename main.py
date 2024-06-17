from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
import sys
from Validations import schema
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/tasks/" , response_model=list[schema.Task])
async def read_tasks(skip: int = 10, limit: int =10, db: Session= Depends(get_db), token: str= Depends(oauth2_scheme)):
    return {"items": "These are the items"}
