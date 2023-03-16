from dataclasses import dataclass


@dataclass(frozen=True)
class GettingTasks:
    id: list[int]
    tasks: list[str]
    creation_dates: list[str]
    deadlines: list[str]
    status: list[bool]
