from pydantic import BaseModel,EmailStr
from typing import List, Optional
from datetime import datetime



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