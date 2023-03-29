# # tasks_manager

Консольная утилита для трекинга задач.

### Описание
Данная утилита позволяет создавать задачи с дедлайнами, просматривать их и менять статус (выполнено/невыполнено).

### Запуск

1. Для добавления задачи `python task.py add <"task"> <deadline>`.
    - `<"task">` - название задачи,
    - `<deadline>` - дедлайн, формат ввода: ДД.ММ.ГГГГ.
2. Для вывода списка невыполненных задач `python task.py show`.
3. Для изменения статуса задачи `python task.py move <task_number>`.
    - `<task_number>` можно узнать вызвав команду `python task.py show`.
4. Для вывода списка выполненных задач `python task.py history`.
5. Для изменения дедлайна задачи `python task.py change <task_number> <new_deadline>`.
    - `<task_number>` - можно узнать вызвав команду `python task.py show`,
    - `<new_deadline>` - новый дедлайн, формат ввода: ДД.ММ.ГГГГ.
6. Для удаления списка выполненных задач `python task.py remove`.
7. Для удаления списка всех задач `python task.py remove all`.
8. Для вывода справки `python task.py help`
9. Для вывода README `python task.py readme`.
