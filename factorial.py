#!/usr/bin/env python3
"""Calculate the factorial of a non-negative integer."""

import argparse
import math
import sys


def factorial(number: int) -> int:
    """Return n!; factorial is defined for non-negative integers."""
    if number < 0:
        raise ValueError("number must be a non-negative integer")
    return math.factorial(number)


def main() -> int:
    parser = argparse.ArgumentParser(description="Calculate the factorial of a non-negative integer.")
    parser.add_argument("number", type=int, help="non-negative integer whose factorial is calculated")
    args = parser.parse_args()
    try:
        result = factorial(args.number)
    except ValueError as error:
        parser.error(str(error))
    print(f"{args.number}! = {result}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
