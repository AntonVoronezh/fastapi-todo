# uvicorn app:app --reload
from fastapi import FastAPI
from pydantic import BaseModel
from typing import  Optional

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    descr: str
    price: int
    on_offer: bool


@app.get('/')
def index():
    return {'yyy': '9999'}


@app.get('/greet/{name}')
def greet_name(name: str):
    return {'title': f'hello {name}'}


@app.get('/greet')
def great_optional_name(name: Optional[str] = 'user'):
    return {'message': f'hello {name}'}


@app.put('/item/{item_id}')
def update_item(item_id: int, item: Item):
    return {
        'id': item_id,
        'name': item.name,
        'descr': item.descr,
        'price': item.price,
        'on_offer': item.on_offer,
    }
