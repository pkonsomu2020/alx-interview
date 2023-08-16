#!/usr/bin/python3
import signal
import sys

def print_stats(signal, frame):
    print("File size:", total_size)
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))
    sys.stdout.flush()

signal.signal(signal.SIGINT, print_stats)

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0

for line in sys.stdin:
    line_parts = line.split()
    if len(line_parts) == 9:
        try:
            status_code = int(line_parts[7])
            file_size = int(line_parts[8])
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size
            line_count += 1
        except ValueError:
            pass
    if line_count == 10:
        print_stats(None, None)
        line_count = 0
