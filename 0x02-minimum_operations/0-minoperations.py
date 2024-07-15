#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    # clipboard = 'H'
    # current_length = 'H'
    # operation_needed = 0
    if n <= 1:
        return 0

    operation_needed = 0
    clipbord = 0
    current_length = 1
    while (n > current_length):
        # if n is div by current length, we can copy all
        if n % current_length == 0:
            # this only time we can copy
            operation_needed += 1
            clipbord = current_length

        operation_needed += 1
        current_length += clipbord
    return operation_needed
