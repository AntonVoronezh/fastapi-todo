from sqlalchemy.dialects.postgresql import ARRAY

from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    on_offer = Column(Boolean, default=False)
    price = Column(Integer, nullable=False)
    tags = Column(ARRAY(Integer), default=[])


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)


def __repr__(self: Item):
    return f'<Item name = {self.name}, price = {self.price}, on_offer = {self.on_offer}>'
