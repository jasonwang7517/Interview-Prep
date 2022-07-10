"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""

class Solution(object):
    def mySqrt(self, x):
        if x <= 1:
            return x
        left = 0
        right = x
        while right - left > 1:
            middle = (right + left) // 2
            if middle ** 2 == x:
                return middle
            elif middle ** 2 > x:
                right = middle
            elif middle ** 2 < x:
                left = middle
        return left
        