#!/usr/bin/python3
'''
calculates the minimum amount of processes necessary
to create a certain number of characters.
You must imagine that there is only one function
to copy everything and one to paste.
'''

import math


def min_operations(n):
    """
    Calculates the fewest number of operations needed to achieve exactly n 'H' characters in a text file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The fewest number of operations needed. Returns 0 if it is impossible to achieve.

    """
    if n == 1:
        return 0

    # Finding the smallest factor of n
    smallest_factor = None
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            smallest_factor = i
            break

    if smallest_factor is None:
        return n

    # Perform "Copy All" once and "Paste" smallest_factor - 1 times
    return 1 + min_operations(n // smallest_factor)
