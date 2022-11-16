from db.database import Base, engine


def create_db():
    print('Creating db..')
    Base.metadata.create_all(engine)
