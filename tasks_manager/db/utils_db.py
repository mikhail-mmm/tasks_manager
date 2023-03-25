import enum
import sys

from datetime import date

from db.db_classes import Task
from db.db_creation import connect_db
from db.db_model import TaskModel, TaskStatus

from sqlalchemy import select, delete
from sqlalchemy.exc import OperationalError

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


def change_task_status_to_done(task_number: int) -> str | None:
    if SESSION.query(TaskModel).filter_by(id=task_number).first() is not None:
        row = SESSION.query(TaskModel).get(task_number)
        if row.status == TaskStatus.Undone:
            row.status = TaskStatus.Done
            SESSION.commit()
            changed_status_task = SESSION.query(TaskModel).get(task_number)
            return changed_status_task.status.value
    return None


def change_deadline(task_number: int, new_deadline: date) -> date | None:
    if SESSION.query(TaskModel).filter_by(id=task_number).first() is not None:
        row = SESSION.query(TaskModel).get(task_number)
        if row.status == TaskStatus.Undone:
            row.deadline = new_deadline
            SESSION.commit()
            changed_deadline_task = SESSION.query(TaskModel).get(task_number)
            return changed_deadline_task.deadline
    return None
