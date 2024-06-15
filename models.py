import datetime 
from sqlalchemy import Column, Integer, String, DateTime, create_engine, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    
    """
    This is the postgreSQL schema for Task creation. 
    """
    
    _tablename_ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    Username  = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime,default=datetime.datetime.nowI(datetime.UTC))
    


class Task(Base):
    
    """
    This is the postgreSQL schema for Task creation. 
    """
    
    _tablename_ = 'tasks'
    
    id = Column(Integer, primary_key=True , index=True )
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, index=True)
    owner_id = Column(Integer,ForeignKey(User.id))
    owner = relationship("User", back_populates="tasks") 