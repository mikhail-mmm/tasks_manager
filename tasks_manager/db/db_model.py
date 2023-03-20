from datetime import date
from sqlalchemy import Table, Column, String, Integer, Date, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.schema import MetaData


class Base(DeclarativeBase):
    metadata = MetaData()


class Tasks(Base):

    __table__ = Table(
        "tasks",
        Base.metadata,
        Column("id", Integer, primary_key=True),
        Column("task", String),
        Column("creation_date", Date),
        Column("deadline", Date),
        Column("status", Boolean),
    )

    id: Mapped[int]
    task: Mapped[str]
    creation_date: Mapped[date]
    deadline: Mapped[date]
    status: Mapped[bool]
