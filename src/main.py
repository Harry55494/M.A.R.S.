import json
import os
import time

from dotenv import load_dotenv

from display.Formatter import Formatter
from utils.boot_message import boot_message
from utils.clear_screen import clear_screen_os

if __name__ == "__main__":
    load_dotenv()
    boot_message()
    if not os.environ.get("MODE") == "development":
        time.sleep(5)

    # Initialize the formatter

    formatter = Formatter()

    clear_screen_os()

    # Start main loop

    formatter.set_data(json.loads(os.environ["SERVICES"]))
    formatter.format_loop()
