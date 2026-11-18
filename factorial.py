#!/usr/bin/env python3
"""Calculate n! for a non-negative whole number."""

import argparse


def factorial(number: int) -> int:
    """Multiply the integers from 2 through number."""
    if number < 0:
        raise ValueError("number must be zero or greater")

    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Calculate the factorial of a non-negative integer."
    )
    parser.add_argument(
        "number",
        type=int,
        help="the number whose factorial should be calculated",
    )
    args = parser.parse_args()

    if args.number < 0:
        parser.error("number must be zero or greater")

    print(f"{args.number}! = {factorial(args.number)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
