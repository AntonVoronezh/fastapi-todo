from fastapi import APIRouter

from modules.todo.dto.todo import TodoDto

todos_router = APIRouter(prefix=f"ssssssssssssss")


@todos_router.get('/', response_model=TodoDto, summary="Получение списка заданий")
async def all_todos():
    return await {'aaaaa': 'bbbbbbb'}
