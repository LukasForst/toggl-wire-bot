from typing import Tuple


def convertMillis(millis: int) -> Tuple[int, int, int]:
    """
    Takes milliseconds and returns triple seconds, minutes, hours
    """
    seconds, milliseconds = divmod(millis, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    seconds = int(seconds + milliseconds / 1000)
    return hours, minutes, seconds


def millisToText(millis: int) -> str:
    """
    Takes milliseconds record and returns text conversion.
    """
    hours, minutes, _ = convertMillis(millis)
    return f"{hours} hours {minutes} minutes"
