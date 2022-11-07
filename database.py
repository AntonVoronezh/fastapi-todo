from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://root:root@localhost/test_db", echo=True)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)



