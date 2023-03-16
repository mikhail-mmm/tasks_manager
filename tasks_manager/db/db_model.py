from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from typing import Any

Base = declarative_base()


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    task = Column(String)
    creation_date = Column(DateTime)
    deadline = Column(DateTime)
    status = Column(Boolean)
