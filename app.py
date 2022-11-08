# uvicorn app:app --reload
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

app = FastAPI()
db = SessionLocal()


class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int
    on_offer: bool

    class Config:
        orm_mode = True


@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
    items = db.query(models.Item).all()
    return items


@app.get('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def get_item_by_id(item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item


@app.post('/items', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    db_item = db.query(models.Item).filter(models.Item.name == item.name).first()

    if db_item is not None:
        return HTTPException(status_code=400, detail='Name is !!!!!!!!!!!!!!!!!!!!!@!!!')

    new_item = models.Item(
        name=item.name,
        description=item.description,
        price=item.price,
        on_offer=item.on_offer,
    )

    db.add(new_item)
    db.commit()

    return new_item


@app.put('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def update_item_by_id(item_id: int, item: Item):
    item_to_update = db.query(models.Item).filter(models.Item.id == item_id).first()
    item_to_update.name = item.name
    item_to_update.price = item.price
    item_to_update.on_offer = item.on_offer
    item_to_update.description = item.description

    db.commit()

    return item


@app.delete('/item/{item_id}')
def delete_item_by_id(item_id: int):
    item_to_delete = db.query(models.Item).filter(models.Item.id == item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=404, detail='** not found **')

    db.delete(item_to_delete)
    db.commit()

    return item_to_delete

# @app.get('/')
# def index():
#     return {'yyy': '9999'}
#
#
# @app.get('/greet/{name}')
# def greet_name(name: str):
#     return {'title': f'hello {name}'}
#
#
# @app.get('/greet')
# def great_optional_name(name: Optional[str] = 'user'):
#     return {'message': f'hello {name}'}
#
#
# @app.put('/item/{item_id}')
# def update_item(item_id: int, item: Item):
#     return {
#         'id': item_id,
#         'name': item.name,
#         'descr': item.descr,
#         'price': item.price,
#         'on_offer': item.on_offer,
#     }
