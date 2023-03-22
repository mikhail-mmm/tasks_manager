from datetime import date

from db.db_classes import TaskStatusSymbol
from db.utils_db import (insert_task, get_tasks, delete_done_tasks,
                         change_task_status_to_done, change_deadline,
                         delete_all)

import fire

from pathlib import Path

from rich.markdown import Markdown

from utils import (create_print_table_undone_tasks, create_print_table_done_tasks,
                   str_to_date, console)


class TaskManager:

    def add(self, task: str, deadline: str) -> None:
        deadline_datetime = str_to_date(deadline)
        if deadline_datetime:
            if insert_task(task, deadline_datetime):
                return console.print(
                    f"Задача {task} добавлена! Deadline: {deadline}",
                    "\n:thumbs_up:",
                    style="bold green",
                )
            else:
                return console.print(
                    "Ошибка. Нет связи с БД!",
                    style="bold red"
                )
        else:
            return console.print(
                f"Неверный формат ввода даты дедлайна: {deadline}!",
                "\n:thumbs_down:",
                "\nПопробуйте формат ДД:ММ:ГГГГ.",
                "\nИли убедитесь, что дата дедлайна не из прошлого.",
                style="bold red"
            )

    def show(self) -> None:
        table = create_print_table_undone_tasks()
        tasks = get_tasks(TaskStatusSymbol.Undone.value)
        if tasks:
            for row in tasks:
                left_time = (row.deadline - row.created_at).days
                table.add_row(
                    str(row.id), row.task_name, date.strftime(row.created_at, '%d.%m.%Y'),
                    date.strftime(row.deadline, '%d.%m.%Y'), f"{left_time} day(s)",
                    )
            return console.print(table)
        return console.print(
                    "Нет выполняемых задач!",
                    style="bold red",
                )

    def history(self) -> None:
        table = create_print_table_done_tasks()
        done_tasks = get_tasks(TaskStatusSymbol.Done.value)
        if done_tasks:
            for row in done_tasks:
                table.add_row(
                    str(row.id), row.task_name, date.strftime(row.created_at, '%d.%m.%Y'),
                    date.strftime(row.deadline, '%d.%m.%Y'), row.status,
                    )
            return console.print(table)
        return console.print(
            "Нет выполненных задач!",
            style="bold red"
        )

    def move(self, selected_task: str) -> None:
        if change_task_status_to_done(int(selected_task)):
            return console.print(
                    f"Задача номер {selected_task} выполнена!",
                    "\n:thumbs_up:",
                    style="bold green",
                )
        return console.print(
            f"Задача номер {selected_task} не найдена или уже выполнена!",
            "\n:thumbs_down:",
            "\nПопробуйте вызвать команду <show>, чтобы убедиться в правильности номера задачи.",
            style="bold red"
        )

    def change(self, task_number: str, new_deadline: str) -> None:
        deadline_datetime = str_to_date(new_deadline)
        if deadline_datetime:
            if change_deadline(int(task_number), deadline_datetime):
                return console.print(
                        f"Дедлайн задачи {task_number} изменен на {new_deadline}!",
                        "\n:thumbs_up:",
                        style="bold green",
                    )
            else:
                return console.print(
                    f"Задача номер {task_number} не найдена или вы пытаетесь изменить дедлайн уже выполненной задачи!",
                    "\n:thumbs_down:",
                    "\nПопробуйте вызвать команду <show>, чтобы убедиться в правильности номера задачи.",
                    style="bold red"
                )
        else:
            return console.print(
                f"Неверный формат ввода даты дедлайна: {new_deadline}!",
                "\n:thumbs_down:",
                "\nПопробуйте формат ДД:ММ:ГГГГ.",
                "\nИли убедитесь, что дата дедлайна не из прошлого.",
                style="bold red"
            )

    def remove(self, arg: str = 'done') -> None:
        if arg == 'done':
            delete_done_tasks()
            return console.print(
                "Выполненные задачи удалены!",
                style="bold red",
            )
        elif arg == 'all':
            delete_all()
            return console.print(
                "Все задачи удалены!",
                style="bold red",
            )

    def help(self) -> None:
        with open("HELP.md") as help:
            markdown = Markdown(help.read())
        return console.print(markdown)

    def readme(self) -> None:
        readme_path = f"{Path(__file__).parents[1]}/README.md"
        with open(readme_path) as readme:
            markdown = Markdown(readme.read())
        return console.print(markdown)


if __name__ == "__main__":
    task = TaskManager()
    fire.Fire(task)
