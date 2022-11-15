from sqlalchemy import Column, Integer, ForeignKey, Date

from db.database import Base


class Todo(Base):
    __tablename__ = 'todo_details'
    __table_args__ = {"comment": "Детали записи"}

    todo_detail_id = Column(Integer, ForeignKey('todos.todo_id'), primary_key=True,
                            comment="Идентификатор деталей записи что сделать")
    todo_create = Column(Date, nullable=False)
