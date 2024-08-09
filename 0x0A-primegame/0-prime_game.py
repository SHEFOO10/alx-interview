#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            benWinsCount += 1
            continue

        isMariaTurn = True

        while (True):
            if not primesSet:
                if isMariaTurn:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break
            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]
            isMariaTurn = not isMariaTurn
    if mariaWinsCount > benWinsCount:
        return "Maria"
    elif benWinsCount > mariaWinsCount:
        return "Ben"
    return None


def is_prime(n):
    """ check if the number is prime """
    if n < 2:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


def primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes
