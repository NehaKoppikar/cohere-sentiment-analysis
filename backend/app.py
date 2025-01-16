from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cohere import ClassifyExample
import os
from dotenv import load_dotenv
import uvicorn
import cohere

# Load environment variables
load_dotenv()
api_key = os.getenv("cohere_api")

if not api_key:
    raise ValueError("Cohere API key not found. Please set it in the .env file.")

app = FastAPI(debug=True)

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup the Cohere client
co = cohere.ClientV2(api_key)

# Pydantic model for input validation
class SentimentRequest(BaseModel):
    text: str

COHERE_EXAMPLES = [
    ClassifyExample(text="I absolutely loved this movie, it was fantastic!", label="Positive"),
    ClassifyExample(text="The plot was dull and boring, I didn't enjoy it at all.", label="Negative"),
    ClassifyExample(text="The movie was okay, but nothing special.", label="Neutral"),
    ClassifyExample(text="Great acting and direction, but the pacing was off.", label="Positive"),
    ClassifyExample(text="I hated the ending, it ruined the whole experience.", label="Negative"),
    ClassifyExample(text="It was just average, nothing memorable.", label="Neutral"),
    ClassifyExample(text="This movie is amazing!", label="Positive"),
    ClassifyExample(text="I hated the ending.", label="Negative"),
]

@app.post("/sentiment-analysis", summary="Perform Sentiment Analysis")
async def analyze_text(text: str = Form(...)):
    try:
        response = co.classify(
            model="embed-english-v3.0",
            inputs=[text],
            examples=COHERE_EXAMPLES
        )
        return {
            "sentiment": response.classifications[0].prediction
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
