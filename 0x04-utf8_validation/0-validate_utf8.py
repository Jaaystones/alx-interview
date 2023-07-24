#!/usr/bin/env python3
"""
A python  method that determines if
a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Checks if a list of integers are valid UTF-8 codepoints.
    """
    count = 0

    for d in data:
        if count == 0:
            if d & 0b10000000 == 0:  # 1-byte character
                count = 0
            elif d & 0b11100000 == 0b11000000:  # 2-byte character
                count = 1
            elif d & 0b11110000 == 0b11100000:  # 3-byte character
                count = 2
            elif d & 0b11111000 == 0b11110000:  # 4-byte character
                count = 3
            else:
                return False
        else:
            if d & 0b11000000 != 0b10000000:  # Continuation byte
                return False
            count -= 1

    if count == 0:
        return True

    return False
