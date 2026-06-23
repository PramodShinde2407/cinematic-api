from pydantic import BaseModel,Field,EmailStr


class UserCreate(BaseModel):
    # id:int
    name:str=Field(...,max_length=10, min_length=2)
    email:EmailStr
    password:str=Field(..., max_length=20, min_length=8)
    user_name:str=Field(..., max_length=10, min_length=3)
    
class UserSignIn(BaseModel):
    user_name:str
    password:str=Field(..., max_length=20, min_length=8)
    
    