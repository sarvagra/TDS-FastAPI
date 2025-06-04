
import httpx 
from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os
import json 
import pandas as pd

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
url=os.getenv("url")

app= FastAPI()
@app.get("/sentiment")
def get_sentiement(text: str):
    headers={
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data={
        "model":"gpt-4o-mini",
        "messages":[
            {
            "role": "system",
            "content": "Classify the sentiment of the review ONLY as GOOD, BAD, or NEUTRAL."
        },
        {
            "role": "user",
            "content": text
        }
        ],
    }
    request=httpx.post(url,headers=headers, json=data, timeout=30)
    response=request.json()
    return response['choices'][0]['message']['content']

