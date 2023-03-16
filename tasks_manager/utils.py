from datetime import date

from rich.console import Console
from rich.table import Table

console = Console()


def create_print_table() -> Table:
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("No.", style="bold blue")
    table.add_column("Task", style="italic green")
    table.add_column("Creation date")
    table.add_column("Deadline")
    table.add_column("Status")
    return table


def str_to_date(input_date_str: str) -> date | None:
    if "." in input_date_str:
        date_parts = input_date_str.split('.')
        if len(date_parts) == 3:
            try:
                date_parts_int = [int(item) for item in date_parts]
                return_date = date(date_parts_int[2], date_parts_int[1], date_parts_int[0])
                delta_date = return_date - date.today()
                if delta_date.days > 0:
                    return return_date
            except ValueError:
                return None
    else:
        return None
