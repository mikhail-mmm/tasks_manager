from datetime import date

from db.db_classes import Task, TaskStatusSymbol
from db.db_model import TaskModel

from sqlalchemy import select, delete

from db.db_creation import SESSION


def insert_task(task: str, deadline: date) -> bool:
    SESSION.add(TaskModel(task=task, created_at=date.today(), deadline=deadline, status=TaskStatusSymbol.Undone.value))
    SESSION.commit()
    return True


def get_tasks(status: str) -> list[Task]:
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
    SESSION.execute(delete(TaskModel).filter(TaskModel.status))
    SESSION.commit()


def delete_all() -> None:
    SESSION.execute(delete(TaskModel))
    SESSION.commit()


def change_task_status_to_done(task_number: int) -> bool | None:
    try:
        row = SESSION.query(TaskModel).get(task_number)
        if row.status == TaskStatusSymbol.Undone.value:
            row.status = TaskStatusSymbol.Done.value
            SESSION.commit()
            return True
        return None
    except AttributeError:
        return None


def change_deadline(task_number: int, new_deadline: date) -> bool | None:
    try:
        row = SESSION.query(TaskModel).get(task_number)
        if row.status == TaskStatusSymbol.Undone.value:
            row.deadline = new_deadline
            SESSION.commit()
            return True
        return None
    except AttributeError:
        return None
