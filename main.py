from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Item(BaseModel):
    text:str
@app.post("/process/")
def send_data(item:Item):
    processed_text=item.text.upper()
    return {"processed_text":processed_text}