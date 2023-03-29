from datetime import date

from db.utils_db import (
    insert_task, get_tasks, delete_done_tasks,
    change_task_status_to_done, change_deadline,
    delete_all_tasks, is_task_in_db, is_undone_task,
)

import fire

from pathlib import Path

from rich.markdown import Markdown

from task_classes import TaskStatus

from utils import (
    create_print_table_undone_tasks, create_print_table_done_tasks,
    str_to_date, CONSOLE,
)


class TaskManager:

    def add(self, task: str, deadline: str) -> None:
        deadline_datetime = str_to_date(deadline)
        if deadline_datetime:
            inserted_task = insert_task(task, deadline_datetime)
            return CONSOLE.print(
                f"Задача {task} добавлена!\n{inserted_task}\n:thumbs_up:",
                style="bold green",
            )
        else:
            return CONSOLE.print(
                f"Неверный формат ввода даты дедлайна: {deadline}!",
                "\n:thumbs_down:",
                "\nПопробуйте формат ДД:ММ:ГГГГ.",
                "\nИли убедитесь, что дата дедлайна не из прошлого.",
                style="bold red",
            )

    def show(self) -> None:
        table = create_print_table_undone_tasks()
        tasks = get_tasks(TaskStatus.Undone)
        if tasks:
            for row in tasks:
                left_time = (row.deadline - row.created_at).days
                table.add_row(
                    str(row.id), row.task_name, date.strftime(row.created_at, '%d.%m.%Y'),
                    date.strftime(row.deadline, '%d.%m.%Y'), f"{left_time} day(s)",
                )
            return CONSOLE.print(table)
        return CONSOLE.print(
            "Нет выполняемых задач!",
            style="bold red",
        )

    def history(self) -> None:
        table = create_print_table_done_tasks()
        done_tasks = get_tasks(TaskStatus.Done)
        if done_tasks:
            for row in done_tasks:
                table.add_row(
                    str(row.id), row.task_name, date.strftime(row.created_at, '%d.%m.%Y'),
                    date.strftime(row.deadline, '%d.%m.%Y'), row.status.value,
                )
            return CONSOLE.print(table)
        return CONSOLE.print(
            "Нет выполненных задач!",
            style="bold red",
        )

    def move(self, task_number: str) -> None:
        if is_task_in_db(task_number) and is_undone_task(task_number):
            change_task_status_to_done(int(task_number))
            return CONSOLE.print(
                f"Задача {task_number} выполнена!",
                "\n:thumbs_up:",
                style="bold green",
            )
        return CONSOLE.print(
            f"Задача номер {task_number} не найдена или уже выполнена!",
            "\n:thumbs_down:",
            "\nПопробуйте вызвать команду <show>, чтобы убедиться в правильности номера задачи.",
            style="bold red",
        )

    def change(self, task_number: str, new_deadline: str) -> None:
        deadline_datetime = str_to_date(new_deadline)
        if deadline_datetime:
            if is_task_in_db(task_number) and is_undone_task(task_number):
                change_deadline(int(task_number), deadline_datetime)
                return CONSOLE.print(
                    f"Дедлайн задачи {task_number} изменен на {new_deadline}!",
                    "\n:thumbs_up:",
                    style="bold green",
                )
            else:
                return CONSOLE.print(
                    f"Задача номер {task_number} не найдена или вы пытаетесь изменить дедлайн уже выполненной задачи!",
                    "\n:thumbs_down:",
                    "\nПопробуйте вызвать команду <show>, чтобы убедиться в правильности номера задачи.",
                    style="bold red",
                )
        else:
            return CONSOLE.print(
                f"Неверный формат ввода даты дедлайна: {new_deadline}!",
                "\n:thumbs_down:",
                "\nПопробуйте формат ДД:ММ:ГГГГ.",
                "\nИли убедитесь, что дата дедлайна не из прошлого.",
                style="bold red",
            )

    def remove(self, arg: str = 'done') -> None:
        if arg == 'done':
            delete_done_tasks()
            return CONSOLE.print(
                "Выполненные задачи удалены!",
                style="bold red",
            )
        elif arg == 'all':
            delete_all_tasks()
            return CONSOLE.print(
                "Все задачи удалены!",
                style="bold red",
            )

    def help(self) -> None:
        with open("HELP.md") as help:
            markdown = Markdown(help.read())
        return CONSOLE.print(markdown)

    def readme(self) -> None:
        readme_path = f"{Path(__file__).parents[1]}/README.md"
        with open(readme_path) as readme:
            markdown = Markdown(readme.read())
        return CONSOLE.print(markdown)


if __name__ == "__main__":
    task = TaskManager()
    fire.Fire(task)
