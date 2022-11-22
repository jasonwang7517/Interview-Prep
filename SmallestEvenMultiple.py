"""
Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
"""

class SmallestEvenMultiple(object):
    def smallestEvenMultiple(self, n):
        return n if n % 2 == 0 else n * 2