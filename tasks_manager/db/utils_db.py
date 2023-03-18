from datetime import date

from sqlalchemy import select
from sqlalchemy.exc import OperationalError, ProgrammingError

from db.db_classes import UndoneTasks, DoneTasks
from db.db_conection import session, db
from db.db_model import Tasks, Base


def insert_task(task: str, deadline: date) -> bool | None:
    Base.metadata.create_all(db)
    try:
        session.add(Tasks(task=task, creation_date=date.today(), deadline=deadline, status=False))
        session.commit()
        return True
    except (OperationalError, ProgrammingError):
        return None


def get_undone_tasks() -> UndoneTasks | None:
    undone_tasks = create_undone_tasks_dataclass()
    try:
        for row in session.scalars(select(Tasks).where(Tasks.status == False)):
            undone_tasks.id.append(row.id)
            undone_tasks.tasks.append(row.task)
            undone_tasks.creation_dates.append(date.strftime(row.creation_date, '%d.%m.%Y'))
            undone_tasks.deadlines.append(date.strftime(row.deadline, '%d.%m.%Y'))
            undone_tasks.time_left.append((row.deadline - row.creation_date).days)
        return undone_tasks
    except (OperationalError, ProgrammingError):
        return None


def delete_done_tasks() -> bool | None:
    try:
        session.query(Tasks).filter(Tasks.status).delete()
        session.commit()
        return True
    except (OperationalError, ProgrammingError):
        return None


def delete_all_tasks() -> bool | None:
    try:
        Base.metadata.drop_all(bind=db)
        return True
    except (OperationalError, ProgrammingError):
        return None


def change_task_status(task_number: int) -> bool | None:
    try:
        task = session.query(Tasks).get(task_number)
        task.status = True
        session.commit()
        return True
    except (OperationalError, ProgrammingError):
        return None


def get_done_tasks() -> DoneTasks | None:
    done_tasks = create_done_tasks_dataclass()
    try:
        for row in session.scalars(select(Tasks).where(Tasks.status)):
            done_tasks.id.append(row.id)
            done_tasks.tasks.append(row.task)
            done_tasks.creation_dates.append(date.strftime(row.creation_date, '%d.%m.%Y'))
            done_tasks.deadlines.append(date.strftime(row.deadline, '%d.%m.%Y'))
            done_tasks.status.append(row.status)
        return done_tasks
    except (OperationalError, ProgrammingError):
        return None


def change_deadline(task_number: int, new_deadline: date) -> bool | None:
    try:
        task = session.query(Tasks).get(task_number)
        task.deadline = new_deadline
        session.commit()
        return True
    except (OperationalError, ProgrammingError):
        return None


def create_undone_tasks_dataclass() -> UndoneTasks:
    undone_tasks = UndoneTasks(
        id=[],
        tasks=[],
        creation_dates=[],
        deadlines=[],
        time_left=[],
        )
    return undone_tasks


def create_done_tasks_dataclass() -> DoneTasks:
    done_tasks = DoneTasks(
        id=[],
        tasks=[],
        creation_dates=[],
        deadlines=[],
        status=[],
        )
    return done_tasks
