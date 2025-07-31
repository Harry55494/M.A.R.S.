from rich.console import Console


def boot_message():
    """
    Boot message to print to the console when the application starts.
    :return: None
    """

    console = Console()

    print("\n")
    console.print("M.A.R.S.", style="bold red", justify="center")
    console.print(
        "Machine Activity Reporting System",
        justify="center",
    )
    console.print(
        "v0.0.1-Alpha",
        justify="center",
    )
    print("\n")
