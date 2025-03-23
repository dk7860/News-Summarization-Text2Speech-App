from fastapi import FastAPI
from pydantic import BaseModel
from utils import fetch_news, analyze_sentiment, generate_hindi_audio
app = FastAPI()
class NewsRequest(BaseModel):
    company_name: str
@app.get("/news")
def get_news(company_name: str):
    return fetch_news(company_name)
@app.post("/sentiment")
def get_sentiment(news_request: NewsRequest):
    return analyze_sentiment(news_request.company_name)
@app.post("/tts")
def get_tts(news_request: NewsRequest):
    return generate_hindi_audio(news_request.company_name)