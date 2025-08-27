from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

    #Fastapi is initialized
app=FastAPI()
#     #kernel is initialized
# kernel=sk.Kernel()
    #GEMINI ai should be configured with kernel (api key auth)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

class Item(BaseModel):
    text:str
@app.post("/process/")
def send_data(item:Item):
    input_text=item.text
    gemini_response = gemini_model.generate_content(input_text)
    bard_output = gemini_response.text
    return {"response": bard_output}