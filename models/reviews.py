from sqlalchemy import Column, Integer, String, Float
from database.base import Base    
class Reviews(Base):
    __tablename__="reviews"
    id=Column(Integer,primary_key=True, autoincrement=True)
    source=Column(String)
    user_id=Column(Integer,nullable=True)
    external_review_id=Column(Integer,nullable=True)
    movie_id=Column(Integer)# foreign key
    user_name=Column(String)
    name=Column(String)
    review=Column(String)
    created_at=Column(String) # when review is posted
    rating=Column(Float)
    
    
    