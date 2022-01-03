"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""

class HappyNumber(object):
    def isHappy(self, n):
        seen = set()
        digits = list(str(n))
        while True:
            curr_sum = 0
            for i in digits:
                curr_sum += int(i) ** 2
            if curr_sum == 1:
                return True
            if curr_sum in seen:
                return False
            seen.add(curr_sum)
            digits = list(str(curr_sum))