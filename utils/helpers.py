import re

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def prompt_input(message):
    return input(message).strip()


def prompt_int(message):
    """Ask for a whole number, or return None if the answer isn't one."""
    answer = prompt_input(message)
    return int(answer) if answer.isdigit() else None


def is_valid_email(email):
    return bool(EMAIL_PATTERN.match(email))
