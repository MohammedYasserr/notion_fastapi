from pydantic import BaseModel,EmailStr
from typing import List, Optional
from datetime import datetime




"""
The Below Pydantic Validation Classes are for User creation validation.
"""
class UserBase(BaseModel):
    username : str
    email : EmailStr
    

class UserCreate(UserBase):
    password:str


class User(UserBase):
    id : int
    created_at : datetime.datetime
    
    class Config : 
        orm_mode: True
        
class Token(BaseModel):
    access_token : str
    token_type : str
    
class TokenData(BaseModel):
    username : Optional[str] = None
        
"""
The Below Pydantic Validation Classes are for Task creation validation.
"""

class TaskBase(BaseModel):
    title : str
    description : Optional[str] = None
    completed : bool  = False

class TaskCreate(TaskBase):
    pass
class Task(TaskBase):
    id :int
    owner_id:int
    
    class Config:
        orm_mode:True
