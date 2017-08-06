#!/usr/bin/env python3

"""
Project Euler #34.

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.
"""

from math import factorial
from itertools import combinations_with_replacement as cwr

FACTORIALS = {str(i): factorial(i) for i in range(10)}

factorial_sum = 0

for n in range(2, 7):
    for c in cwr(map(str, range(0, 10)), n):
        c_sum = sum(map(FACTORIALS.__getitem__, c))
        if sorted(c) == sorted(str(c_sum)):
            factorial_sum += c_sum

print(factorial_sum)
