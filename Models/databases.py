from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv


load_dotenv()
# Getting the database from Environmental Variables..
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

"""
This is a simple commit to check whether my github account is updating the contrbution heatmap or not
I am doing another commit to test it 

"""