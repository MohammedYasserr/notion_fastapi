import datetime 
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class User(Base):
    _tablename_ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    Username  = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime,default=datetime.datetime.nowI(datetime.UTC))
    