import os
import random
import time
from datetime import datetime

from rich.align import Align
from rich.console import Console

from src.utils.clear_screen import clear_screen_os
from src.utils.clear_screen import clear_screen_cursor


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
            "\n[red][bold]M[/bold]achine [bold]A[/bold]ctivity [bold]R[/bold]eporting [bold]S[/bold]ystem[red]\n",
            justify="center",
        )
        self.console.print(self.data)
        self.console.print(
            "MAKE A PROPER PLAN TO AVOID TECH DEBT",
            style="bold red" + self.flash_status,
            justify="center",
        )
        self.console.print(
            "\n[bold red]M.A.R.S.[/bold red] v0.0.1-alpha",
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
            if not self.initial_screen_cleared:
                clear_screen_os()
                self.initial_screen_cleared = True
