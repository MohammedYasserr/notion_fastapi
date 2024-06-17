from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError,jwt
from typing import List 
from sqlalchemy.orm import Session
import datetime


import Models
from Validations import schema


app = FastAPI()


@app.get("/tasks/" , response_model=list[schema.Task])
async def read_tasks(skip: int = 10, limit: int =10, db: Session= Depends(get_db), token: str= Depends(oauth2_scheme)):
    return {"items": "These are the items"}
