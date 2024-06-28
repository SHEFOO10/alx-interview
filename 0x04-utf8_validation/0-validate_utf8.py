#!/usr/bin/python3
""" 0. UTF-8 Validation """


def calcBytes(num):
    """ calculate number of bytes of the given number """
    mask = (1 << 8 - 1)
    nBytes = 0
    while mask & num:
        mask >>= 1
        nBytes += 1
    return nBytes


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """
    i = 0
    while i < len(data):
        byte = calcBytes(data[i])
        boundry = i + byte - (byte != 0)
        i += 1
        if byte == 1 or byte > 4 or boundry >= len(data):
            return False
        while i < len(data) and i <= boundry:
            currentItem = calcBytes(data[i])
            if currentItem != 1:
                return False
            i += 1
    return True
