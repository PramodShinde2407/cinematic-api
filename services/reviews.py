import httpx
# import asyncio
import os

TMDB_API_KEY=os.getenv("TMDB_API_KEY")

headers={
    "accept":"application/json",
    "Authorization":f"Bearer {TMDB_API_KEY}"
    
}

async def reviews_fetch(movie_id:int):
    url=f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"
    
    try:
        async with httpx.AsyncClient() as client:
            res=await client.get(url,headers=headers)
            data=res.json()
            # print(data["results"])
            authors=[a["author"] for a in data["results"]]
            print(authors)
            # print(data)
            return data
            
    except httpx.ConnectTimeout:
        print("Connection timed out")

    except httpx.ConnectError:
        print("Connection failed")

    except Exception as e:
        print("Error:", e)
    

# asyncio.run(reviews_fetch(414906))