import random
from sqlalchemy import Column, Integer, String, Boolean, Text
from faker import Faker

from db.create_db import create_db
from db.database import Base, SessionLocal
from db.models.db_enums import enum_todo_type
from shared.enums.todos import TodoTypeEnum

bools = [True, False]


class Todo(Base):
    __tablename__ = 'aaaaaaaaaa'
    __table_args__ = {"comment": "Записи"}

    todo_id = Column(Integer, primary_key=True, comment="Идентификатор записи что сделать")
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    active = Column(Boolean, default=False)
    weight = Column(Integer, nullable=False)
    priority = Column(enum_todo_type, comment="Тип записи")

    def __init__(self, name: str, description: str, active: bool, weight: int, priority: TodoTypeEnum):
        self.name = name
        self.description = description
        self.active = active
        self.weight = weight
        self.priority = priority

    def __repr__(self):
        print(f'[Name: {self.name}]')


# create_db()

facker = Faker('ru_RU')

name = facker.name()
description = facker.address()
active = random.choice(bools)
weight = facker.random.randint(10, 100)
priority = random.choice(list(TodoTypeEnum))

# todo = Todo(name, description, active, weight, priority)
# sess = SessionLocal()
# sess.add(todo)
# sess.commit()

print(facker.paragraph(nb_sentences=5))
print(facker.lexify(text='Random Identifier: ??????????'))
print(facker.bothify(text='Product Number: ????-########', letters='ABCDE'))
print(facker.numerify(text='Intel Core i%-%%##K vs AMD Ryzen % %%##X'))
