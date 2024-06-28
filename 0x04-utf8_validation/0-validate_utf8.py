#!/usr/bin/python3

def validUTF8(data):
    def check(num):
        """ get number of bytes for the given number """
        mask = (1 << 8-1)  # 0b10000000
        numOfBytes = 0
        while num & mask:
            mask >>= 1
            numOfBytes += 1
        return numOfBytes

    i = 0
    while i < len(data):
        nbyte = check(data[i])
        boundry = i + nbyte - (nbyte != 0)
        i += 1
        if nbyte == 1 or nbyte > 4 or boundry >= len(data):
            return False

        while i < len(data) and i <= boundry:
            currentItem = check(data[i])
            if currentItem != 1:
                return False
            i += 1
        return True
