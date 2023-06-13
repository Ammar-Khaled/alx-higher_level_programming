#!/usr/bin/python3
""" This script reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
    * Total file size: File size: <total size>
        where is the sum of all previous (see input format above)
    * Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        if a status code doesn't appear, it is not printed
        format: <status code>: <number>
        status codes are printed in ascending order
"""

import sys


class Struct:
    """ structure for keeping information."""

    def __init__(self):
        """ init method."""
        self.file_size = 0
        self.status_codes = {}

    def init_codes(self):
        """ initialise dict."""
        self.status_codes = {'200': 0,
                             '301': 0,
                             '400': 0, '401': 0, '403': 0, '404': 0, '405': 0,
                             '500': 0}

    def add_status_code(self, code):
        """ update counter for givin code."""
        if code in self.status_codes:
            self.status_codes[code] += 1

    def print_info(self):
        """ print information"""
        print("File size: {}".format(self.file_size))
        for code in sorted(self.status_codes):
            if self.status_codes[code] != 0:
                print("{}: {:d}".format(code, self.status_codes[code]))


if __name__ == "__main__":
    counter = 0
    struct = Struct()
    struct.init_codes()

    try:
        for line in sys.stdin:
            if counter % 10 == 0 and counter != 0:
                struct.print_info()

            try:
                line_list = line.split(" ")
                for i in range(len(line_list)):
                    line_list[i] = line_list[i].strip()

                struct.add_status_code(line_list[-2])
                struct.file_size += int(line_list[-1].strip("\n"))

            except Exception:
                pass

            counter += 1

    except KeyboardInterrupt:
        struct.print_info()
        raise

    struct.print_info()
