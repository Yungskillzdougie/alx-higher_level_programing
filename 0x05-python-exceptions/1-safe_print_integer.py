#!/usr/bin/python3

def safe_print_interger(value):
    """"Print integer with "{:d}".format().

    Args:
    value (int): integer to print.

    Returns:
    if TypeError or valueError occurs - False.
    Otherwise - True.
    """
    Try:
        print("{:d}".format(value))

        return(True)

    except(TYpeError, ValueError):

        return(False)
