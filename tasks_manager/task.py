import fire

from db.utils_db import (insert_task, get_undone_tasks, delete_done_date,
                         chenge_task_status, get_done_tasks)
from rich.console import Console
from utils import create_print_table, str_to_date, console


class TaskManager:
    """Консольная утилита для трэккинга задач."""

    def add(self, task: str, deadline: str) -> None:
        """Команда добавляет задачу и дедлайн."""
        deadline_datetime = str_to_date(deadline)
        if deadline_datetime:
            insert_task(task, deadline_datetime)
            return console.print(
                f"Задача {task} добавлена успешно! Deadline: {deadline}",
                "\n:thumbs_up:",
                style="bold green",
            )
        return console.print(
            f"Неверный формат ввода даты дедлайна: {deadline}!",
            "\n:thumbs_down:",
            "\nПопробуйте формат ДД:ММ:ГГГГ.",
            "\nИли убедитесь, что дата дедлайне не из прошлого.",
            style="bold red"
        )

    def remove(self) -> None:
        """Удаляет выполненные задачи."""
        delete_done_date()
        return console.print(
            "Данные удалены!",
            style="bold red",
        )

    def show(self) -> None:
        table = create_print_table()
        undone_task = get_undone_tasks()
        for i in range(len(undone_task.id)):
            table.add_row(
                str(undone_task.id[i]), undone_task.tasks[i], undone_task.creation_dates[i],
                undone_task.deadlines[i], "Undone",
                )
        return console.print(table)

    def move(self, task_number: str) -> None:
        """Отмечает задачу как выполненную."""
        if chenge_task_status(int(task_number)):
            return console.print(
                    f"Задача номер {task_number} выполнена!",
                    "\n:thumbs_up:",
                    style="bold green",
                )
        return console.print(
            f"Задача номер {task_number} не найдена!",
            "\n:thumbs_down:",
            "\nПопробуйте вызвать команду <show>, чтобы убедиться в правильности номера задачи.",
            "\nИли убедитесь, что база данных доступна.",
            style="bold red"
        )

    def history(self):
        """Выводит историю всех задач."""
        table = create_print_table()
        done_task = get_done_tasks()
        if done_task:
            for i in range(len(done_task.id)):
                table.add_row(
                    str(done_task.id[i]), done_task.tasks[i], done_task.creation_dates[i],
                    done_task.deadlines[i], "Done",
                    )
            return console.print(table)
        return console.print(
            "Ошибка. Нет связи с БД!",
            style="bold red"
        )

    # def change(self, number_task, new_deadline):
    #     """Позволяет изменить дедлайн."""
    #     pass

    def help(self):
        """Выводит справку по работе с утилитой."""
        pass


if __name__ == "__main__":
    task = TaskManager()
    fire.Fire(task)
