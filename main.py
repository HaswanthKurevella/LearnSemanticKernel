from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import semantic_kernel as sk
from semantic_kernel.connectors.ai.google.google_ai import GoogleAIChatCompletion


# Load environment variables
load_dotenv()

# Get Gemini API key
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Semantic Kernel
kernel = sk.Kernel()

kernel.add_service(
    GoogleAIChatCompletion(
        service_id="gemini",
        api_key=GEMINI_KEY,
        gemini_model_id="gemini-2.0-flash"
    )
)

# FastAPI app
app = FastAPI()

# Input schema
class Item(BaseModel):
    text: str

@app.post("/process/")
async def process_text(item: Item):
    # Use Semantic Kernel to call Gemini
    response = await kernel.invoke_prompt(item.text, service_id="gemini")

    return {
        "original": item.text,
        "gemini_output": str(response)
    }
