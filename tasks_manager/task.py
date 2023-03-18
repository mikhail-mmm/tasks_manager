import fire

from db.utils_db import (insert_task, get_undone_tasks, delete_done_tasks,
                         change_task_status, get_done_tasks, change_deadline,
                         delete_all_tasks)
from pathlib import Path
from rich.markdown import Markdown
from utils import (create_print_table_undone_task, create_print_table_done_task,
                   str_to_date, console)


class TaskManager:

    def add(self, task: str, deadline: str) -> None:
        deadline_datetime = str_to_date(deadline)
        if deadline_datetime:
            if insert_task(task, deadline_datetime):
                return console.print(
                    f"Задача {task} добавлена успешно! Deadline: {deadline}",
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
        table = create_print_table_undone_task()
        undone_task = get_undone_tasks()
        if undone_task:
            for i in range(len(undone_task.id)):
                table.add_row(
                    str(undone_task.id[i]), undone_task.tasks[i], undone_task.creation_dates[i],
                    undone_task.deadlines[i], f"{undone_task.time_left[i]} day(s)",
                    )
            return console.print(table)
        return console.print(
                    "Ошибка. Нет связи с БД! Или БД пуста!",
                    style="bold red",
                )

    def move(self, selected_task: str) -> None:
        if change_task_status(int(selected_task)):
            return console.print(
                    f"Задача номер {selected_task} выполнена!",
                    "\n:thumbs_up:",
                    style="bold green",
                )
        return console.print(
            f"Задача номер {selected_task} не найдена!",
            "\n:thumbs_down:",
            "\nПопробуйте вызвать команду <show>, чтобы убедиться в правильности номера задачи.",
            "\nИли убедитесь, что база данных доступна.",
            style="bold red"
        )

    def history(self) -> None:
        table = create_print_table_done_task()
        done_task = get_done_tasks()
        if done_task:
            for i in range(len(done_task.id)):
                table.add_row(
                    str(done_task.id[i]), done_task.tasks[i], done_task.creation_dates[i],
                    done_task.deadlines[i], "Done",
                    )
            return console.print(table)
        return console.print(
            "Ошибка. Нет связи с БД! Или БД пуста!",
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
                    f"Задача номер {task_number} не найдена!",
                    "\n:thumbs_down:",
                    "\nПопробуйте вызвать команду <show>, чтобы убедиться в правильности номера задачи.",
                    "\nИли убедитесь, что база данных доступна.",
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
            if delete_done_tasks():
                return console.print(
                    "Выполненные задачи удалены!",
                    style="bold red",
                )
            return console.print(
                    "Ошибка. Нет связи с БД! Или БД пуста!",
                    style="bold red",
                )
        elif arg == 'all':
            if delete_all_tasks():
                return console.print(
                    "Все задачи удалены!",
                    style="bold red",
                )
            return console.print(
                    "Ошибка. Нет связи с БД! Или БД пуста!",
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
