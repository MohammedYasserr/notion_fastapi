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
from typing import Annotated
from Validations import schema

app = FastAPI()
models.Base.metadata.create_all(bind=engine) 


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

# @app.post('/task')
# async def create_task(task:schema.TaskBase):
    
    