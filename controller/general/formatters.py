import datetime
import locale


def format_integer(integer: int) -> str:
    return f"{integer:n}"


def format_real(f: float) -> str:
    return locale.format_string("%.2f", f, True)


def format_datetime(date: datetime.datetime) -> str:
    return date.strftime("%y-%m-%d %H:%M:%S")
