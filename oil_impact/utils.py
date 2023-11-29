import re


def remove_whitespace(string: str) -> str:
    """
    Remove all whitespace characters from a string.

    Args:
        string (str): The string to remove whitespace from.

    Returns:
        str: The input string with all whitespace characters removed.
    """
    return re.sub(r"\s+", "", string)
