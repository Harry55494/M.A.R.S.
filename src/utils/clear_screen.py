import os


def clear_screen_os():
    """
    Clear the terminal screen using os method.
    """
    import os
    import platform

    # Determine the command based on the operating system
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def clear_screen_cursor():
    """
    Clear the terminal screen using ANSI escape codes.
    """
    terminal_height = os.get_terminal_size().lines + 15
    print(
        f"\033[{terminal_height}A\033[2K", end=""
    )  # Move cursor to home and clear screen
