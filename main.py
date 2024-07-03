from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError,jwt
from typing import List 
from sqlalchemy.orm import Session
import datetime
from pydantic import BaseModel

import Models
from Validations import schema

from databases import engine,sessionLocal
import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)





@app.get("/tasks/" , response_model=list[schema.Task])
async def read_tasks(skip: int = 10, limit: int =10, db: Session= Depends(get_db), token: str= Depends(oauth2_scheme)):
    return {"items": "These are the items"}
