"""
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.
"""

class ThreeDivisors(object):
    def isThree(self, n):
        divisors = 2
        for i in range(2, 1 + (n / 2)):
            if n % i == 0:
                divisors += 1
                if divisors > 3:
                    return False
        return divisors == 3
        