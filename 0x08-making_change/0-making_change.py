#!/usr/bin/python3
'''Determine the fewest number of coins needed to meet a given amount total
'''


def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0

    # Initialize the table with sys.maxsize except for 0
    table = [0] + [float('inf')] * total

    for coin in coins:
        for i in range(coin, total + 1):
            table[i] = min(table[i], table[i - coin] + 1)

    return table[total] if table[total] != float('inf') else -1
