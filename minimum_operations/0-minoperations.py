#!/usr/bin/python3
"""
Module for calculating minimum operations needed to get n H characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly
    n H characters in the file.

    The solution is based on prime factorization. To achieve n characters,
    we need to find all prime factors of n and sum them up.

    Args:
        n (int): The target number of H characters

    Returns:
        int: Minimum number of operations needed, or 0 if impossible

    Example:
        >>> minOperations(9)
        6
        >>> minOperations(12)
        7
        >>> minOperations(1)
        0
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Find all prime factors and sum them
    while n > 1:
        # While n is divisible by divisor
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
