#!/usr/bin/python3


"""
A script that reads stdin line by line and computes metrics
"""

import sys


def print_stats(status_codes, file_size):
    """
    prints stats

    Arguments:
        status_codes {dict} -- [dictionary of status codes]
        file_size {int} -- [file size]
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    file_size = 0
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            split_line = line.split()
            try:
                file_size += int(split_line[-1])
            except [ValueError, IndexError]:
                pass
            try:
                status_codes[split_line[-2]] += 1
            except [KeyError, IndexError]:
                pass
            if count % 10 == 0:
                print_stats(status_codes, file_size)
        print_stats(status_codes, file_size)
    except KeyboardInterrupt:
        print_stats(status_codes, file_size)
        raise
