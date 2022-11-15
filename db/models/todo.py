from sqlalchemy import Column, Integer, String, Boolean, Text

from db.database import Base


class Todo(Base):
    __tablename__ = 'todos'
    __table_args__ = {"comment": "Записи"}

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    on_offer = Column(Boolean, default=False)
    price = Column(Integer, nullable=False)
