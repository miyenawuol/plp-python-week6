"""Utility functions with safe handling for common errors."""


def safe_divide(a, b):
    """Return a / b, or a friendly message when division by zero occurs."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def safe_number(text):
    """Convert text to an integer, or return a friendly error message."""
    try:
        return int(text)
    except ValueError:
        return "Not a number"


def get_field(learner, key):
    """Return a value from a dictionary, or a friendly message if missing."""
    try:
        return learner[key]
    except KeyError:
        return "Field not found"


def demo():
    """Run a simple example of each utility function."""
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_number("42"))
    print(safe_number("abc"))

    learner = {"name": "Amina", "score": 82}
    print(get_field(learner, "score"))
    print(get_field(learner, "email"))
    