from fastapi import APIRouter

from modules.todo.dto.todo import TodoDto

todos_router = APIRouter(prefix="/todos",
                         tags=["todos"],
                         dependencies=[])


@todos_router.get('/', response_model=TodoDto, summary="Получение списка заданий")
async def all_todos():
    return await {'aaaaa': 'bbbbbbb'}
