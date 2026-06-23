from pydantic import BaseModel, Field
from datetime import date
class MovieCreate(BaseModel):
    id:int
    movie_id:int=Field(...)
    movie_name:str= Field(...)
    release_date:str
    genres:str= Field(...)
    revenue:int= Field(...,ge=0)
    budget:int= Field(...,ge=0)
    rating:float= Field(..., ge=0, le=10)
    












