from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

# from schema.userIn import UserSignIn
from utils.security import hashPassword
from utils.security import verifyPassword
from database.session import get_db
from models.user import User
from core.security import create_access_token
from sqlalchemy.orm import Session
router=APIRouter()

@router.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    user=db.query(User).filter(User.user_name==form_data.username).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="user not Found"
        )
    else:
        verified_user=verifyPassword(form_data.password,user.password)
        if not verified_user:
            raise HTTPException(
                status_code=401,
                detail="invalid Credentials"
            )
        
        access_token=create_access_token(
            data={"sub":str(user.user_id)}
        )
        return {
            "access_token":access_token,
            "token_type":"bearer"
        }
    