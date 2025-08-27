from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

# FastAPI app
app = FastAPI()

# Input schema
class Item(BaseModel):
    text: str

@app.post("/process/")
def process_text(item: Item):
    # Directly send user text to Gemini
    response = gemini_model.generate_content(item.text)
    
    return {
        "original": item.text,
        "gemini_output": response.text
    }
