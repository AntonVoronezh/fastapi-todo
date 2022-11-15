from db.database import Base
from sqlalchemy import String, Integer, Column, ForeignKey


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    address = Column(String)
    age = Column(Integer)
    group = Column(Integer, ForeignKey('groups.id'))

    def __init__(self, full_name: str, age: int, address: str, id_group: int):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.address = address
        self.group = id_group

    def __repr__(self):
        info = f'Студент [ФИО: {self.surname} {self.name} {self.patronymic}], возраст: {self.age}, ' \
        f'адресс: {self.address}, ID группы: {self.group} '

        return info





def __repr__(self: Item):
    return f'<Item name = {self.name}, price = {self.price}, on_offer = {self.on_offer}>'
