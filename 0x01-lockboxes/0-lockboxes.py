#!/usr/bin/python3
"""
    n number of locked boxes.
    Each box is numbered sequentially from 0 to n - 1 and
    each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """ Check if I can unlock all boxes """
    keys = set(boxes[0])
    keys.add(0)
    unlocked = set([0])

    while True:
        new_keys = set()
        for key in keys:
            if key < len(boxes):
                new_keys.update(boxes[key])
        if new_keys.issubset(unlocked):
            break
        unlocked.update(new_keys)
        keys = new_keys
    return len(unlocked) == len(boxes)
