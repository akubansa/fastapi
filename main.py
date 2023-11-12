from fastapi import FastAPI
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

#definiowanie modelu

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
    


@app.get("/", tags = ["category1"])
def read_root():
    """Description of the category.
    """
    return {"Hello": "world acha"}

@app.put("/iten/{item_id}")
def update_item(item_id:int, item: Item): #item spodziewa sie klasy Item
    #powyzej definiujemy co jest wymagane do wyslania put
    return{"item name":item.name, "item id": item_id}
