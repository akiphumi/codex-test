"""Main module for codex-test."""

import argparse


def add(a, b):
    """Return the sum of *a* and *b*.

    If either argument is ``None``, it is treated as ``0``. This allows the
    function to handle missing values gracefully.
    """
    if a is None and b is None:
        return 0
    if a is None:
        return b
    if b is None:
        return a
    return a + b


def main(argv=None):
    parser = argparse.ArgumentParser(description="Add two numbers")
    parser.add_argument("a", type=int, nargs="?", help="First number")
    parser.add_argument("b", type=int, nargs="?", help="Second number")
    args = parser.parse_args(argv)

    result = add(args.a, args.b)
    print(result)


if __name__ == "__main__":
    main()
