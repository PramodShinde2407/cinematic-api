import httpx
import os
TMDB_API_KEY=os.getenv("TMDB_API_KEY")
headers={
    "accept":"application/json",
    "Authorization":f"Bearer {TMDB_API_KEY}"
}


async def movie_fetch(movie_name:str):
    url="https://api.themoviedb.org/3/search/movie"
    params={
        "query":movie_name
    }
    try:
        async with httpx.AsyncClient() as client:
            res=await client.get(url, headers=headers, params=params)
            data=res.json()
            if not data["results"]:
                return None
            movie=data["results"]
            print(movie)
            return movie
            
    except httpx.ConnectError:
        print("connection Faild")
        
        
   
        
        

    








