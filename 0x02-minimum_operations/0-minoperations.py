#!/usr/bin/python3
"""
This module contains a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
Prototype: `minOperations(n)`
Returns: integer
if n is impossible to achieve, returns 0.
"""

def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    i = 2
    while i <= n:
        if n % i == 0:
            n //= i
            operations += i
        else:
            i += 1

    return operations

# Test cases
if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
