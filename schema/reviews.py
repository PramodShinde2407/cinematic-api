from pydantic import BaseModel, Field
from datetime import date

class reviewsCreate(BaseModel):
    review:str=Field(...,min_length=0)
    movie_id:int=Field(...,ge=1)
    rating:int=Field(...,ge=0,le=5)
    
    
class reviewsUpdate(BaseModel):
    review_id:int=Field(...)
    review:str=Field(...,min_length=0)
    rating:int=Field(...,ge=0,le=5)
    
class reviewsDelete(BaseModel):
    review_id:int=Field(...)
    
     