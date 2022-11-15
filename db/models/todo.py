from sqlalchemy import Column, Integer, String, Boolean, Text

from db.database import Base
from db.models.db_enums import enum_todo_type


class Todo(Base):
    __tablename__ = 'todos'
    __table_args__ = {"comment": "Записи"}

    todo_id = Column(Integer, primary_key=True, comment="Идентификатор записи что сделать")
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    active = Column(Boolean, default=False)
    weight = Column(Integer, nullable=False)
    priority = Column(enum_todo_type, comment="Тип записи")

