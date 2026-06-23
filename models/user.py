from sqlalchemy import Column, Integer, String
from database.base import Base

class User(Base):
    __tablename__="user"
    user_id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String)
    user_name=Column(String, unique=True)
    email=Column(String, unique=True)
    password=Column(String, nullable=False)
    
    