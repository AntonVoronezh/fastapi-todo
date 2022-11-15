# uvicorn main:app --reload
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db.database import SessionLocal
from modules.todo.controller.todo import todos_router

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

for router in (
        todos_router
):
    app.include_router(router)
