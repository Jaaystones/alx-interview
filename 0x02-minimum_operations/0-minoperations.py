#!/usr/bin/python3
"""
Calculates the minimum number of operations
required to create a certain number of characters
given that there is only one function to copy everything
and one to paste.
"""


def min_operations(n):
    """
    Calculates the minimum number of operations
    required to create 'n' characters.

    Args:
        n (int): The desired number of characters.

    Returns:
        int: The minimum number of operations required.
        Returns 0 if 'n' is less than or equal to 1.

    """
    p = 0

    if n <= 1:
        return p

    for i in range(2, n + 1):
        while 0 == n % i:
            p = p + i
            n = n / i
            if n < i:
                break
    return p
