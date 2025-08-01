import random
import time
from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console
from rich.table import Table

from src.utils.clear_screen import clear_screen_cursor
from src.utils.clear_screen import clear_screen_os


class Formatter:

    def __init__(self):
        print("Formatter initialized")
        self.data = None
        self.console = Console()
        self.flash_status = " dim"
        self.initial_screen_cleared = False

    def set_data(self, data):
        self.data = data

    def invert_flash_status(self):
        """
        Inverts the flash status for the console output.
        This is used to toggle the visibility of the flash effect.
        """
        if self.flash_status == " dim":
            self.flash_status = " "
        else:
            self.flash_status = " dim"

    def format_and_print(self):
        """
        Formats and prints the given data.

        :param data: The data to format and print.
        :return: None
        """

        self.console.print(
            "\n[underline]HOMELAB STATUS[/underline]\n", justify="center", style="bold"
        )

        overall_table = Table(
            show_header=False,
            header_style="bold magenta",
            show_lines=False,
            box=None,
        )

        overall_table.add_column()
        overall_table.add_column()

        table = Table(
            show_header=True,
            header_style="bold magenta",
            show_lines=False,
            box=box.MINIMAL,
        )

        table.add_column("Service", style="cyan", no_wrap=True, width=20)
        table.add_column("Status", style="green", no_wrap=True, width=10)
        table.add_column("Uptime", style="yellow", no_wrap=True, width=10)

        table.add_row("test", "up", "5m")

        overall_table.add_row(table, table)

        self.console.print(
            overall_table,
            justify="center",
        )

        self.console.print(
            "\n[bold][underline]UPDATES[/bold][/underline]\n",
            justify="center",
        )
        self.console.print(
            "MAKE A PROPER PLAN TO AVOID TECH DEBT",
            style="bold red" + self.flash_status,
            justify="center",
        )

        print("\n" * 5)

        self.console.print(
            "\n[red][bold]M[/bold]achine [bold]A[/bold]ctivity [bold]R[/bold]eporting [bold]S[/bold]ystem[red] [green]v0.0.1-alpha[/green]",
            style="dim",
            justify="center",
        )
        self.console.print(
            Align.center(
                datetime.now().strftime(" %H:%M:%S %d-%m-%Y"),
                style="dim",
                vertical="bottom",
            )
        )
        self.invert_flash_status()

    def format_loop(self):
        while True:
            if self.data is not None:
                self.format_and_print()
            else:
                self.console.print("No data to display.", style="bold red")
            time.sleep(0.5)
            clear_screen_cursor()
            if not self.initial_screen_cleared or random.random() < 0.01:
                clear_screen_os()
                self.initial_screen_cleared = True
