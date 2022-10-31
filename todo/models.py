from sqlalchemy import Column, String, Integer, Boolean
from todo.database.base import Base


class Todo(Base):
    __tablename__ = 'todos'

    id = Column()