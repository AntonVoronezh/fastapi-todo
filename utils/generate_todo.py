from sqlalchemy import Column, Integer, String, Boolean, Text

from db.database import Base, SessionLocal
from db.models.db_enums import enum_todo_type


class Todo(Base):
    __tablename__ = 'to'
    __table_args__ = {"comment": "Записи"}

    todo_id = Column(Integer, primary_key=True, comment="Идентификатор записи что сделать")
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    active = Column(Boolean, default=False)
    weight = Column(Integer, nullable=False)
    # priority = Column(enum_todo_type, comment="Тип записи")

    def __init__(self, name: str, description: str, active: bool, weight: int):
        self.name = name
        self.description = description
        self.active = active
        self.weight = weight

    def __repr__(self):
        print(f'[Name: {self.name}]')


name = 'aaaaaaa'
description = 'bbbbbbbbbbb'
active = False
weight = 1

todo = Todo(name, description, active, weight)
sess = SessionLocal()
sess.add(todo)
sess.commit()

