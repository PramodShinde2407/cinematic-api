# this is basically signup or registration page
#steps-->>
#1) server will 1st valided all the credentials like all are in the proper format
#2) after that it will check if user is alredy present or not by using email(unique)
#3) if yes then it will give message that user is already present 
#4) if not then it will make new row for user in user table with all its information and give new id (autoincremented)

from fastapi import APIRouter,HTTPException
from schema.userIn import UserCreate #schemas are used for data validation which comes from req body
from models.user import User  #models are used for new object creation
from database.session import get_db   
from fastapi import Depends
from sqlalchemy.orm import Session
from schema.userOut import UserOut
from utils.security import hashPassword  # here hashPassword--function
router=APIRouter()
# here db --session object not user object
@router.post("/register",response_model=UserOut)
def register(user:UserCreate, db:Session=Depends(get_db)):
    existing_user = db.query(User).filter(
        (User.email == user.email) |
        (User.user_name == user.user_name)
    ).first()

    if existing_user:
        if existing_user.email == user.email:
            raise HTTPException(
                status_code=400,
                detail="User already exists with this email"
            )

        if existing_user.user_name == user.user_name:
            raise HTTPException(
                status_code=409,
                detail="User already exists with this username"
            )
    else:
        print(user.password)
        print(len(user.password.encode("utf-8")))
        print()
        hashed_password=hashPassword(user.password)  
        if len(hashed_password.encode("utf-8")) > 70:
            raise HTTPException(
                status_code=401,
                detail="Password exceded its size"
            )
        print(hashed_password)
        print(len(hashed_password.encode("utf-8")))
        print()
        new_user=User(     # here we created new user object by using model
            name=user.name,
            email=user.email,
            password=hashed_password,
            user_name=user.user_name
             
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    
    
    