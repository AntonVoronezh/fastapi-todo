from fastapi import APIRouter

from app import db
from modules.todo.dto.todo import TodoDto

todos_router = APIRouter(prefix="/todos",
                         tags=["todos"],
                         dependencies=[])


@todos_router.get('/', response_model=TodoDto, status_code=200, summary="Получение списка заданий")
async def all_todos():
    todos = db.query(TodoDto).all()
    return todos
