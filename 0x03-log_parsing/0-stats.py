#!/usr/bin/python3
""" 0-stats """
import sys
import re
import signal


def print_stats(codes_hits, size):
    sys.stdout.write(f'File size: {size}\n')
    for status_code, hits in codes_hits.items():
        sys.stdout.write(f'{status_code}: {hits}\n')
    sys.stdout.flush()


def handle_SIGINT(signum, frame):
    print_stats(codes_hits, Total_size)


signal.signal(signal.SIGINT, handle_SIGINT)

codes_hits = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
Total_size = 0
requests = 0

for line in sys.stdin:
    match = re.match(
        r'^.+ - \[[0-9-]+ [\d:\.]+\]'
        r' "GET /projects/260 HTTP/1.1" (\d+) (\d+)$',
        line
        )
    if match:
        requests += 1
        status, file_size = [
            int(match.group(1)),
            int(match.group(2))
        ]
        codes_hits[status] += 1
        Total_size += file_size
        if requests % 10 == 0:
            print_stats(codes_hits, Total_size)
