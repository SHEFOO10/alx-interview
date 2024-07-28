#!/usr/bin/python3
""" 0. Change comes from within """


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins
    needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Initialize the number of changes and current value
    changes = 0
    remaining_total = total

    # Iterate over each coin
    for coin in coins:
        if remaining_total == 0:
            break
        if coin <= remaining_total:
            count = remaining_total // coin
            changes += count
            remaining_total -= coin * count

    # If we have exactly made the total
    if remaining_total == 0:
        return changes
    return -1
