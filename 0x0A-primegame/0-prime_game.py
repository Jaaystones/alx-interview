#!/usr/bin/python3
'''Prime Game
'''
from typing import List


def isWinner(x: int, nums: List[int]) -> str:
    ''' This function take turns choosing a prime number
    from the set and removing that number and its multiples from the set.
    The player that cannot make a move loses the game
    '''
    def is_prime(num: int) -> bool:
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_primes(n: int) -> List[int]:
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_win(n: int) -> bool:
        primes = get_primes(n)
        dp = [False] * (n + 1)
        dp[0] = False
        dp[1] = False
        for i in range(2, n + 1):
            for prime in primes:
                if i - prime >= 0 and not dp[i - prime]:
                    dp[i] = True
                    break
        return dp[n]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
