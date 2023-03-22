import enum

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, kw_only=True)
class Task:
    id: int
    task_name: str
    created_at: date
    deadline: date
    status: str


class TaskStatusSymbol(enum.Enum):
    Done = "Done"
    Undone = "Undone"
