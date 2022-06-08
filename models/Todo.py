from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from database import Base, engine

# TODO Tables!


class TODO(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))


# Create The Database!
Base.metadata.create_all(engine)
