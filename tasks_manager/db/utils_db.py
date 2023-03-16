from datetime import date

from sqlalchemy import select
from sqlalchemy.exc import OperationalError

from db.db_classes import GettingTasks
from db.db_conection import session
from db.db_model import Tasks


def insert_task(task, deadline) -> bool:
    try:
        session.add(Tasks(task=task, creation_date=date.today(), deadline=deadline, status=False))
        session.commit()
        return True
    except OperationalError:
        return False


def get_undone_tasks() -> GettingTasks | None:
    undone_tasks = getting_tasks()
    try:
        for row in session.scalars(select(Tasks).where(Tasks.status is False)):
            undone_tasks.id.append(row.id)
            undone_tasks.tasks.append(row.task)
            undone_tasks.creation_dates.append(date.strftime(row.creation_date, '%d.%m.%Y'))
            undone_tasks.deadlines.append(date.strftime(row.deadline, '%d.%m.%Y'))
            undone_tasks.status.append(row.status)
        return undone_tasks
    except OperationalError:
        return None


def delete_done_date() -> bool:
    session.query(Tasks).filter(Tasks.status is False).delete()
    session.commit()
    return True


def chenge_task_status(task_number):
    try:
        task = session.query(Tasks).get(task_number)
        task.status = True
        session.commit()
    except OperationalError:
        return None


def get_done_tasks():
    done_tasks = getting_tasks()
    try:
        for row in session.scalars(select(Tasks).where(Tasks.status is True)):
            done_tasks.id.append(row.id)
            done_tasks.tasks.append(row.task)
            done_tasks.creation_dates.append(date.strftime(row.creation_date, '%d.%m.%Y'))
            done_tasks.deadlines.append(date.strftime(row.deadline, '%d.%m.%Y'))
            done_tasks.status.append(row.status)
        return done_tasks
    except OperationalError:
        return None


def getting_tasks() -> GettingTasks:
    getting_tasks = GettingTasks(
        id=[],
        tasks=[],
        creation_dates=[],
        deadlines=[],
        status=[],
        )
    return getting_tasks
