#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        import sys
        sys.stderr.write("Exception: {}\n".format(e))
        return False
