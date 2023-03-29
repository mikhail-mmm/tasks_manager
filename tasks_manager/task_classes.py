import enum

from dataclasses import dataclass
from datetime import date


class TaskStatus(enum.Enum):
    Done: str = "Done"
    Undone: str = "Undone"


@dataclass(frozen=True, kw_only=True)
class Task:
    id: int
    task_name: str
    created_at: date
    deadline: date
    status: TaskStatus
