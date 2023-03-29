from datetime import date, datetime

from rich.console import Console
from rich.table import Table

CONSOLE = Console()


def create_print_table_undone_tasks() -> Table:
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("No.", style="bold yellow")
    table.add_column("Task", style="italic green")
    table.add_column("Created at", style="cyan")
    table.add_column("Deadline", style="magenta")
    table.add_column("Time left", style="red")
    return table


def create_print_table_done_tasks() -> Table:
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("No.", style="bold yellow")
    table.add_column("Task", style="italic green")
    table.add_column("Created at", style="cyan")
    table.add_column("Deadline", style="magenta")
    table.add_column("Status", style="bold green")
    return table


def str_to_date(input_date_str: str) -> date | None:
    try:
        date_datetime = datetime.strptime(input_date_str, "%d.%m.%Y").date()
        return date_datetime
    except ValueError:
        return None
