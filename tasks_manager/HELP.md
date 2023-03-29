## Список доступных команд

1. `python task.py add <"task"> <deadline>` - добавляет задачу.
    - `<"task">` - название задачи,
    - `<deadline>` - дедлайн, формат ввода: ДД.ММ.ГГГГ.
2. `python task.py show` - выводит список невыполненных задач 
3. `python task.py move <task_number>` - изменяет статус задачи на выполненно.
    - `<task_number>` можно узнать вызвав команду `python task.py show`.
4. `python task.py history` - выводит список выполненных задач.
5. `python task.py change <task_number> <new_deadline>` - изменяет дедлайн для задачи.
    - `<task_number>` - можно узнать вызвав команду `python task.py show`,
    - `<new_deadline>` - новый дедлайн, формат ввода: ДД.ММ.ГГГГ.
6. `python task.py remove` - удаляет выполненные задачи.
7. `python task.py remove all` - удаляет все задачи.
8. `python task.py help` - выводит справку.
9. `python task.py readme` - выводит файл README.md.
