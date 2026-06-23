from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from models.user import User
from database.session import get_db
from sqlalchemy.orm import Session
import os

# -- config 


SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_TIME=int(os.getenv("ACCESS_TOKEN_EXPIRE_TIME"))

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")

# create access token
# this is fun is used during login process once system verfies the user entered password and db's stored password exact match it gives token to the user

def create_access_token(data:dict, expires_delta:Optional[timedelta]= None):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+(expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME))
    to_encode.update({
        "exp":expire,
        "type":"access"
    })
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

# get current user
# this fun is used during user tries to acccess protected routes
# here we pass token as a parameter actually this token is passed by fronted (stored in browser) so this fun validates that token
# how validates-->> get the token, extract payload (user_id and token types) from the token check user_id matches exactly with db's stored user_id
# -->> also  check token type and expiray time if it expired raise the error

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):  
    credentials_Exceptions=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credentials",
        headers={"www-Authenticate": "Bearer"}
    )
    
    
    try:
        payload=jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        user_id:str=payload.get("sub")
        # exp:str=payload.get("exp")
        token_type:str=payload.get("type")
        if user_id is None or token_type!="access":
            raise credentials_Exceptions
        
    except JWTError:
        raise credentials_Exceptions
                    
    user=db.query(User).filter(User.user_id==user_id).first()
    if user is None:
        raise credentials_Exceptions
    print(user)
    return user
    




