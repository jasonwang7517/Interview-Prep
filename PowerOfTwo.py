"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

class PowerOfTwo(object):
    def isPowerOfTwo(self, n):
        while abs(n) > 2:
            if abs(n) % 2 == 1:
                return False
            n /= 2
        if n <= 2 and n > 0:
            return True
        return False
        