from datetime import date
from dateutil.parser import parse
from dateutil.parser._parser import ParserError

from rich.console import Console
from rich.table import Table

console = Console()


def create_print_table_undone_task() -> Table:
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("No.", style="bold yellow")
    table.add_column("Task", style="italic green")
    table.add_column("Creation date", style="cyan")
    table.add_column("Deadline", style="magenta")
    table.add_column("Time left", style="red")
    return table


def create_print_table_done_task() -> Table:
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("No.", style="bold yellow")
    table.add_column("Task", style="italic green")
    table.add_column("Creation date", style="cyan")
    table.add_column("Deadline", style="magenta")
    table.add_column("Status", style="bold green")
    return table


def str_to_date(input_date_str: str) -> date | None:
    try:
        date_datetime = parse(input_date_str).date()
        return date_datetime
    except ParserError:
        return None
