import asyncio
import httpx

headers = {
    "accept": "application/json",
    "Authorization": "Bearer YOUR_TOKEN"
}

async def test():
    async with httpx.AsyncClient(timeout=30) as client:
        res = await client.get(
            "https://api.themoviedb.org/3/movie/550",
            headers=headers
        )
        print("Status:", res.status_code)
        print(res.text[:500])

asyncio.run(test())