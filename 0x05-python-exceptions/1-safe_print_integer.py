#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    success = True
    try:
        formatted_value = "{:d}".format(value)
    except (TypeError, ValueError):
        success = False
    else:
        print(formatted_value)
    finally:
        return success
