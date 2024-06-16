#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
Given a number n,write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    Return: int
    if n is impossible to achieve, return 0
    """
    body = 'H'
    next = 'H'
    n_operations = 0
    while len(body) < n:
        if n % len(body) == 0:
            n_operations += 2
            next = body
            body += body
        else:
            n_operations += 1
            body += next
    if len(body) != n:
        return 0
    return n_operations
