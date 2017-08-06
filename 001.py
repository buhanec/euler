#!/usr/bin/env python3

"""
Project Euler #1.

Find the sum of all the multiple of 3 or 5 below 1000.
"""


print(sum(n for n in range(1000) if not n % 3 or not n % 5))
