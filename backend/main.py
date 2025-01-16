from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from cohere import Client, ClassifyExample
import uvicorn
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Obtain Cohere's API Key fron .env file
api_key = os.getenv("cohere_api")

# FastAPI App Initialization
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
co = Client(api_key)

# Route Definition
@app.post("/sentiment-analysis") # POST endpoint
async def analyze_text(text: str = Form(...)):
    try:
        response = co.classify(
            model= "embed-english-v3.0", # alternate model as opposed to large
            inputs=[text],
            examples = [
            ClassifyExample(text="I absolutely loved this movie, it was fantastic!", label="Positive"),
            ClassifyExample(text="The plot was dull and boring, I didn't enjoy it at all.", label="Negative"),
            ClassifyExample(text="The movie was okay, but nothing special.", label="Neutral"),
            ClassifyExample(text="Great acting and direction, but the pacing was off.", label="Positive"),
            ClassifyExample(text="I hated the ending, it ruined the whole experience.", label="Negative"),
            ClassifyExample(text="It was just average, nothing memorable.", label="Neutral"),
            ClassifyExample(text="This movie is amazing!", label="Positive"),
            ClassifyExample(text="I hated the ending.", label="Negative")
            ]


        )
        
        return {
            "sentiment": response.classifications[0].prediction
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
