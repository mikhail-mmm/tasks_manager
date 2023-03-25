import enum

from sqlalchemy import Column, String, Integer, Date, Enum
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.schema import MetaData


class Base(DeclarativeBase):
    metadata = MetaData()


class TaskStatus(enum.Enum):
    Done = "Done"
    Undone = "Undone"


class TaskModel(Base):
    Base.metadata

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    task = Column(String)
    created_at = Column(Date)
    deadline = Column(Date)
    status = Column(Enum(TaskStatus))

    def __str__(self) -> str:
        return f"{self.task} {self.created_at} {self.deadline} {self.status.value}"
