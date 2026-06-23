from fastapi import FastAPI,HTTPException
from dotenv import load_dotenv
load_dotenv()   # it should loaded before using env varialbes in any file so we have loaded before below imports
from database.base import Base
from database.connection import engine
from routes.registration_route import router as regi_router
from routes.movies_routes import router as movie_router
from routes.reviews_routes import router as reviews_router
from routes.auth_routes import router as auth_router

app=FastAPI()

app.include_router(regi_router)
app.include_router(movie_router)
app.include_router(reviews_router)
app.include_router(auth_router,prefix="/auth")
@app.get('/')
def home():
    print("hii")
    return {"message":"welcome to home"}


Base.metadata.create_all(bind=engine)







