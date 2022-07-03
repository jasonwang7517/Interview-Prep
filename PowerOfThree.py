"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""

class PowerOfThree(object):
    def isPowerOfThree(self, n):
        while n >= 3:
            if n % 3 != 0:
                return False
            n = n // 3
        return n == 1