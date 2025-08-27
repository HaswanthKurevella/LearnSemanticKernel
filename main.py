from fastapi import FastAPI
from pydantic import BaseModel
import semantic_kernel as sk
from semantic_kernel.connectors.ai.google.google_ai import GoogleAIChatCompletion
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

# Initialize Semantic Kernel
kernel = sk.Kernel()

# Add Gemini service via official connector
gemini_service = GoogleAIChatCompletion(
    gemini_model_id="gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    service_id="gemini-service"
)

kernel.add_service(gemini_service)

# Create a semantic function (prompt template)
summarize_function = kernel.create_semantic_function(
    prompt="Summarize the following text in simple words:\n{{$input}}",
    skill_name="SummarySkill",
    function_name="Summarize"
)

# FastAPI setup
app = FastAPI()

class Item(BaseModel):
    text: str

@app.post("/process/")
async def process_text(item: Item):
    result = await kernel.run_async(
        input=item.text,
        skill_name="SummarySkill",
        function_name="Summarize"
    )
    # result.value holds the generated text
    return {
        "original": item.text,
        "gemini_summary": result.value
    }
