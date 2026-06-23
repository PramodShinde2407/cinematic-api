from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.dialects.postgresql import JSON
from database.base import Base

class Movie(Base):
    __tablename__="movies"
    id=Column(Integer, primary_key=True, autoincrement=True)
    movie_id=Column(Integer, unique=True)
    movie_name=Column(String)
    release_date=Column(String)
    genres=Column(JSON)
    revenue=Column(Integer)
    budget=Column(Integer)
    rating=Column(Float)
    
    
    