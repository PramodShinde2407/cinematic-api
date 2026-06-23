from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime,timezone
from database.session import get_db
from models.reviews import Reviews
from schema.reviews import reviewsCreate
from schema.reviews import reviewsUpdate
from schema.reviews import reviewsDelete
from services.reviews import reviews_fetch
from sqlalchemy.orm import Session
from core.security import get_current_user
router=APIRouter()


# this is endpoint for fetching external details
@router.get("/movies/reviews")
async def reviews(movie_id:int, db:Session=Depends(get_db)):
    # 1st we will check in the db that reviews are pesent or not
    authors=[
        review.name
        for review in db.query(Reviews).filter(Reviews.movie_id==movie_id).all()
    ]
    
    if authors :
        return authors
    
    #fetching from external api
    else:
        reviews= await reviews_fetch(movie_id)
        print(reviews)
        # create new Object to save it in db
        if reviews is None:
            raise HTTPException(
                status_code=404,
                detail="reviews not Found"
                
            )
        
        id=reviews["id"]
        for review in reviews["results"]:
            new_reviews=Reviews(
                movie_id=id,
                external_review_id=review["id"],
                source="external",
                user_name=review["author_details"]["username"],
                user_id=None,
                name=review["author"],
                review=review["content"],
                created_at=review["created_at"],
                rating=review["author_details"]["rating"]
                        
            )
            db.add(new_reviews)
            print(new_reviews)
            
        db.commit()
        # db.refresh(new_reviews)
        authors=[a["author"] for a in reviews["results"]]
        print(authors)
        return authors
        


# these are the apis for fetching data which is submittesd by user

@router.get("/reviews")
async def getReview(user=Depends(get_current_user) , db:Session=Depends(get_db)):
    reviews=db.query(Reviews).filter(Reviews.user_id==user.user_id).all()  #returns a list of objects.
    return [
        {
            "review_id":review.id,
            "review":review.review,
            "movie_id":review.movie_id
        }
        for review in reviews
    ]



@router.post("/reviews")
async def giveReview(review_data:reviewsCreate, user=Depends(get_current_user) , db:Session=Depends(get_db)):
    
    review=Reviews(
        user_name=user.user_name,
        user_id=user.user_id,
        source="user",
        name=user.name,
        review=review_data.review,
        movie_id=review_data.movie_id,
        rating=review_data.rating,
        created_at=datetime.now(timezone.utc),
        external_review_id=None
        
    )
    db.add(review);
    db.commit()
    db.refresh(review)
    return review


@router.put("/reviews")
async def updateReview(review_data:reviewsUpdate, user=Depends(get_current_user) , db:Session=Depends(get_db)):
    review=db.query(Reviews).filter(Reviews.user_id == user.user_id, Reviews.id == review_data.review_id, Reviews.source=="user").first()
    if review is None:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )
    review.review=review_data.review
    review.rating=review_data.rating
    db.commit()
    db.refresh(review)       
    return review


@router.delete("/reviews")
async def deleteReview(review_data:reviewsDelete,user=Depends(get_current_user) , db:Session=Depends(get_db)):
    
    review=db.query(Reviews).filter(Reviews.user_id==user.user_id, Reviews.id == review_data.review_id, Reviews.source == "user").first()  
    if review is None:
        raise HTTPException(
            status_code=404,
            detail= "review not found"
        )
        
    db.delete(review)
    db.commit()
    return {"message":"review deleted successfully"}
