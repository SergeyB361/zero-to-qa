from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title='FastAPI Basics Day 5')
inventory = {1: {'id': 1, 'name': 'keyboard'}, 2: {'id': 2, 'name': 'monitor'}}


class ItemOut(BaseModel):
    id: int
    name: str


@app.get('/inventory/{item_id}', response_model=ItemOut)
def get_inventory_item(item_id: int) -> ItemOut:
    item = inventory.get(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='item not found')
    return ItemOut(**item)
