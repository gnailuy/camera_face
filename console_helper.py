import sys


def print_error(*args, **kwargs):
    # Print error message to stderr
    print(*args, file=sys.stderr, **kwargs)
