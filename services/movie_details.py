import httpx
# import asyncio
import os
TMDB_API_KEY=os.getenv("TMDB_API_KEY")
headers={
    "accept":"application/json",
    "Authorization":f"Bearer {TMDB_API_KEY}"
    
}

async def movie_details_fetch(movie_id:int):
    url=f"https://api.themoviedb.org/3/movie/{movie_id}"
    try:
        async with httpx.AsyncClient() as client:
        
            res=await client.get(url, headers=headers)
            details=res.json()
            print(details)
            genre_names=[g["name"] for g in details["genres"] ]
            return{
                "title": details["original_title"],
                "release_date": details["release_date"],
                "rating": details["vote_average"],
                "budget": details["budget"],
                "genres": genre_names,
                "revenue": details["revenue"],
                "id":details["id"]
                
                
            }
            
    except httpx.ConnectError:
        print("connection Faild")
        
        
   
# asyncio.run(movie_details_fetch(414906))       
        

    








