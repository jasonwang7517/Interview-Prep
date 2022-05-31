"""
You are given a 0-indexed string num of length n consisting of digits.

Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.
"""

from collections import defaultdict

class CheckIfNumberHasEqualDigitCountAndDigitValue(object):
    def digitCount(self, num):
        counts = defaultdict(lambda: 0)
        for i in num:
            counts[int(i)] += 1
        for i in range(len(num)):
            if counts[i] != int(num[i]):
                return False
        return True
        