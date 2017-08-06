#!/usr/bin/env python3

"""
Project Euler #34.

Given is the arithmetic-geometric sequence u(k) = (900-3k)r^(k-1).
Let s(n) = Σ_(k=1...n)u(k)$.

Find the value of r for which s(5000) = -600,000,000,000.

Give your answer rounded to 12 places behind the decimal point.
"""

from functools import partial
from math import copysign

TARGET = -600_000_000_000

r = 1
jump = 0.1
n = 5000


def u(k, r):
    """Function u given in problem."""
    return (900 - 3 * k) * r ** (k - 1)


def s(n, r):
    """Function s given in problem."""
    return sum(map(partial(u, r=r), range(1, n + 1)))


sum_ = s(n, r)

while abs(TARGET - sum_) > 1:
    r += copysign(jump, s(n, r) - TARGET)
    jump /= 2
    sum_ = s(n, r)

print(f'{r:.12f}')
