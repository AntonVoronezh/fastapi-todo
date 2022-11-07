from database import Base
from sqlalchemy import String, Boolean, Integer, Column


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)