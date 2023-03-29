import enum
import sys

from datetime import date

from db.db_creation import connect_db
from db.db_model import TaskModel

from sqlalchemy import select, delete
from sqlalchemy.exc import OperationalError

from task_classes import Task, TaskStatus

from utils import CONSOLE

try:
    DB, SESSION = connect_db()
except OperationalError:
    CONSOLE.print("Нет связи с БД!\n:no_entry_sign:", style="bold red")
    sys.exit()


def insert_task(task: str, deadline: date) -> TaskModel:
    inserted_task = TaskModel(
        task=task,
        created_at=date.today(),
        deadline=deadline,
        status=TaskStatus.Undone,
    )
    SESSION.add(inserted_task)
    SESSION.commit()
    return inserted_task


def get_tasks(status: enum.Enum) -> list[Task]:
    undone_tasks = []
    for row in SESSION.scalars(select(TaskModel).where(TaskModel.status == status)):
        task = Task(
            id=row.id,
            task_name=row.task,
            created_at=row.created_at,
            deadline=row.deadline,
            status=row.status
        )
        undone_tasks.append(task)
    return undone_tasks


def delete_done_tasks() -> None:
    SESSION.execute(delete(TaskModel).filter(TaskModel.status == TaskStatus.Done))
    SESSION.commit()


def delete_all_tasks() -> None:
    SESSION.execute(delete(TaskModel))
    SESSION.commit()


def change_task_status_to_done(task_number: int) -> None:
    row = SESSION.query(TaskModel).get(task_number)
    row.status = TaskStatus.Done
    SESSION.commit()


def change_deadline(task_number: int, new_deadline: date) -> None:
    row = SESSION.query(TaskModel).get(task_number)
    row.deadline = new_deadline
    SESSION.commit()


def is_task_in_db(task_number: int) -> bool:
    if SESSION.query(TaskModel).filter_by(id=task_number).first() is not None:
        return True
    return False


def is_undone_task(task_number: int) -> bool:
    row = SESSION.query(TaskModel).get(task_number)
    if row.status == TaskStatus.Undone:
        return True
    return False
