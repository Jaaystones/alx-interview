#!/usr/bin/python3
'''Task
'''

import math


def minOperations(n):
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
    return 1 + minOperations(n // smallest_factor)
