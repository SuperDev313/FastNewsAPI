from fastapi import FastAPI, HTTPException
from typing import Optional
import httpx
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

NEWS_API_BASE_URL = os.getenv("NEWS_API_BASE_URL")
API_KEY = os.getenv("GNEWS_API_KEY")

@app.get("/")
def read_root():
    return {"message": "Welcome to the News API!"}


@app.get("/articles/")
async def get_articles(q: Optional[str] = None, lang: str = 'en', max_results: int = 5):
    async with httpx.AsyncClient() as client:
        params = {
            "token": API_KEY,
            "lang": lang,
            "max": max_results
        }
        if q:
            params["q"] = q
        response = await client.get(f"{NEWS_API_BASE_URL}/top-headlines", params=params)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            return articles
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch articles")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
