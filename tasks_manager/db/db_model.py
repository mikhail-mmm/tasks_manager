from datetime import date

from sqlalchemy import Table, Column, String, Integer, Date
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.schema import MetaData


class Base(DeclarativeBase):
    metadata = MetaData()


class TaskModel(Base):

    __table__ = Table(
        "tasks",
        Base.metadata,
        Column("id", Integer, primary_key=True),
        Column("task", String),
        Column("created_at", Date),
        Column("deadline", Date),
        Column("status", String),
    )

    id: Mapped[int]
    task: Mapped[str]
    created_at: Mapped[date]
    deadline: Mapped[date]
    status: Mapped[str]
