#!/usr/bin/python3

"""This script reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
it prints those statistics since the beginning:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous lines
        (see input format above)
        Number of lines by status code:
            Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
            If a status code doesn’t appear, it doesn’t print anything for
            that status code.
            The status codes are printed in ascending order.
"""


def print_metrics(size, status_codes):
    """Print the metrics for HTTP status codes.

    Args:
        size (int): The file size.
        status_codes (dict): HTTP status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0
    try:
        for line in sys.stdin:
            if line_count == 10:
                print_metrics(size, status_codes)
                line_count = 1
            else:
                line_count += 1
            line = line.split()
            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass
            try:
                if line[-2] in codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass
        print_metrics(size, status_codes)
    except KeyboardInterrupt:
        print_metrics(size, status_codes)
        raise
