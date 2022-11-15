from sqlalchemy.orm import relationship

from db.database import Base
from sqlalchemy import String, Integer, Column


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String)
    student = relationship('Student')

    def __repr__(self):
        info = f'Группа [ID: {self.id} , Название: {self.group_name}]'
        return info
