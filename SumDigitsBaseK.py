"""
Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.

After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.
"""

class SumDigitsInBaseK(object):
    def sumBase(self, n, k):
        ans = 0
        while n > 0:
            ans += n % k
            n //= k
        return ans