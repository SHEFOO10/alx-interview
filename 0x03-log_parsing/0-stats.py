#!/usr/bin/python3
""" 0-stats """
import sys


codes_hits = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0}
Total_size = 0


def print_stats():
    print('File size: {}'.format(Total_size))
    for status_code, hits in codes_hits.items():
        if hits > 0:
            print('{}: {}'.format(status_code, hits))


requests = 0

try:
    for line in sys.stdin:
        line_list = line.split()
        if len(line_list) > 4:
            requests += 1
            status, file_size = line_list[-2], int(line_list[-1])
            codes_hits[status] += 1
            Total_size += file_size
            if requests == 10:
                print_stats()
                requests = 0
except Exception:
    pass
finally:
    print_stats()
