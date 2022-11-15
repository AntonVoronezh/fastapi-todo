from sqlalchemy import String, Integer, Column, ForeignKey, Table
from sqlalchemy.orm import relationship

from db.database import Base

association_table = Table('association', Base.metadata,
                          Column('lesson_id', Integer, ForeignKey('lesson.id')),
                          Column('group_id', Integer, ForeignKey('groups.id'))
                          )



class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    lesson_title = Column(String)
    gropus = relationship('Group', secondary=association_table, backref='group_lesson')


    def __repr__(self):
        info = f'Группа [ID: {self.id} , Название: {self.group_name}]'
        return info
