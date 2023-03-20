from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class Task:
    id: int
    task_name: str
    creation_date: str
    deadline: str
    other: str
