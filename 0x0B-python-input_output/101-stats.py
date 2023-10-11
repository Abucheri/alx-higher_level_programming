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
import sys


metrics = {
        'total_size': 0,
        'status_codes': {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0,
            }
        }
line_count = 0
lines = []
try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 2:
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                metrics['total_size'] += file_size
                if status_code in metrics['status_codes']:
                    metrics['status_codes'][status_code] += 1
                line_count += 1
                lines.append(line.strip())
                if line_count % 10 == 0:
                    print(f"File size: {metrics['total_size']}")
                    for code in sorted(metrics['status_codes']):
                        if metrics['status_codes'][code] > 0:
                            print(f"{code}: {metrics['status_codes'][code]}")
            except ValueError:
                pass
except KeyboardInterrupt:
    print(f"File size: {metrics['total_size']}")
    for code in sorted(metrics['status_codes']):
        if metrics['status_codes'][code] > 0:
            print(f"{code}: {metrics['status_codes'][code]}")
    raise
except Exception:
    raise
