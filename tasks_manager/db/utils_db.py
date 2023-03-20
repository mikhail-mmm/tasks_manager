from datetime import date

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from db.db_classes import Task
from db.config import get_config, get_connection_dsn
from db.db_model import Tasks, Base

db = create_engine(get_connection_dsn(get_config()), echo=True)

session = Session(db)


def insert_task(task: str, deadline: date) -> bool:
    Base.metadata.create_all(db)
    session.add(Tasks(task=task, creation_date=date.today(), deadline=deadline, status=False))
    session.commit()
    return True


def get_undone_tasks() -> list[Task]:
    undone_tasks = []
    for row in session.scalars(select(Tasks).where(Tasks.status == False)):
        left_time = (row.deadline - row.creation_date).days
        task = Task(
            id=row.id,
            task_name=row.task,
            creation_date=date.strftime(row.creation_date, '%d.%m.%Y'),
            deadline=date.strftime(row.deadline, '%d.%m.%Y'),
            other=f"{left_time} day(s)",
        )
        undone_tasks.append(task)
    return undone_tasks


def delete_history() -> bool:
    session.query(Tasks).filter(Tasks.status).delete()
    session.commit()
    return True


def delete_all() -> bool:
    Base.metadata.drop_all(bind=db)
    return True


def change_task_status(task_number: int) -> bool:
    task = session.query(Tasks).get(task_number)
    task.status = True
    session.commit()
    return True


def get_done_tasks() -> list[Task]:
    done_tasks = []
    for row in session.scalars(select(Tasks).where(Tasks.status)):
        task = Task(
            id=row.id,
            task_name=row.task,
            creation_date=date.strftime(row.creation_date, '%d.%m.%Y'),
            deadline=date.strftime(row.deadline, '%d.%m.%Y'),
            other="Done",
        )
        done_tasks.append(task)
    return done_tasks


def change_deadline(task_number: int, new_deadline: date) -> bool:
    row = session.query(Tasks).get(task_number)
    row.deadline = new_deadline
    session.commit()
    return True
