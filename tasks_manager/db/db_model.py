from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.schema import MetaData


class Base(DeclarativeBase):
    metadata = MetaData()


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    task = Column(String)
    creation_date = Column(DateTime)
    deadline = Column(DateTime)
    status = Column(Boolean)
