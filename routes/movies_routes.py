from fastapi import APIRouter,HTTPException, Depends
from database.session import get_db
# from schema.movie import MovieCreate
from models.movie import Movie
from services.movie_list import movie_fetch
from services.movie_details import movie_details_fetch
from sqlalchemy.orm import Session
router=APIRouter()


@router.get("/movies/search")
async def find(movie_name:str):
        movie=await movie_fetch(movie_name)
        if movie is None:
            raise HTTPException(
                status_code=404,
                detail="Movie not Found"
                
            )
        return movie
    
    

@router.get("/movies/details")
async def details(movie_id:int, db:Session=Depends(get_db)):
    #check in the db 1st
    movie=db.query(Movie).filter(Movie.movie_id == movie_id).first()  # it wil return object
    if movie:
        return movie

    else:
        movie=await movie_details_fetch(movie_id)
        if movie is None:
            raise HTTPException(
                status_code=404,
                detail="Movie not Found"
                
            )
                
            
        new_movie=Movie(
            movie_name=movie["title"],
            release_date=movie["release_date"],
            rating=movie["rating"],
            movie_id=movie["id"],
            genres=movie["genres"],
            revenue=movie["revenue"],
            budget=movie["budget"]
            
            
        )
        print(new_movie)
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
        return new_movie
    
    

