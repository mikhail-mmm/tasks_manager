from dataclasses import dataclass


@dataclass(frozen=True)
class UndoneTasks:
    id: list[int]
    tasks: list[str]
    creation_dates: list[str]
    deadlines: list[str]
    time_left: list[str]


@dataclass(frozen=True)
class DoneTasks:
    id: list[int]
    tasks: list[str]
    creation_dates: list[str]
    deadlines: list[str]
    status: list[bool]
