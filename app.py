# uvicorn app:app --reload
from time import timezone

from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from sqlalchemy import desc, asc, select

from db.database import SessionLocal
import models
from db.models.db_enums import enum_todo_type

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = SessionLocal()


class Todo(BaseModel):
    todo_id = int
    name = str
    description = str
    on_offer = bool
    weight = int
    priority = enum_todo_type

    class Config:
        orm_mode = True


class TodoDetails(BaseModel):
    todo_detail_id = int
    todo_create = timezone

    class Config:
        orm_mode = True




#
# class Item(BaseModel):
#     id: int
#     name: str
#     description: str
#     price: int
#     on_offer: bool
#     tags: List[int]
#
#     class Config:
#         orm_mode = True
#
#
# class Tag(BaseModel):
#     id: int
#     name: str
#
#     class Config:
#         orm_mode = True
#
#
# @app.get('/items', response_model=List[Item], status_code=200, name='Получение всех записей')
# def get_all_items():
#     items = db.query(models.Item).all()
#     return items
#
#
# @app.get('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
# def get_item_by_id(item_id: int):
#     item = db.query(models.Item).filter(models.Item.id == item_id).first()
#     return item
#
#
# @app.post('/items', response_model=Item, status_code=status.HTTP_201_CREATED)
# def create_item(item: Item):
#     db_item = db.query(models.Item).filter(models.Item.name == item.name).first()
#
#     if db_item is not None:
#         return HTTPException(status_code=400, detail='Name is !!!!!!!!!!!!!!!!!!!!!@!!!')
#
#     new_item = models.Item(
#         name=item.name,
#         description=item.description,
#         price=item.price,
#         on_offer=item.on_offer,
#     )
#
#     db.add(new_item)
#     db.commit()
#
#     return new_item
#
#
# @app.put('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
# def update_item_by_id(item_id: int, item: Item):
#     item_to_update = db.query(models.Item).filter(models.Item.id == item_id).first()
#     item_to_update.name = item.name
#     item_to_update.price = item.price
#     item_to_update.on_offer = item.on_offer
#     item_to_update.description = item.description
#
#     db.commit()
#
#     return item
#
#
# @app.delete('/item/{item_id}')
# def delete_item_by_id(item_id: int):
#     item_to_delete = db.query(models.Item).filter(models.Item.id == item_id).first()
#
#     if item_to_delete is None:
#         raise HTTPException(status_code=404, detail='** not found **')
#
#     db.delete(item_to_delete)
#     db.commit()
#
#     return item_to_delete
#
#
# @app.get('/sort')
# def sort_items(order_by: str = None, order_direction: str = None):
#     if order_direction is None:
#         items = db.query(models.Item).order_by(order_by).all()
#     if order_direction == 'asc':
#         items = db.query(models.Item).order_by(asc(order_by)).all()
#     if order_direction == 'desc':
#         items = db.query(models.Item).order_by(desc(order_by)).all()
#     return items
#
#
# @app.get('/search')
# def items_search(q: str or int = None):
#     if q is None:
#         items = db.query(models.Item).all()
#     else:
#         items = db.query(models.Item).filter(models.Item.name.like(f'%{q}%')).all()
#     return items
#
#
# @app.get('/pagination')
# def get_pagination(skip: int = 1, limit: int = 1):
#     items = db.query(models.Item).offset(skip).limit(limit).all()
#     return items
#
#
# @app.get('/tags')
# def get_tags():
#     tags = db.query(models.Tag).all()
#     return tags
#
#
# @app.get('/tags/filter/{tag_id}')
# def filter_tags(tag_id: int):
#     # tag = db.query(models2.Item).filter(models2.Item.tags.in_(tag_id)).first()
#     c = select(db.query(models.Item)).where(models.Item.tags.in_(tag_id))
#     # tag = db.query(models2.Item).all()
#     s = select(c)
#     rs = db.query(models.Item).execute(c)
#     print(rs.fetchall())
#     return rs.fetchall()
#
