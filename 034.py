#!/usr/bin/env python3

"""
Project Euler #34.

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.
"""

from math import factorial

UPPER_BOUNDARY = 50000
FACTORIALS = {str(i): factorial(i) for i in range(10)}

factorial_sum = 0

for n in range(3, UPPER_BOUNDARY):
    n_sum = sum(FACTORIALS[i] for i in str(n))
    if n_sum == n:
        factorial_sum += n_sum

print(factorial_sum)
