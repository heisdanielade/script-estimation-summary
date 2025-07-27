from datetime import datetime
from typing import Callable

from colorama import init, Fore, Style

init(autoreset=True)

check_availability: Callable[[str],
                             str] = lambda val: val if val is not None else "n/a"


def indicate_priority(value: str) -> str:
    """Return colored text based on issue priority level."""
    priority_map: dict = {
        "urgent": Fore.LIGHTRED_EX,
        "high": Fore.LIGHTYELLOW_EX,
        "medium": Fore.LIGHTBLUE_EX,
        "low": Fore.LIGHTBLUE_EX
    }
    color = priority_map.get(value.lower())
    return f"{color}{value}{Style.RESET_ALL}" if color else value


def indicate_deadline(date: str, date_format: str = "%Y-%m-%d") -> str:
    """Return colored text to indicate passed issue deadline."""
    try:
        parsed_date = datetime.strptime(date, date_format)
    except ValueError:
        return date

    current_date = datetime.now()

    if current_date >= parsed_date:
        return f"{Fore.LIGHTRED_EX}{date}{Style.RESET_ALL}"

    return date
